from typing import Callable


def rephrase_prompt(prompt: str, print_verbose: Callable) -> str:
    """Rephrase the prompt to make it more understandable to the language model and AI search."""
    print_verbose(
        "Someday I will rephrase the prompt and pass it to Azure AI Search, but for now I will just return the original prompt."
    )
    print_verbose(f"Original prompt: {prompt}")
    rephrased_prompt = prompt
    print_verbose(f"Rephrased prompt: {rephrased_prompt}")

    return rephrased_prompt
