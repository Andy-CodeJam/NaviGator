"""Define the Azure AI Search request."""

import json
import os
from dataclasses import dataclass
from typing import Dict, List

try:
    from search_provider import AzureAiSearchProvider, SearchProvider
except ModuleNotFoundError:
    from navigator_py.search.search_provider import (
        AzureAiSearchProvider,
        SearchProvider,
    )


@dataclass
class AzureAiSearchRequest:
    """Request model for Azure AI Search."""

    _query: str | None = None
    _search_provider: SearchProvider | None = None
    _top: int = 10
    _query_type: str = "semantic"

    @property
    def search_provider(self) -> SearchProvider:
        if self._search_provider is None:
            self._search_provider = AzureAiSearchProvider()
        return self._search_provider

    @property
    def query(self) -> str:
        if self._query is None:
            raise ValueError("Query is not set")
        return self._query

    @property
    def query_type(self) -> str:
        return self._query_type

    @property
    def top(self) -> int:
        return self._top

    def search(self) -> List[Dict[str, str]]:
        response = list(
            self.search_provider.client.search(
                search_text=self.query,
                query_type=self.query_type,
                semantic_configuration_name=self.search_provider.semantic_configuration_name,
                top=self.top,
            )
        )

        content = []
        for r in response:
            content.append(json.loads(r["content"]))

        return content


@dataclass
class SpiraQASearch(AzureAiSearchRequest):
    """Request model for Spira QA Search."""

    _query: str | None = None
    _search_provider: SearchProvider | None = AzureAiSearchProvider(
        _index_name="spira-qa-index3",
        _semantic_configuration_name="default",
        _endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
        _api_key=os.getenv("AZURE_SEARCH_API_KEY"),
    )
    _top: int = 10
    _query_type: str = "semantic"

    def search(self) -> List[Dict[str, str]]:
        result = list(
            self.search_provider.client.search(
                search_text=self.query,
                query_type=self.query_type,
                semantic_configuration_name=self.search_provider.semantic_configuration_name,
                top=self.top,
            )
        )

        content = []
        for r in result:
            content.append({k: v for k, v in r["content"].items() if k not in ["id"]})

            for k, v in r["content"].items():
                if k not in ["id", "content"]:
                    content[-1][k] = v

        return content


@dataclass
class SpiraDocsSearch(AzureAiSearchRequest):
    """Request model for Spira Docs Search."""

    _query: str | None = None
    _search_provider: SearchProvider | None = AzureAiSearchProvider(
        _index_name="spira-docs-index2",
        _semantic_configuration_name="default",
        _endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
        _api_key=os.getenv("AZURE_SEARCH_API_KEY"),
    )
    _top: int = 10
    _query_type: str = "semantic"

    def search(self) -> List[Dict[str, str]]:
        result = list(
            self.search_provider.client.search(
                search_text=self.query,
                query_type=self.query_type,
                semantic_configuration_name=self.search_provider.semantic_configuration_name,
                top=self.top,
            )
        )

        content = []
        for r in result:
            content.append({k: v for k, v in r["content"].items() if k not in ["id"]})
            for k, v in r["content"].items():
                if k not in ["id", "content"]:
                    content[-1][k] = v

        return content
