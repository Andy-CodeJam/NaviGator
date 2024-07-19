from typing import Callable, Dict, List

from navigator_py.search import SpiraDocsSearch, SpiraQASearch


def get_top_qa_kb_articles(query: str, top: int = 3) -> List[Dict[str, str]]:
    """Get the top 5 articles from the QA KB based on the query."""
    search = SpiraQASearch(_query=query, _top=top)
    return search.search()


def get_top_docs_articles(query: str, top: int = 3) -> List[Dict[str, str]]:
    """Get the top 5 articles from the Docs based on the query."""
    search = SpiraDocsSearch(_query=query, _top=top)
    return search.search()


def search_for_documents(prompt: str, print_verbose: Callable, top: int = 3) -> None:
    """Search for the top articles in the QA KB and Docs based on the prompt."""
    top_qa_kb = get_top_qa_kb_articles(prompt, top)
    top_docs = get_top_docs_articles(prompt, top)

    print_verbose(
        "I have the top articles from the original knowledge base and from the Spira documentation, as returned by Azure AI search."
    )
    print_verbose(
        "I will check each one individually to decide whether or not it is likely to be among the top 3 most useful articles for the user prompt."
    )
    print_verbose(
        "This will make it easier to generate a response to the user's query."
    )

    return top_qa_kb, top_docs
