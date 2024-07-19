from typing import Callable, Dict, List

from navigator_py.models import YesNoResponse
from navigator_py.prompts import EvaluateWhetherOrNotAnArticleIsLikelyToBeUseful


def evaluate_articles(
    prompt: str,
    print_verbose: Callable,
    top_qa_kb: List[Dict[str, str]],
    top_docs: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    evaluated_qa_articles = []
    evaluated_docs_articles = []

    def eval_article(doc: Dict[str, str]) -> YesNoResponse:
        evaluation = EvaluateWhetherOrNotAnArticleIsLikelyToBeUseful(article=doc)
        output = evaluation.prompt(prompt)
        # output = await evaluation.aprompt(prompt)
        return YesNoResponse(response=output.response)

    for i, doc in enumerate(top_qa_kb):
        print_verbose(f"Checking QA KB article {i + 1} for usefulness.")
        # evaluated = asyncio.run(eval_article(doc))
        evaluated = eval_article(doc)
        if evaluated.response == "Y":
            print_verbose(
                f"QA KB article {i + 1} is likely to be useful, so I will keep it:\n\n{doc}\n\n"
            )
            evaluated_qa_articles.append(doc)
        else:
            print_verbose(
                f"QA KB article {i + 1} is not likely to be useful, so I will discard it:\n\n{doc}\n\n"
            )

    for i, doc in enumerate(top_docs):
        print_verbose(f"Checking Docs article {i + 1} for usefulness.")
        # evaluated = asyncio.run(eval_article(doc))
        evaluated = eval_article(doc)
        if evaluated.response == "Y":
            print_verbose(
                f"Docs article {i + 1} is likely to be useful, so I will keep it:\n\n{doc}\n\n"
            )
            evaluated_docs_articles.append(doc)
        else:
            print_verbose(
                f"Docs article {i + 1} is not likely to be useful, so I will discard it:\n\n{doc}\n\n"
            )

    print_verbose("I have evaluated all the articles.")
    print_verbose(
        f"I started with {len(top_qa_kb)} QA KB articles and now have {len(evaluated_qa_articles)} useful ones."
    )
    print_verbose(
        f"I started with {len(top_docs)} Docs articles and now have {len(evaluated_docs_articles)} useful ones."
    )

    return evaluated_qa_articles + evaluated_docs_articles
