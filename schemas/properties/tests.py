from typing import Annotated, Any, Optional

from pydantic import BaseModel, Field, StringConstraints


class OutputFile(BaseModel):
    id: Annotated[str, StringConstraints(pattern=r"^[0-9,_,a-z,A-Z]*$")] = Field(
        description="Id referring to an output-file", min_length=1
    )
    md5_reference: Optional[str] = Field(
        alias="md5-reference",
        description="MD5 checksum string to match against the MD5 checksum of the output-file specified by the id object",
        min_length=1,
        default=None,
    )


class Assertion(BaseModel):
    exit_code: int = Field(
        alias="exit-code", description="Expected code returned by the program."
    )
    output_files: list[OutputFile] = Field(alias="output-files", min_length=1)


class TestCase(BaseModel):
    name: str = Field(description="Name of the test-case", min_length=1)
    invocation: Any
    assertions: Assertion
