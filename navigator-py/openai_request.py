import os
from dataclasses import dataclass

import openai
from dotenv import find_dotenv, load_dotenv
from openai import AzureOpenAI

from navigator.azure_oai_provider import AzureOpenAIProvider

load_dotenv(find_dotenv())


@dataclass
class OpenAIRequest:
    """Represents a request to the Azure OpenAI API."""

    _ai_provider: AzureOpenAIProvider | None = None
    _max_tokens: int = int(os.getenv("OPENAI_MAX_TOKENS", 60))
    _temperature: float = float(os.getenv("OPENAI_TEMPERATURE", 0.1))
    _system_prompt: str = (
        "You are a helpful AI assistant that helps users with their questions."
    )

    @property
    def system_prompt(self):
        return self._system_prompt

    @system_prompt.setter
    def system_prompt(self, value: str):
        self._system_prompt = value

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
                ],
            )

            return response.choices[0].message.content
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
