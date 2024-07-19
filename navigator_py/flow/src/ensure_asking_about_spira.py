from typing import Callable

from navigator_py.prompts import IsAskingAboutSpira


def ensure_asking_about_spira(prompt: str, print_verbose: Callable) -> int:
    """Ensure that the user is asking about Spira. Return an integer code based on the outcome."""
    print_verbose("Is the user asking about Spira?")
    is_asking_about_spira = IsAskingAboutSpira()
    response = is_asking_about_spira.prompt(prompt).response
    print_verbose(f"{response}")

    if response == "N":
        print_verbose(
            "The user is asking about something else, and I can only answer questions about Spira."
        )
        return 2
    elif response != "Y":
        print_verbose(
            f"I expected the response to be 'Y' or 'N', but actually got {response}. This doesn't make any sense and I'm exiting."
        )
        return 3

    return 0
