"""pydantic model for a yes/no response."""

# from dataclasses import dataclass

from pydantic import BaseModel, Field


# @dataclass
class YesNoResponse(BaseModel):
    """Model to validate that a response is either 'Y' or 'N'."""

    # The response to validate
    response: str = Field(..., min_length=1, max_length=1, pattern="^[YN]$")
