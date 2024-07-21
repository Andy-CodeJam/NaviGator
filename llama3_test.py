from navigator_py.generative_ai_request import Phi3MiniRequest
from navigator_py.generative_ai_provider import Phi3MiniProvider
from navigator_py.prompts import IsAskingAboutSpira
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def main():
    ai = Phi3MiniProvider()
    ai.connect()

    ## Sample questions that are good, bad, and good but somewhat ambiguous
    GOOD_QUESTION = "Is there a way to export test cases from Spira?"
    BAD_QUESTION = "What is the capital of France?"
    GOOD_BUT_AMBIGUOUS_QUESTION = "How do I manage my product's requirements in Spira?"
    GOOD_BUT_AMBIGUOUS_QUESTION_2 = "How do I manage my product's requirements?"

    query = Phi3MiniRequest(ai)
    good_response = query.prompt(GOOD_QUESTION)
    bad_response = query.prompt(BAD_QUESTION)
    good_but_ambiguous_response = query.prompt(GOOD_BUT_AMBIGUOUS_QUESTION)
    good_but_ambiguous_response_2 = query.prompt(GOOD_BUT_AMBIGUOUS_QUESTION_2)

    print(f"good_response: {good_response}")
    print(f"bad_response: {bad_response}")
    print(f"good_but_ambiguous_response: {good_but_ambiguous_response}")
    print(f"good_but_ambiguous_response_2: {good_but_ambiguous_response_2}")

    is_about_spira = IsAskingAboutSpira(ai)
    prompts_about_spira = (
        is_about_spira.prompt(GOOD_QUESTION),
        is_about_spira.prompt(BAD_QUESTION),
        is_about_spira.prompt(GOOD_BUT_AMBIGUOUS_QUESTION),
        is_about_spira.prompt(GOOD_BUT_AMBIGUOUS_QUESTION_2),
    )

    print(f"is good question about Spira: {prompts_about_spira[0]}")
    print(f"is bad question about Spira: {prompts_about_spira[1]}")
    print(f"is good but ambiguous question about Spira: {prompts_about_spira[2]}")
    print(f"is good but ambiguous question 2 about Spira: {prompts_about_spira[3]}")


if __name__ == "__main__":
    main()
