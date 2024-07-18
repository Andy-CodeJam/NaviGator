"""Define some configuration options relevant to the navigator_py package/generative AI."""

from dataclasses import dataclass

# export the instanced config object by default
__all__ = ["config"]


@dataclass
class Config:
    """Configuration options for the navigator_py package."""

    # The maximum number of tokens to generate in a response
    max_tokens: int = 60

    # The temperature to use when generating a response (keeping it low
    # to avoid randomness)
    temperature: float = 0.05


config = Config()
