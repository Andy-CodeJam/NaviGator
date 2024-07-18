import os
from sys import argv

from dotenv import find_dotenv, load_dotenv

from navigator_py.prompts import (
    EvaluateWhetherOrNotQuestionHasBeenAnswered,
    HasSingleMultipleOrNoQuestions,
    IsAskingAboutSpira,
    UseArticlesToGenerateAnswer,
)

load_dotenv(find_dotenv())


def get_sample_data():
    import joblib

    return joblib.load("sample_data")


def main():
    # Get the prompt from the
    if len(argv) < 2:
        print("Usage: main.py <prompt>")
        exit(1)
    prompt = argv[1]
    verbose = True if os.getenv("IS_NAVIGATOR_VERBOSE").lower() == "true" else False

    def print_verbose(message):
        if verbose:
            print(f"Thinking: [{message}]\n=====================\n")

    # First ensure that we are indeed asking about Spira
    print_verbose("Is the user asking about Spira?")
    is_asking_about_spira = IsAskingAboutSpira()
    response = is_asking_about_spira.prompt(prompt).response
    print_verbose(f"{response}")

    if response == "N":
        print_verbose(
            "The user is asking about something else, and I can only answer questions about Spira."
        )
        exit(2)
    elif response != "Y":
        print_verbose(
            f"I expected the response to be 'Y' or 'N', but actually got {response}. This doesn't make any sense and I'm exiting."
        )
        exit(3)

    # Now we know that the user is asking about Spira

    # Check if there is a single question in the prompt,
    # if there are multiple questions, or if there are no questions
    # Only move forward if there is a single question
    # Otherwise respond that we can only answer one question at a time
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
        exit(4)
    elif response == "M":
        print_verbose(
            "The user is asking about multiple topics. I can only answer one question at a time. I need to exit."
        )
        exit(5)

    # Rephrase the prompt and pass to the Azure AI Search

    # Azure search will return a list of top 3 relevant articles and return
    # to the LLM
    top_3_articles = get_sample_data()  # This is a placeholder for the Azure AI Search

    # LLM will use the top 3 articles to generate a response
    print_verbose("I have the top 3 articles.")
    print_verbose("I will use them to generate a response to the user's query.")

    generate_answer_with_response = UseArticlesToGenerateAnswer(articles=top_3_articles)
    generated_llm_answer = generate_answer_with_response.prompt(prompt)

    print_verbose("I have generated a response.")
    print_verbose("Here is my response:\n\n")
    print_verbose(generated_llm_answer)

    # LLM will evaluate yes or no whether the original question was answered
    # If no, rephrase and send back to Azure AI Search, but return the
    # top 5 articles
    print_verbose("I need to evaluate whether or not the question was answered?")
    eval_whether_or_not_question_has_been_answered = (
        EvaluateWhetherOrNotQuestionHasBeenAnswered(draft_response=generated_llm_answer)
    )
    response = eval_whether_or_not_question_has_been_answered.prompt(prompt).response

    print_verbose(response)
    if response == "N":
        print_verbose(
            "The question was not answered. I need to rephrase the question and try again."
        )
        exit(6)
    elif response != "Y":
        print_verbose(
            f"I expected to see either 'Y' or 'N', but got {response}. I'm exiting."
        )
        exit(7)

    # If yes, write a response
    print_verbose(
        "The question was answered by the proposed draft response. I will return the response to the user."
    )

    # Return the response to the user
    print(generated_llm_answer)


if __name__ == "__main__":
    main()
