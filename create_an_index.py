import os

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    ComplexField,
    SearchableField,
    SearchFieldDataType,
    SearchIndex,
    SimpleField,
)
from dotenv import find_dotenv, load_dotenv

from document import get_documents

load_dotenv(find_dotenv())

SEARCH_ENDPOINT = os.getenv("SEARCH_ENDPOINT")
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")
credential = AzureKeyCredential(SEARCH_API_KEY)


# Create a search schema
def create_search_schema():
    index_client = SearchIndexClient(endpoint=SEARCH_ENDPOINT, credential=credential)

    fields = [
        SimpleField(name="qa_id", type=SearchFieldDataType.String, key=True),
        SearchableField(
            name="question",
            type=SearchFieldDataType.String,
            analyzer_name="en.lucene",
            sortable=True,
        ),
        SearchableField(
            name="answer", type=SearchFieldDataType.String, analyzer_name="en.lucene"
        ),
    ]

    scoring_profiles = []
    suggester = [
        # {"name": "sg", "source_fields": ["Tags", "Address/City", "Address/Country"]}
    ]

    # Create the search index=
    index = SearchIndex(
        name=INDEX_NAME,
        fields=fields,
        suggesters=suggester,
        scoring_profiles=scoring_profiles,
    )
    result = index_client.create_or_update_index(index)
    print(f" {result.name} created")
