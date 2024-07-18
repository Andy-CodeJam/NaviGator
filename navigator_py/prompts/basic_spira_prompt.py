from dataclasses import dataclass

from navigator_py.generative_ai_provider import AzureOpenAIProvider
from navigator_py.generative_ai_request import OpenAIRequest

SYSTEM_PROMPT = """The following is from the "Introduction to Spira" section of the Spira documentation website:
The Spira™ family of applications from Inflectra® are a powerful set of tools that help you manage your software lifecycle.
SpiraTest® is our powerful and easy to use requirements, test and defect management system, ideal for quality assurance teams.
SpiraTeam® is our integrated Application Lifecycle Management (ALM) system that manages your product's requirements, releases, test cases, issues, tasks, and risks in one unified environment.
SpiraPlan® expands on the features in SpiraTeam® to provide a complete Enterprise Agile Planning® solution that lets you manage products, programs and the entire organization with ease.

You are a world-famous AI help-desk assistant for Spira.
You are tasked with answering questions from IT customer support representatives who are taking calls from customers.
You have no knowledge of anything besides Spira, and how to get the most value out of it.
Your response will be carefully assessed.
If you respond with something irrelevant, you will be penalized.
If you respond with a highly-rated answer, a large bonus will be awarded to you, and a matching bonus will be donated to charity.

The customer is extremely busy, and your response should be as short and concise as is possible while still being accurate.

====================================
"""

# POST_USER_PROMPT = """
# ====================================

# Please provide a response to the prior user question. Keep in mind the following:
# 1. You are a world-famous AI help-desk assistant for Spira.
# 2. You do not know anything except for information about Spira.
# 3. Your response should be formatted as a
# """


@dataclass
class BasicSpiraPrompt(OpenAIRequest):
    """Represents a request to the Azure OpenAI API to determine if the user is asking about Spira."""

    _system_prompt: str = SYSTEM_PROMPT
    # _post_user_prompt: str = POST_USER_PROMPT

    def connect(self):
        self._ai_provider = AzureOpenAIProvider()

    def prompt(self, prompt: str) -> str:
        """Return a 'Y' or 'N' response to the question of whether the user is asking about Spira in their prompt."""
        return self._prompt(prompt).content

    async def aprompt(self, prompt: str) -> str:
        """Same as prompt, but async."""
        return await self._aprompt(prompt).content
        # return YesNoResponse(response=response)
