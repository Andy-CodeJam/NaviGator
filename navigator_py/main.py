from dotenv import find_dotenv, load_dotenv

from navigator_py.flow import (
    ensure_asking_about_spira,
    ensure_single_topic_in_prompt,
    evaluate_articles,
    evaluate_llm_answer,
    generate_llm_answer,
    parse_command_line,
    rephrase_prompt,
    search_for_documents,
)

load_dotenv(find_dotenv())

RETURN_N_DOCS = 3  # Number of documents to return from each source

error_code_map = {
    1: "No prompt was provided, or the prompt was not able to be parsed from the command line.",
    2: "The prompt seemed to be asking about something other than Spira. Unfortunately, I can only answer questions about Spira.",
    3: "There was a data validation error. I cannot proceed unless I get a 'Y' or 'N' response. This is likely a random hallucination, and is why the validation is in place! Please try your query again.",
    4: "My reading of the prompt tells me that the user is not asking about a topic at all. I don't know what this means, so I'm exiting. This could be a bug, but maybe try to reword your query to be a little more clear about what you are looking for.",
    5: "My reading of the prompt tells me that the user is asking about multiple topics. I can only answer one question at a time. I need to exit. Please try asking about a more focused, single topic.",
    6: "I wasn't able to generate a response that answers your question on my first try. I need to rephrase the question and try again. Please try asking your question in a different way.",
    7: "I expected to see either 'Y' or 'N', but got something else. I'm exiting. This is likely a bug, so please try asking your question in a different way, but it could be a hallucination, so you might also try simply resubmitting your query.",
}


def main():
    # Get the prompt from the command line
    prompt, print_verbose = parse_command_line()
    if prompt == 1:
        exit(error_code_map[1])

    # First ensure that we are indeed asking about Spira
    is_asking_about_spira_result = ensure_asking_about_spira(prompt, print_verbose)
    if is_asking_about_spira_result > 0:
        exit(error_code_map[is_asking_about_spira_result])

    # Now we know that the user is asking about Spira (it would have exited otherwise)

    # Check if there is a single question in the prompt,
    # if there are multiple questions, or if there are no questions
    # Only move forward if there is a single question
    # Otherwise respond that we can only answer one question at a time
    is_single_topic_result = ensure_single_topic_in_prompt(prompt, print_verbose)
    if is_single_topic_result > 0:
        exit(error_code_map[is_single_topic_result])

    # Rephrase the prompt and pass to the Azure AI Search
    # Not implemented -- this is just a placeholder that returns the original prompt
    rephrased_prompt = rephrase_prompt(prompt, print_verbose)

    # Azure search will return a list of top 3 relevant articles and return
    # to the LLM
    top_qa_kb, top_docs = search_for_documents(
        rephrased_prompt, print_verbose, top=RETURN_N_DOCS
    )

    # LLM will evaluate the top 3 articles to determine which are most useful for
    # generating a response with citations
    evaluated_articles = evaluate_articles(
        rephrased_prompt, print_verbose, top_qa_kb, top_docs
    )

    # LLM will use the top evaluated articles to generate a response
    generated_llm_answer = generate_llm_answer(
        rephrased_prompt, print_verbose, evaluated_articles
    )

    # LLM will evaluate yes or no whether the original question was answered
    # If no, rephrase and send back to Azure AI Search, but return the
    # top 5 articles
    evaluation_of_llm_answer = evaluate_llm_answer(
        rephrased_prompt, generated_llm_answer, print_verbose
    )
    if evaluation_of_llm_answer > 0:
        exit(error_code_map[evaluation_of_llm_answer])

    with open("answer.md", "w") as f:
        f.write(generated_llm_answer)

    return generated_llm_answer


if __name__ == "__main__":
    main()
