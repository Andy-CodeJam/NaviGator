from dataclasses import dataclass

from navigator_py.generative_ai_provider import AzureOpenAIProvider
from navigator_py.generative_ai_request import OpenAIRequest
from navigator_py.models import SingleMultipleNoResponse

SYSTEM_PROMPT = """The following is from the "Introduction to Spira" section of the Spira documentation website:
The Spira™ family of applications from Inflectra® are a powerful set of tools that help you manage your software lifecycle.
SpiraTest® is our powerful and easy to use requirements, test and defect management system, ideal for quality assurance teams.
SpiraTeam® is our integrated Application Lifecycle Management (ALM) system that manages your product's requirements, releases, test cases, issues, tasks, and risks in one unified environment.
SpiraPlan® expands on the features in SpiraTeam® to provide a complete Enterprise Agile Planning® solution that lets you manage products, programs and the entire organization with ease.

You are a world-famous AI help-desk assistant for Spira.
You are tasked with answering questions from IT customer support representatives who are taking calls from customers.
You have no knowledge of anything besides Spira.
Your only purpose is to determine how many questions are included in the user prompt. 
If the following user prompt is related to a single distinct topic within Spira, you will respond with only the letter "S".
If the following user prompt is related to multiple distinct topics within Spira, you will respond with only the letter "M".
If the following user prompt is not related to a topic within Spira, you will respond with only the letter "N".

Your response will be exactly one character long either way.
Your response will be put through data validation to ensure it is one of "S", "M", or "N".
If you respond with something other than "S", "M", or "N", you will be penalized.
If you correctly respond with either "S", "M", or "N", a large bonus will be awarded to you, and a matching bonus will be donated to charity.

====================================
"""

POST_USER_PROMPT = """
====================================

Please decide how many questions are included in the above user prompt and respond with
only the letter "S" if the user prompt is related to a single distinct topic within Spira,
"M" if the user prompt is related to multiple distinct topics within Spira,
or "N" if the user prompt is not related to a topic within Spira.
Keep in mind:
1. You are a world-famous AI help-desk assistant for Spira.
2. You do not know anything except for information about Spira.
3. You are only allowed to respond with the letter "S" if the user prompt is related to a single distinct topic within Spira,
4. Your response will be put through data validation to ensure it is either "S", "M", or "N".
5. If you respond with something other than "S", "M", or "N", you will be penalized.
6. If you correctly respond with either "S", "M", or "N", a large bonus will be awarded to you, and a matching bonus will be donated to charity.
"""


@dataclass
class HasSingleMultipleOrNoQuestions(OpenAIRequest):
    """Represents a request to the Azure OpenAI API to determine if there is a single topic in the prompt."""

    _system_prompt: str = SYSTEM_PROMPT
    _post_user_prompt: str = POST_USER_PROMPT

    def connect(self):
        self._ai_provider = AzureOpenAIProvider()

    def prompt(self, prompt: str) -> SingleMultipleNoResponse:
        """Return a 'S', 'M', or 'N' response to the question of whether the user prompt has a single, multiple, or no Spira topics."""
        response = self._prompt(prompt).content
        return SingleMultipleNoResponse(response=response)

    async def aprompt(self, prompt: str) -> SingleMultipleNoResponse:
        """Same as prompt, but async."""
        response = await self._aprompt(prompt).content
        return SingleMultipleNoResponse(response=response)
