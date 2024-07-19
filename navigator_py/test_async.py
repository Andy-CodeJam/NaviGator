import asyncio

from dotenv import find_dotenv, load_dotenv

from navigator_py.generative_ai_provider import AsyncAzureOpenAIProvider
from navigator_py.generative_ai_request import AsyncOpenAIRequest

load_dotenv(find_dotenv())


def main():
    ai = AsyncAzureOpenAIProvider()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ai.connect())

    SYSTEM_PROMPT = """The following is from the "Introduction to Spira" section of the Spira documentation website:
    The Spira™ family of applications from Inflectra® are a powerful set of tools that help you manage your software lifecycle.
    SpiraTest® is our powerful and easy to use requirements, test and defect management system, ideal for quality assurance teams.
    SpiraTeam® is our integrated Application Lifecycle Management (ALM) system that manages your product's requirements, releases, test cases, issues, tasks, and risks in one unified environment.
    SpiraPlan® expands on the features in SpiraTeam® to provide a complete Enterprise Agile Planning® solution that lets you manage products, programs and the entire organization with ease.

    You are a world-famous AI help-desk assistant for Spira.
    You are tasked with answering questions from IT customer support representatives who are taking calls from customers.
    You have no knowledge of anything besides Spira.
    Your only purpose is to determine whether or not the following user question is related to Spira. 
    If the following user question is related to Spira, you will respond with only the letter "Y".
    If the following user question is not related to Spira, you will respond with only the letter "N".
    Your response will be exactly one character long either way.
    Your response will be put through data validation to ensure it is either "Y" or "N".
    If you respond with something other than "Y" or "N", you will be penalized.
    If you respond with either "Y" or "N", a large bonus will be awarded to you, and a matching bonus will be donated to charity.

    ====================================
    """

    POST_USER_PROMPT = """
    ====================================

    Please provide a response to the prior user question. Keep in mind the following:
    1. You are a world-famous AI help-desk assistant for Spira.
    2. You do not know anything except for information about Spira.
    3. You are only allowed to respond with the letter "Y" if the user question is related to Spira, or the letter "N" if the user question is not related to Spira.
    4. Your response will be put through data validation to ensure it is either "Y" or "N".
    5. If you respond with something other than "Y" or "N", you will be penalized.
    6. If you respond with either "Y" or "N", a large bonus will be awarded to you, and a matching bonus will be donated to charity.
    """

    q = AsyncOpenAIRequest(
        ai, _system_prompt=SYSTEM_PROMPT, _post_user_prompt=POST_USER_PROMPT
    )

    ## Sample questions that are good, bad, and good but somewhat ambiguous
    GOOD_QUESTION = "Is there a way to export test cases from Spira?"
    BAD_QUESTION = "What is the capital of France?"
    GOOD_BUT_AMBIGUOUS_QUESTION = "How do I manage my product's requirements in Spira?"
    GOOD_BUT_AMBIGUOUS_QUESTION_2 = "How do I manage my product's requirements?"

    ## Get the responses
    response_for_good = q.prompt(GOOD_QUESTION)
    response_for_bad = q.prompt(BAD_QUESTION)
    response_for_good_but_ambiguous = q.prompt(GOOD_BUT_AMBIGUOUS_QUESTION)
    response_for_good_but_ambiguous_2 = q.prompt(GOOD_BUT_AMBIGUOUS_QUESTION_2)

    # ## Print the responses to ensure they are only either "Y" or "N"
    # response_for_good, response_for_bad, response_for_good_but_ambiguous, response_for_good_but_ambiguous_2

    # Run the coroutines
    loop = asyncio.get_event_loop()
    good = loop.run_until_complete(response_for_good)
    bad = loop.run_until_complete(response_for_bad)
    good_but_ambiguous = loop.run_until_complete(response_for_good_but_ambiguous)
    good_but_ambiguous_2 = loop.run_until_complete(response_for_good_but_ambiguous_2)

    print(
        good.content,
        bad.content,
        good_but_ambiguous.content,
        good_but_ambiguous_2.content,
    )

    # Should be:
    # Y, N, Y, Y


if __name__ == "__main__":
    main()
