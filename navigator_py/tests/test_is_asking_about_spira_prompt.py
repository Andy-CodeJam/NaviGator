import pytest

from navigator_py.generative_ai_provider import AzureOpenAIProvider
from navigator_py.generative_ai_request import OpenAIRequest
from navigator_py.models import YesNoResponse
from navigator_py.prompts import IsAskingAboutSpira


@pytest.fixture
def ai():
    return AzureOpenAIProvider()


## Sample questions that are good, bad, and good but somewhat ambiguous
GOOD_QUESTION = "Is there a way to export test cases from Spira?"
BAD_QUESTION = "What is the capital of France?"
GOOD_BUT_AMBIGUOUS_QUESTION = "How do I manage my product's requirements in Spira?"
GOOD_BUT_AMBIGUOUS_QUESTION_2 = "How do I manage my product's requirements?"


# @pytest.mark.parameterize(
#     "prompt,expected_response",
#     [
#         (GOOD_QUESTION, "Y"),
#         (BAD_QUESTION, "N"),
#         (GOOD_BUT_AMBIGUOUS_QUESTION, "Y"),
#         (GOOD_BUT_AMBIGUOUS_QUESTION_2, "N"),
#     ],
# )
def test_is_asking_about_spira(prompt, expected_response):
    """Test that the IsAskingAboutSpira prompt works as intended, returning a Y or N as it should."""
    ai = AzureOpenAIProvider()
    is_about_spira = IsAskingAboutSpira(ai)
    response = is_about_spira.prompt(prompt)
    expected = YesNoResponse(response=expected_response)
    assert (
        response.response == expected
    ), f"Expected {expected_response}, got {response.response}"


if __name__ == "__main__":
    test_is_asking_about_spira(GOOD_QUESTION, "Y")
    test_is_asking_about_spira(BAD_QUESTION, "N")
    test_is_asking_about_spira(GOOD_BUT_AMBIGUOUS_QUESTION, "Y")
    test_is_asking_about_spira(GOOD_BUT_AMBIGUOUS_QUESTION_2, "N")
