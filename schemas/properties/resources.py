from pydantic import BaseModel, Field, model_validator


class SuggestedResources(BaseModel):
    cpu_cores: int = Field(
        alias="cpu-core",
        description="The requested number of cpu cores to run the described application",
        ge=1,
    )
    ram: float = Field(
        description="The requested number of GB RAM to run the described application",
        ge=0,
    )
    disk_space: float = Field(
        alias="disk-space",
        description="The requested number of GB of storage to run the described application",
        ge=0,
    )
    nodes: int = Field(
        description="The requested number of nodes to spread the described application across",
        ge=1,
    )
    walltime_estimate: float = Field(
        alias="walltime-estimate",
        description="Estimated wall time of a task in seconds.",
        ge=0,
    )
