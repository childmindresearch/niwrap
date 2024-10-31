from pydantic import BaseModel, Field


class ErrorCode(BaseModel):
    code: int = Field(description="Value of the exit code")
    description: str = Field(description="Description of the error code.")
