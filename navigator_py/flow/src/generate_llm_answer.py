from typing import Callable, Dict, List

from navigator_py.prompts import UseArticlesToGenerateAnswer


def generate_llm_answer(
    prompt: str, print_verbose: Callable, articles: List[Dict[str, str]]
) -> str:
    print_verbose(
        "Now that I have useful articles, I will use them to generate a response to the user's query."
    )

    generate_answer_with_response = UseArticlesToGenerateAnswer(articles=articles)
    generated_llm_answer = generate_answer_with_response.prompt(prompt)

    print_verbose("I have generated a response.")
    print_verbose("Here is my response:")
    print_verbose(generated_llm_answer)

    return generated_llm_answer
