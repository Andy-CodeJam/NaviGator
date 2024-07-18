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
You have no knowledge of anything besides Spira.
Your only purpose is to take the following user prompt and three articles and generate a response that is relevant to the user prompt.
Your response should cite the articles where approriate. 
====================================
"""

POST_USER_PROMPT = """
====================================

Given the above user prompt and articles, please provide a response that is relevant to the user prompt.
Keep in mind the following:
1. You are a world-famous AI help-desk assistant for Spira.
2. You do not know anything except for information about Spira.
3. Your response should be formatted in markdown similarly in structure to a blog post.
4. You are providing this response to a customer support representative who is currently on the line with a very impatient caller.
5. Please make your response as concise and to-the-point as possible.

"""


@dataclass
class UseArticlesToGenerateAnswer(OpenAIRequest):
    """Represents a request to the Azure OpenAI API to determine if there is a single topic in the prompt."""

    _system_prompt: str = SYSTEM_PROMPT
    _post_user_prompt: str = POST_USER_PROMPT
    articles: list[dict] | None = None

    def __post_init__(self):
        if self.articles is None:
            raise ValueError("Articles must be provided.")

    def connect(self):
        self._ai_provider = AzureOpenAIProvider()

    def _updated_prompt(self, prompt: str) -> str:
        """Update the prompt with the articles."""
        return f"""{prompt}
        
        ========================
        
        The three articles are reproduced below:
        {self.articles}"""

    def prompt(self, prompt: str) -> str:
        """Generate an answer to the prompt based on the articles."""
        updated_prompt = self._updated_prompt(prompt)
        response = self._prompt(updated_prompt).content
        return response

    async def aprompt(self, prompt: str) -> str:
        """Same as prompt, but async."""
        response = await self._aprompt(prompt).content
        return response
