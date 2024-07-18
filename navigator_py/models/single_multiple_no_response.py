"""pydantic model for a single/multiple/no response."""

from pydantic import BaseModel, Field


class SingleMultipleNoResponse(BaseModel):
    """Model to validate that a response is either 'S', 'M', or 'N'."""

    # The response to validate
    response: str = Field(..., min_length=1, max_length=1, pattern="^[SMN]$")
