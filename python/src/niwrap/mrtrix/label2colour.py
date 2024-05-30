# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


LABEL2COLOUR_METADATA = Metadata(
    id="c4f6aaaf20fd52063e88fcdc01019a97ce9a411e",
    name="label2colour",
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


class Label2colourOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label2colour(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    colour_out: OutputPathType
    """the output colour image"""
    config: ConfigOutputs
    """Subcommand outputs"""


def label2colour(
    nodes_in: InputPathType,
    colour_out: InputPathType,
    lut: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Config] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Label2colourOutputs:
    """
    label2colour by Robert E. Smith (robert.smith@florey.edu.au).
    
    Convert a parcellated image (where values are node indices) into a colour
    image.
    
    Many software packages handle this colouring internally within their viewer
    program; this binary explicitly converts a parcellation image into a colour
    image that should be viewable in any software.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/label2colour.html
    
    Args:
        nodes_in: the input node parcellation image
        colour_out: the output colour image
        lut: Provide the relevant colour lookup table (if not provided, nodes
            will be coloured randomly)
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
        NamedTuple of outputs (described in `Label2colourOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL2COLOUR_METADATA)
    cargs = []
    cargs.append("label2colour")
    if lut is not None:
        cargs.extend(["-lut", execution.input_file(lut)])
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
    cargs.append(execution.input_file(nodes_in))
    cargs.append(execution.input_file(colour_out))
    ret = Label2colourOutputs(
        root=execution.output_file("."),
        colour_out=execution.output_file(f"{pathlib.Path(colour_out).name}"),
        config=[config.outputs(execution) for config in config],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "Config",
    "ConfigOutputs",
    "LABEL2COLOUR_METADATA",
    "Label2colourOutputs",
    "label2colour",
]
