from typing import Annotated, Optional

from pydantic import BaseModel, Field, StringConstraints


class Group(BaseModel):
    id: Annotated[str, StringConstraints(pattern=r"^[0-9,_,a-z,A-Z]*$")] = Field(
        description='A short, unique, informative identifier containing only alphanumeric characters and underscores. Typically used to generate variable names. Example: "outfile_group".',
        min_length=1,
    )
    name: str = Field(
        description="A human-readable name for the input group.", min_length=1
    )
    description: Optional[str] = Field(
        description="Description of the input group.", default=None
    )
    members: list[Annotated[str, StringConstraints(pattern=r"^[0-9,_,a-z,A-Z]*$")]] = (
        Field(description="IDs of the inputs belonging to this group.")
    )
    mutually_exclusive: bool = Field(
        alias="mutually-exclusive",
        description="True if only one input in the group may be active at runtime.",
        default=False,
    )
    one_is_required: bool = Field(
        alias="one-is-required",
        description="True if at least one of the inputs in the group must be active at runtime.",
        default=False,
    )
    all_or_one: bool = Field(
        alias="all-or-none",
        description="True if members of the group need to be toggled together",
        default=False,
    )
