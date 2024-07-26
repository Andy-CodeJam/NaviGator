import os

# from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol

import openai
from dotenv import find_dotenv, load_dotenv

from navigator_py.config import config
from navigator_py.generative_ai_provider import (
    AsyncAzureOpenAIProvider,
    AzureOpenAIProvider,
    GenerativeAIClient,
    GenerativeAICompletion,
    GenerativeAIProvider,
)

load_dotenv(find_dotenv())


@dataclass
class GenerativeAIRequest(Protocol):
    """Protocol interface for a generative AI request. At minimum,
    a request must have a connect method to establish a connection
    to the provider and a prompt method to generate a response.

    Additionally requires two properties: system_prompt and post_user_prompt.

    system_prompt: str
        The initial context given to the AI model to level set the conversation.
    post_user_prompt: str
        The context given to the AI model after the user's input to continue
        the conversation. Allows for specific instructions to be given to the model
        re: how to format the response.
    """

    @property
    def system_prompt(self) -> str: ...

    @property
    def post_user_prompt(self) -> str: ...

    def connect(self): ...

    def prompt(self, prompt: str): ...


@dataclass
class BaseAIRequest:
    _ai_provider: GenerativeAIProvider | None = None
    _max_tokens: int = int(os.getenv("OPENAI_MAX_TOKENS", 60))
    _temperature: float = float(os.getenv("OPENAI_TEMPERATURE", 0.1))
    _system_prompt: str = (
        "You are a helpful AI assistant that helps users with their questions."
    )
    _post_user_prompt: str = "Please provide a response to the user's question in a markdown format similar in structure to a blog post."
    _chat_history: list[dict] | None = None

    def __post_init__(self):
        if self._chat_history is None:
            self._chat_history = []

    @property
    def ai_provider(self) -> GenerativeAIProvider:
        if self._ai_provider is None:
            raise ValueError("AI provider is not set")
        return self._ai_provider

    @property
    def max_tokens(self) -> int:
        """Return the maximum number of tokens to generate."""
        return self._max_tokens

    @property
    def temperature(self):
        """Return the temperature to use for generating completions."""
        return self._temperature

    @property
    def system_prompt(self):
        return self._system_prompt

    @property
    def post_user_prompt(self):
        return self._post_user_prompt

    @property
    def chat_history(self):
        return self._chat_history

    def connect(self):
        self.ai_provider.connect()

    def _prompt_action(
        self, client: GenerativeAIClient, prompt: str
    ) -> GenerativeAICompletion:
        """Generate a response to the prompt using the AI provider."""
        raise NotImplementedError


@dataclass
class OpenAIRequest(BaseAIRequest):
    """Represents a basic request to the Azure OpenAI API."""

    _ai_provider: GenerativeAIProvider | None = None
    _max_tokens: int = int(os.getenv("OPENAI_MAX_TOKENS", 60))
    _temperature: float = float(os.getenv("OPENAI_TEMPERATURE", 0.1))
    _system_prompt: str = (
        "You are a helpful AI assistant that helps users with their questions."
    )
    _post_user_prompt: str = "Please provide a response to the user's question in a markdown format similar in structure to a blog post."
    _chat_history: list[dict] | None = None

    def __post_init__(self):
        if self._chat_history is None:
            self._chat_history = []
        if self._ai_provider is None:
            self._ai_provider = AzureOpenAIProvider()
            self._ai_provider.connect()

    def _prompt_action(self, client: openai.Client, prompt: str):
        return client.chat.completions.create(
            model=os.getenv("OPENAI_COMPLETIONS_MODEL"),
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
                {"role": "system", "content": self.post_user_prompt},
            ],
        )

    def _prompt(
        self,
        prompt: str,
        max_tokens: int = config.max_tokens,
        temperature: float = config.temperature,
    ):
        """Generate a response to the prompt using the Azure OpenAI API."""
        max_tokens = self.max_tokens if max_tokens is None else max_tokens
        temperature = self.temperature if temperature is None else temperature
        client = self.ai_provider.client

        try:
            response = self._prompt_action(client, prompt)
            return response.choices[0].message

        # Handle different types of errors + Error messages for debugging
        except openai.AuthenticationError as e:
            print(f"OpenAI API returned an Authentication Error: {e}")
        except openai.APIConnectionError as e:
            print(f"Failed to connect to OpenAI API: {e}")
        except openai.BadRequestError as e:
            print(f"Invalid Request Error: {e}")
        except openai.RateLimitError as e:
            print(f"OpenAI API request exceeded rate limit: {e}")
        except openai.InternalServerError as e:
            print(f"Service Unavailable: {e}")
        except openai.APITimeoutError as e:
            print(f"Request timed out: {e}")
        except openai.APIError as e:
            print(f"OpenAI API returned an API Error: {e}")
        except Exception as e:
            print(f"An exception has occured: {e}")


@dataclass
class AsyncOpenAIRequest(OpenAIRequest):
    """Represents an asynchronous request to the Azure OpenAI API. Based off the OpenAIRequest class, but overrides the _prompt method to be async."""

    @property
    def ai_provider(self) -> AsyncAzureOpenAIProvider:
        if self._ai_provider is None:
            self._ai_provider = AsyncAzureOpenAIProvider()
        return self._ai_provider

    async def _prompt_action(self, client: openai.Client, prompt: str):
        req = await client.chat.completions.create(
            model=os.getenv("OPENAI_COMPLETIONS_MODEL"),
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt},
                {"role": "system", "content": self.post_user_prompt},
            ],
        )

        return req

    async def _prompt(
        self,
        prompt: str,
        max_tokens: int = config.max_tokens,
        temperature: float = config.temperature,
    ):
        """Same as prompt, but async."""
        max_tokens = self.max_tokens if max_tokens is None else max_tokens
        temperature = self.temperature if temperature is None else temperature
        client = self.ai_provider.client

        try:
            response = await self._prompt_action(client, prompt)
            return response.choices[0].message

        # Handle different types of errors + Error messages for debugging
        except openai.AuthenticationError as e:
            print(f"OpenAI API returned an Authentication Error: {e}")
        except openai.APIConnectionError as e:
            print(f"Failed to connect to OpenAI API: {e}")
        except openai.BadRequestError as e:
            print(f"Invalid Request Error: {e}")
        except openai.RateLimitError as e:
            print(f"OpenAI API request exceeded rate limit: {e}")
        except openai.InternalServerError as e:
            print(f"Service Unavailable: {e}")
        except openai.APITimeoutError as e:
            print(f"Request timed out: {e}")
        except openai.APIError as e:
            print(f"OpenAI API returned an API Error: {e}")
        except Exception as e:
            print(f"An exception has occured: {e}")

    async def prompt(self, prompt: str):
        """
        Return a response to the given prompt. Wraps the _prompt method to allow subclasses
        to override it and use validation or other logic.
        """
        out = await self._prompt(prompt)
        return out


# @dataclass
# class HuggingfaceRequest(BaseAIRequest):
#     """Represents a request to a local Llama3 model using Hugging Face Transformers."""

#     _ai_provider: GenerativeAIProvider | None = None
#     _max_length: int = 50
#     _temperature: float = 0.7
#     _system_prompt: str = (
#         "You are a helpful AI assistant that helps users with their questions."
#     )
#     _post_user_prompt: str = (
#         "Please provide a response to the user's question in a concise format."
#     )
#     _chat_history: List[Dict[str, str]] | None = None

#     @property
#     def ai_provider(self) -> GenerativeAIProvider:
#         if self._ai_provider is None:
#             from navigator_py.generative_ai_provider import HuggingfaceProvider

#             self._ai_provider = HuggingfaceProvider()
#             self._ai_provider.connect()
#         return self._ai_provider

#     def _prompt_action(
#         self, client: GenerativeAIClient, prompt: str
#     ) -> GenerativeAICompletion:
#         response = client(
#             prompt, max_length=self._max_length, temperature=self._temperature
#         )
#         return response

#     def _prompt(self, prompt: str, max_length: int = None, temperature: float = None):
#         """Same as prompt, but async."""
#         max_length = self._max_length if max_length is None else max_length
#         temperature = self._temperature if temperature is None else temperature
#         client = self.ai_provider.client

#         response = self._prompt_action(client, prompt)
#         return response[0]["generated_text"]

#     def prompt(self, prompt: str):
#         """
#         Return a response to the given prompt. Wraps the _prompt method to allow subclasses
#         to override it and use validation or other logic.
#         """
#         return self._prompt(prompt)


# @dataclass
# class Llama3Request(HuggingfaceRequest):
#     """Represents a request to a local Llama3 model using Hugging Face Transformers."""

#     _ai_provider: GenerativeAIProvider | None = None
#     _max_length: int = 50
#     _temperature: float = 0.7
#     _system_prompt: str = (
#         "You are a helpful AI assistant that helps users with their questions."
#     )
#     _post_user_prompt: str = (
#         "Please provide a response to the user's question in a concise format."
#     )
#     _chat_history: List[Dict[str, str]] | None = None

#     @property
#     def ai_provider(self) -> GenerativeAIProvider:
#         if self._ai_provider is None:
#             from navigator_py.generative_ai_provider import Llama3Provider

#             self._ai_provider = Llama3Provider()
#             self._ai_provider.connect()
#         return self._ai_provider


# @dataclass
# class Phi3MiniRequest(HuggingfaceRequest):
#     """Represents a request to a local Phi3 Mini model using Hugging Face Transformers."""

#     _ai_provider: GenerativeAIProvider | None = None
#     _max_length: int = 50
#     _temperature: float = 0.7
#     _system_prompt: str = (
#         "You are a helpful AI assistant that helps users with their questions."
#     )
#     _post_user_prompt: str = (
#         "Please provide a response to the user's question in a concise format."
#     )
#     _chat_history: List[Dict[str, str]] | None = None

#     @property
#     def ai_provider(self) -> GenerativeAIProvider:
#         if self._ai_provider is None:
#             from navigator_py.generative_ai_provider import Phi3MiniProvider

#             self._ai_provider = Phi3MiniProvider()
#             self._ai_provider.connect()
#         return self._ai_provider
