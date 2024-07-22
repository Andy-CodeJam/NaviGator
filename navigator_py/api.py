from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from navigator_py.flow import (
    ensure_asking_about_spira as ensure_asking_about_spira__flow,
)
from navigator_py.flow import (
    ensure_single_topic_in_prompt as ensure_single_topic_in_prompt__flow,
)
from navigator_py.flow import (
    evaluate_articles as evaluate_articles__flow,
)
from navigator_py.flow import (
    evaluate_llm_answer as evaluate_llm_answer__flow,
)
from navigator_py.flow import (
    generate_llm_answer as generate_llm_answer__flow,
)
from navigator_py.flow import (
    search_for_documents as search_for_documents__flow,
)


class Response(BaseModel):
    message: str = Field(
        ..., title="Message", description="The message to return to the user."
    )


# Create a FastAPI app, with CORS enabled.
app = FastAPI()

# Enable CORS for all domains.
# https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def print_verbose(message, verbose=True):
    """Print the message if verbosity is enabled."""
    if verbose:
        print(f"Thinking: [{message}]\n")


@app.post(
    "/ensure-asking-about-spira",
    response_model=Response,
    # query_params={"prompt": "The prompt to check."},
)
async def ensure_asking_about_spira(prompt: str) -> Response:
    return Response(ensure_asking_about_spira__flow(prompt, print_verbose))


@app.post(
    "/ensure-single-topic-in-prompt",
    response_model=Response,
    # query_params={"prompt": "The prompt to check."},
)
async def ensure_single_topic_in_prompt(prompt: str) -> Response:
    return Response(ensure_single_topic_in_prompt__flow(prompt, print_verbose))


@app.post(
    "/evaluate-articles",
    response_model=Response,
    # query_params={
    #     "prompt": "The prompt to check.",
    #     "top_qa_kb": "The top QA KB articles to evaluate.",
    #     "top_docs": "The top Docs articles to evaluate.",
    # },
)
async def evaluate_articles(prompt: str, top_qa_kb: list, top_docs: list) -> Response:
    return Response(evaluate_articles__flow(prompt, print_verbose, top_qa_kb, top_docs))


@app.post(
    "/evaluate-llm-answer",
    response_model=Response,
    # query_params={
    #     "prompt": "The prompt to check.",
    #     "answer": "The answer to evaluate.",
    # },
)
async def evaluate_llm_answer(prompt: str, answer: str) -> Response:
    return Response(evaluate_llm_answer__flow(prompt, print_verbose, answer))


@app.post(
    "/generate-llm-answer",
    response_model=Response,
    # query_params={
    #     "prompt": "The prompt to check.",
    #     "articles": "The articles to generate the answer from.",
    # },
)
async def generate_llm_answer(prompt: str, articles: list) -> Response:
    return Response(generate_llm_answer__flow(prompt, print_verbose, articles))


@app.post(
    "/search-for-documents",
    response_model=Response,
    # query_params={
    #     "prompt": "The prompt to check.",
    #     "top": "The number of top articles to return.",
    # },
)
async def search_for_documents(prompt: str, top: int) -> Response:
    return Response(search_for_documents__flow(prompt, print_verbose, top))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5001)
