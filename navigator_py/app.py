# streamlit_app.py
import os
import sys

import streamlit as st

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from navigator_py.flow import (  # noqa: E402
    ensure_asking_about_spira,
    ensure_single_topic_in_prompt,
    evaluate_articles,
    evaluate_llm_answer,
    generate_llm_answer,
    rephrase_prompt,
    search_for_documents,
)

RETURN_N_DOCS = 3


def main():
    st.title("Spira Chat")

    # A container for chat messages
    chat_container = st.container()

    # Input form for the user prompt
    with st.form("prompt_form"):
        prompt = st.text_input("Enter your question about Spira:")
        submit_button = st.form_submit_button("Submit")

    # A function to log messages to the chat container
    def print_verbose(message):
        chat_container.write(message)

    if submit_button and prompt:
        # Start processing the prompt
        print_verbose("Processing prompt...")

        # First ensure that we are indeed asking about Spira
        is_asking_about_spira_result = ensure_asking_about_spira(prompt, print_verbose)
        if is_asking_about_spira_result > 0:
            print_verbose(f"Error: {is_asking_about_spira_result}")
            return

        # Now we know that the user is asking about Spira (it would have exited otherwise)
        print_verbose("Prompt is about Spira.")

        # Check if there is a single question in the prompt,
        # if there are multiple questions, or if there are no questions
        # Only move forward if there is a single question
        is_single_topic_result = ensure_single_topic_in_prompt(prompt, print_verbose)
        if is_single_topic_result > 0:
            print_verbose(f"Error: {is_single_topic_result}")
            return

        # Rephrase the prompt and pass to the Azure AI Search
        rephrased_prompt = rephrase_prompt(prompt, print_verbose)

        # Azure search will return a list of top relevant articles
        top_qa_kb, top_docs = search_for_documents(
            rephrased_prompt, print_verbose, top=RETURN_N_DOCS
        )

        # LLM will evaluate the top articles to determine which are most useful for generating a response with citations
        evaluated_articles = evaluate_articles(
            rephrased_prompt, print_verbose, top_qa_kb, top_docs
        )

        # LLM will use the top evaluated articles to generate a response
        generated_llm_answer = generate_llm_answer(
            rephrased_prompt, print_verbose, evaluated_articles
        )

        # LLM will evaluate whether the original question was answered
        evaluation_of_llm_answer = evaluate_llm_answer(
            rephrased_prompt, generated_llm_answer, print_verbose
        )
        if evaluation_of_llm_answer > 0:
            print_verbose(f"Error: {evaluation_of_llm_answer}")
            return

        print_verbose("Generated Answer:")
        print_verbose(generated_llm_answer)

        with open("answer.md", "w") as f:
            f.write(generated_llm_answer)

        print_verbose("Answer saved to answer.md")


if __name__ == "__main__":
    main()
