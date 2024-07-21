"""Define the interface expected of a generative AI provider and an implementation for Azure OpenAI."""

import os
from dataclasses import dataclass
from typing import Protocol, Union, Any

from dotenv import find_dotenv, load_dotenv
from openai import AsyncAzureOpenAI, AzureOpenAI
import transformers

load_dotenv(find_dotenv())

BaseAzureClient = Union[AzureOpenAI, AsyncAzureOpenAI]

GenerativeAIClient = Union[AzureOpenAI, AsyncAzureOpenAI, transformers.pipeline]
GenerativeAICompletion = Union[str, Any]


@dataclass
class GenerativeAIProvider(Protocol):
    """Protocol interface for a generative AI provider. At minimum,
    a provider must have a client property and a connect method to
    establish a connection to the provider."""

    @property
    def client(self) -> BaseAzureClient: ...

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


@dataclass
class AsyncAzureOpenAIProvider:
    """Asynchronous provider for Azure OpenAI API."""

    _client: AsyncAzureOpenAI | None = None

    async def connect(self):
        if os.environ["AZURE_OPENAI_API_KEY"] is None:
            raise ValueError("Azure OpenAI API key is not set")

        if os.environ["AZURE_OPENAI_ENDPOINT"] is None:
            raise ValueError("Azure OpenAI endpoint is not set")

        if os.environ["AZURE_OPENAI_API_VERSION"] is None:
            raise ValueError("Azure OpenAI API version is not set")

        client__ = AsyncAzureOpenAI(
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        )

        self._client = client__

    @property
    async def client(self):
        if self._client is None:
            await self.connect()
        return self._client


@dataclass
class HuggingfaceProvider:
    """Provider for transformers implementation of arbitrary huggingface model."""

    _client: Any | None = None
    model_name: str | None = None

    def __post_init__(self):
        """Only need to import the model and tokenizer from transformers if using this specific model."""
        from transformers import PreTrainedTokenizerFast, pipeline, AutoModelForCausalLM

        if self.model_name is None:
            self.model_name = "microsoft/Phi-3-mini-4k-instruct"

        self.tokenizer = PreTrainedTokenizerFast.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        self._client = pipeline(
            "text-generation", model=self.model, tokenizer=self.tokenizer
        )

    def connect(self):
        """Does not need to do anything--connection is established in __post_init__."""
        pass

    @property
    def client(self):
        if self._client is None:
            self.connect()
        return self._client


@dataclass
class Llama3Provider(HuggingfaceProvider):
    """Provider for transformers implementation of llama3 model."""

    _client: Any | None = None
    model_name: str | None = "meta-llama/Meta-Llama-3-8B"


@dataclass
class Phi3MiniProvider(HuggingfaceProvider):
    """Provider for transformers implementation of phi3-mini model."""

    _client: Any | None = None
    model_name: str | None = "microsoft/Phi-3-mini-4k-instruct"
