import pathlib
import typing

InputPathType: typing.TypeAlias = pathlib.Path | str
"""Input host file type."""
OutputPathType: typing.TypeAlias = pathlib.Path | str
"""Output host file type."""


class Execution(typing.Protocol):
    """Execution object used to execute commands.

    Created by `Runner.start_execution()`.
    """

    def input_file(self, host_file: InputPathType) -> str:
        """Resolve host input files.

        Returns a local filepath.
        Called (potentially multiple times) after
        `Runner.start_execution()` and before `Runner.run()`.
        """
        ...

    def run(self, cargs: list[str]) -> None:
        """Run the command.

        Called after all `Execution.input_file()`
        and `Execution.output_file()` calls.
        """
        ...

    def output_file(self, local_file: str, optional: bool = False) -> OutputPathType:
        """Resolve local output files.

        Returns a host filepath.
        Called (potentially multiple times) after all
        `Runner.input_file()` calls.
        """
        ...


class Metadata(typing.NamedTuple):
    """Static tool metadata.

    This is structured static metadata that is known at compile time.
    Runners can use this to set up execution environments.
    """

    id: str
    """Unique identifier of the tool."""
    name: str
    """Name of the tool."""
    container_image_type: str | None = None
    """Type of container image. Example: docker, singularity."""
    container_image_tag: str | None = None
    """Name of an image where the tool is installed and configured. Example: bids/mriqc."""
    container_image_index: str | None = None
    """Optional index where the image is available, if not the standard location. Example: docker.io"""
    container_image_opts: str | None = None
    """Container-level arguments for the application. Example: --privileged"""


class Runner(typing.Protocol):
    """Runner object used to execute commands.

    Possible examples would be `LocalRunner`,
    `DockerRunner`, `DebugRunner`, ...
    Used as a factory for `Execution` objects.
    """

    def start_execution(self, metadata: Metadata) -> Execution:
        """Start an execution.

        Called before any `Execution.input_file()` calls.
        """
        ...
