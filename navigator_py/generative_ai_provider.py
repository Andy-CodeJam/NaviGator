"""Define the interface expected of a generative AI provider and an implementation for Azure OpenAI."""

import os
from dataclasses import dataclass
from typing import Protocol

from dotenv import find_dotenv, load_dotenv
from openai import AzureOpenAI

load_dotenv(find_dotenv())


@dataclass
class GenerativeAIProvider(Protocol):
    """Protocol interface for a generative AI provider. At minimum,
    a provider must have a client property and a connect method to
    establish a connection to the provider."""

    @property
    def client(self) -> AzureOpenAI: ...

    def connect(self): ...


@dataclass
class AzureOpenAIProvider:
    """Provider for Azure OpenAI API."""

    _client: AzureOpenAI | None = None

    def connect(self):
        if os.environ["AZURE_OPENAI_API_KEY"] is None:
            raise ValueError("Azure OpenAI API key is not set")

        if os.environ["AZURE_OPENAI_ENDPOINT"] is None:
            raise ValueError("Azure OpenAI endpoint is not set")

        if os.environ["AZURE_OPENAI_API_VERSION"] is None:
            raise ValueError("Azure OpenAI API version is not set")

        self._client = AzureOpenAI(
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        )

    @property
    def client(self):
        if self._client is None:
            self.connect()
        return self._client
