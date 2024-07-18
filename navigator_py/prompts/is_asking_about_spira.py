from dataclasses import dataclass

from navigator_py.generative_ai_provider import AzureOpenAIProvider
from navigator_py.generative_ai_request import OpenAIRequest
from navigator_py.models import YesNoResponse

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


@dataclass
class IsAskingAboutSpira(OpenAIRequest):
    """Represents a request to the Azure OpenAI API to determine if the user is asking about Spira."""

    _system_prompt: str = SYSTEM_PROMPT
    _post_user_prompt: str = POST_USER_PROMPT

    def connect(self):
        self._ai_provider = AzureOpenAIProvider()

    def prompt(self, prompt: str) -> YesNoResponse:
        """Return a 'Y' or 'N' response to the question of whether the user is asking about Spira in their prompt."""
        response = self._prompt(prompt).content
        return YesNoResponse(response=response)

    async def aprompt(self, prompt: str) -> YesNoResponse:
        """Same as prompt, but async."""
        response = await self._aprompt(prompt).content
        return YesNoResponse(response=response)
