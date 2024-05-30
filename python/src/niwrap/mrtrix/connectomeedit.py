# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


CONNECTOMEEDIT_METADATA = Metadata(
    id="e4127e3c7d0c43b2a34a69be209c72dfe99b280d",
    name="connectomeedit",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


class ConfigOutputs(typing.NamedTuple):
    """
    Output object returned when calling `Config.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class Config:
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> ConfigOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ConfigOutputs`).
        """
        ret = ConfigOutputs(
            root=execution.output_file("."),
        )
        return ret


class ConnectomeeditOutputs(typing.NamedTuple):
    """
    Output object returned when calling `connectomeedit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    config: ConfigOutputs
    """Subcommand outputs"""


def connectomeedit(
    input_: str,
    operation: typing.Literal["operation"],
    output: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Config] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> ConnectomeeditOutputs:
    """
    connectomeedit by Matteo Frigo (matteo.frigo@inria.fr).
    
    Perform basic operations on a connectome.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/connectomeedit.html
    
    Args:
        input_: the input connectome.
        operation: the operation to apply, one of: to_symmetric,
            upper_triangular, lower_triangular, transpose, zero_diagonal.
        output: the output connectome.
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `ConnectomeeditOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONNECTOMEEDIT_METADATA)
    cargs = []
    cargs.append("connectomeedit")
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
    cargs.append(input_)
    cargs.append(operation)
    cargs.append(output)
    ret = ConnectomeeditOutputs(
        root=execution.output_file("."),
        config=[config.outputs(execution) for config in config],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONNECTOMEEDIT_METADATA",
    "Config",
    "ConfigOutputs",
    "ConnectomeeditOutputs",
    "connectomeedit",
]
