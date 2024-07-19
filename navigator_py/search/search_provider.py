"""Define the interface expected of a search provider and an implementation for Azure AI Search."""

import json
import os
from dataclasses import dataclass
from typing import Protocol

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


@dataclass
class SearchProvider(Protocol):
    """Generic protocol interface for a search provider. At minimum,
    a provider must have a client property returning a searching client."""

    @property
    def client(self) -> SearchClient: ...


@dataclass
class AzureAiSearchProvider(SearchProvider):
    """Provider for Azure Cognitive Search based on the SearchProvider protocol."""

    _index_name: str | None = None
    _semantic_configuration_name: str | None = None
    _endpoint: str | None = None
    _api_key: str | None = None

    @property
    def endpoint(self) -> str:
        """Return the Azure Cognitive Search endpoint. Use the AZURE_SEARCH_ENDPOINT environment variable if the _endpoint attribute is not set."""
        if self._endpoint is None:
            self._endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        return self._endpoint

    @property
    def api_key(self) -> str:
        """Return the Azure Cognitive Search API key. Use the AZURE_SEARCH_API_KEY environment variable if the _api_key attribute is not set."""
        if self._api_key is None:
            self._api_key = os.getenv("AZURE_SEARCH_API_KEY")
        return self._api_key

    @property
    def index_name(self) -> str:
        """Return the Azure Cognitive Search index name. Use the AZURE_SEARCH_INDEX_NAME environment variable if the _index_name attribute is not set."""
        if self._index_name is None:
            self._index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
        return self._index_name

    @property
    def semantic_configuration_name(self) -> str:
        """Return the Azure Cognitive Search semantic configuration name. Use the AZURE_SEARCH_SEMANTIC_CONFIGURATION_NAME environment variable if the _semantic_configuration_name attribute is not set."""
        if self._semantic_configuration_name is None:
            self._semantic_configuration_name = os.getenv(
                "AZURE_SEARCH_SEMANTIC_CONFIGURATION_NAME"
            )
        return self._semantic_configuration_name

    @property
    def client(self) -> SearchClient:
        return SearchClient(
            endpoint=self.endpoint,
            index_name=self.index_name,
            credential=AzureKeyCredential(self.api_key),
        )

    
