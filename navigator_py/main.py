from sys import argv

from navigator_py.prompts import BasicSpiraPrompt, IsAskingAboutSpira


def main():
    # Get the prompt from the
    if len(argv) < 2:
        print("Usage: main.py <prompt>")
        exit(1)
    prompt = argv[1]

    # First ensure that we are indeed asking about Spira
    is_asking_about_spira = IsAskingAboutSpira()
    response = is_asking_about_spira.prompt(prompt).response

    if response == "N":
        print("I'm sorry, I can only answer questions about Spira.")
        exit(1)
    elif response != "Y":
        print("I'm sorry, I didn't understand your question.")
        exit(1)

    # Now we know that the user is asking about Spira

    # Check if there is a single question in the prompt,
    # if there are multiple questions, or if there are no questions
    # Only move forward if there is a single question
    # Otherwise respond that we can only answer one question at a time

    # Rephrase the prompt and pass to the Azure AI Search

    # Azure search will return a list of top 3 relevant articles and return
    # to the LLM

    # LLM will use the top 3 articles to generate a response

    # LLM will evaluate yes or no whether the original question was answered
    # If no, rephrase and send back to Azure AI Search, but return the
    # top 5 articles

    # If yes, write a response

    # Return the response to the user

    # Now that we know we are asking about Spira, we can proceed with the request
    ## sample request:
    req = BasicSpiraPrompt()
    response = req.prompt(prompt)
    print(response)


if __name__ == "__main__":
    main()
