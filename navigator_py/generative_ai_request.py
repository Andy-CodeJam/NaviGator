import os
from dataclasses import dataclass
from typing import Protocol

import openai
from dotenv import find_dotenv, load_dotenv

from navigator_py.generative_ai_provider import (
    AzureOpenAIProvider,
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
class OpenAIRequest:
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

    @property
    def ai_provider(self) -> GenerativeAIProvider:
        if self._ai_provider is None:
            self._ai_provider = AzureOpenAIProvider()
        return self._ai_provider

    @property
    def max_tokens(self) -> int:
        """Return the maximum number of tokens to generate."""
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, value: int):
        self._max_tokens = value

    @property
    def temperature(self):
        """Return the temperature to use for generating completions."""
        return self._temperature

    @temperature.setter
    def temperature(self, value: float):
        self._temperature = value

    @property
    def system_prompt(self):
        return self._system_prompt

    @system_prompt.setter
    def system_prompt(self, value: str):
        self._system_prompt = value

    @property
    def post_user_prompt(self):
        return self._post_user_prompt

    @post_user_prompt.setter
    def post_user_prompt(self, value: str):
        self._post_user_prompt = value

    @property
    def chat_history(self):
        return self._chat_history

    def connect(self):
        self._ai_provider.client.connect()

    def prompt(
        self,
        prompt: str,
        max_tokens: int | None = None,
        temperature: float | None = None,
    ):
        if max_tokens is None:
            max_tokens = self._max_tokens

        if temperature is None:
            temperature = self._temperature

        client = self._ai_provider._client

        try:
            response = client.chat.completions.create(
                model=os.getenv("OPENAI_COMPLETIONS_MODEL"),
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt},
                    {"role": "system", "content": self.post_user_prompt},
                ],
            )

            return response.choices[0].message

        except openai.AuthenticationError as e:
            # Handle Authentication error here, e.g. invalid API key

            print(f"OpenAI API returned an Authentication Error: {e}")

        except openai.APIConnectionError as e:
            # Handle connection error here

            print(f"Failed to connect to OpenAI API: {e}")

        except openai.BadRequestError as e:
            # Handle connection error here

            print(f"Invalid Request Error: {e}")

        except openai.RateLimitError as e:
            # Handle rate limit error

            print(f"OpenAI API request exceeded rate limit: {e}")

        except openai.InternalServerError as e:
            # Handle Service Unavailable error

            print(f"Service Unavailable: {e}")

        except openai.APITimeoutError as e:
            # Handle request timeout

            print(f"Request timed out: {e}")

        except openai.APIError as e:
            # Handle API error here, e.g. retry or log

            print(f"OpenAI API returned an API Error: {e}")

        except Exception as e:
            # Handles all other exceptions

            print(f"An exception has occured: {e}")
