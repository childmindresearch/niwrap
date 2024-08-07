# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

TRANSFORMCONVERT_METADATA = Metadata(
    id="3a4a3ef4828a481fc9cdaa05890cd0cad5c5f34a",
    name="transformconvert",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TransformconvertConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class TransformconvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `transformconvert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output transformation matrix."""


def transformconvert(
    input_: list[str],
    operation: str,
    output: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TransformconvertConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TransformconvertOutputs:
    """
    transformconvert by Max Pietsch (maximilian.pietsch@kcl.ac.uk).
    
    Convert linear transformation matrices.
    
    This command allows to convert transformation matrices provided by other
    registration softwares to a format usable in MRtrix3. Example usages are
    provided below.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/transformconvert.html
    
    Args:
        input_: the input(s) for the specified operation.
        operation: the operation to perform, one of:\
            flirt_import, itk_import.
        output: the output transformation matrix.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TransformconvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TRANSFORMCONVERT_METADATA)
    cargs = []
    cargs.append("transformconvert")
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.extend(input_)
    cargs.append(operation)
    cargs.append(output)
    ret = TransformconvertOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{output}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TRANSFORMCONVERT_METADATA",
    "TransformconvertConfig",
    "TransformconvertOutputs",
    "transformconvert",
]
