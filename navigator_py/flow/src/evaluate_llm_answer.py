from typing import Callable
from navigator_py.prompts import EvaluateWhetherOrNotQuestionHasBeenAnswered

def evaluate_llm_answer(prompt:str, generated_llm_answer: str, print_verbose: Callable) -> int:
    print_verbose("I need to evaluate whether or not the question was answered?")
    eval_whether_or_not_question_has_been_answered = (
        EvaluateWhetherOrNotQuestionHasBeenAnswered(draft_response=generated_llm_answer)
    )
    response = eval_whether_or_not_question_has_been_answered.prompt(
        prompt
    ).response

    print_verbose(response)
    if response == "N":
        print_verbose(
            "The question was not answered. I need to rephrase the question and try again."
        )
        return 6
    elif response != "Y":
        print_verbose(
            f"I expected to see either 'Y' or 'N', but got {response}. I'm exiting."
        )
        return 7
    else:
        # If yes, write a response
        print_verbose(
            "The question was answered by the proposed draft response. I will return the response to the user."
        )
        return 0
