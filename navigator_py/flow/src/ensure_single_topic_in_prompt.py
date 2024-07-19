from typing import Callable

from navigator_py.prompts import HasSingleMultipleOrNoQuestions


def ensure_single_topic_in_prompt(prompt: str, print_verbose: Callable) -> int:
    print_verbose(
        "Is the user asking about a single topic, multiple topics, or no topics?"
    )
    has_single_multiple_or_no_questions = HasSingleMultipleOrNoQuestions()
    response = has_single_multiple_or_no_questions.prompt(prompt).response
    print_verbose(f"{response}")

    if response == "N":
        print_verbose(
            "The user is not asking about a topic at all. I don't know what this means, so I'm exiting."
        )
        return 4
    elif response == "M":
        print_verbose(
            "The user is asking about multiple topics. I can only answer one question at a time. I need to exit."
        )
        return 5
    else:
        print_verbose("The user is asking about a single topic. I can proceed.")
        return 0
