"""pydantic model for a yes/no response."""

from pydantic import BaseModel, Field


class YesNoResponse(BaseModel):
    """Model to validate that a response is either 'Y' or 'N'."""

    # The response to validate
    response: str = Field(..., min_length=1, max_length=1, pattern="^[YN]$")
