from typing import Annotated, Optional

from pydantic import BaseModel, Field, StringConstraints


class EnvironmentVariable(BaseModel):
    name: Annotated[str, StringConstraints(pattern=r"^[a-z,A-Z][0-9,_,a-z,A-Z]*$")] = (
        Field(
            description='The environment variable name (identifier) containing only alphanumeric characters and underscores. Example: "PROGRAM_PATH".',
            min_length=1,
        )
    )
    value: str = Field(description="The value of the environment variable.")
    description: Optional[str] = Field(
        description="Description of the environment variable.", default=None
    )
