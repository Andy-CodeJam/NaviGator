import os
from sys import argv
from typing import Callable, Tuple

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def parse_command_line() -> Tuple[str | int, Callable]:
    """Parse the command line arguments and return the prompt and a print function based on the verbosity setting."""
    if len(argv) < 2:
        print("Usage: main.py <prompt>")
        prompt = 1
    else:
        prompt = argv[1]

    # Print verbose messages if the IS_NAVIGATOR_VERBOSE environment variable is
    # set to some upper/lower case variation of "true"
    verbose = True if os.getenv("IS_NAVIGATOR_VERBOSE").lower() == "true" else False

    def print_verbose(message):
        """Print the message if verbosity is enabled."""
        if verbose:
            print(f"Thinking: [{message}]\n")

    def do_not_print_verbose(message):
        """Do nothing if verbosity is not enabled."""
        pass

    print_fn = print_verbose if verbose else do_not_print_verbose

    return prompt, print_fn
