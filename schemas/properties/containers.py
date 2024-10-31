from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ContainerEnum(str, Enum):
    DOCKER = "docker"
    SINGULARITY = "singularity"


class DockerSingularityContainer(BaseModel):
    type_: ContainerEnum = Field(alias="type")
    image: str = Field(
        description="Name of an image where the tool is installed and configured. Example: bids/mriqc.",
        min_length=1,
    )
    entrypoint: bool = Field(
        description="Flag indicating whether or not the container uses an entrypoint.",
        default=False,
    )
    index: Optional[str] = Field(
        description="Optional index where the image is available, if not the standard location. Example: docker.io",
        min_length=1,
        default=None,
    )
    container_opts: Optional[list[str]] = Field(
        alias="container-opts",
        description="Container-level arguments for the application. Example: --privileged",
        default=None,
    )
    working_directory: Optional[str] = Field(
        alias="working-directory",
        description="Location from which this task must be launched within the container.",
        min_length=1,
        default=None,
    )
    container_hash: Optional[str] = Field(
        alias="container-hash",
        description="Hash for the given container.",
        min_length=1,
        default=None,
    )


class RootfsContainer(BaseModel):
    type_: Literal["rootfs"] = Field(alias="type")
    url: str = Field(description="URL where the image is available.", min_length=1)
    working_directory: Optional[str] = Field(
        alias="working-directory",
        description="Location from which this task must be launched within the container.",
        min_length=1,
        default=None,
    )
    container_hash: Optional[str] = Field(
        alias="container-hash",
        description="Hash for the given container.",
        min_length=1,
        default=None,
    )
