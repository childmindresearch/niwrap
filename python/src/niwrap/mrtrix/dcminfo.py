# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DCMINFO_METADATA = Metadata(
    id="2f0ac96cc78649201507f26a2cd825cd37394362.boutiques",
    name="dcminfo",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class DcminfoTag:
    """
    print field specified by the group & element tags supplied. Tags should be
    supplied as Hexadecimal (i.e. as they appear in the -all listing).
    """
    group: str
    """print field specified by the group & element tags supplied. Tags should
    be supplied as Hexadecimal (i.e. as they appear in the -all listing)."""
    element: str
    """print field specified by the group & element tags supplied. Tags should
    be supplied as Hexadecimal (i.e. as they appear in the -all listing)."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-tag")
        cargs.append(self.group)
        cargs.append(self.element)
        return cargs


@dataclasses.dataclass
class DcminfoConfig:
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
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class DcminfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcminfo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dcminfo(
    file: InputPathType,
    all_: bool = False,
    csa: bool = False,
    phoenix: bool = False,
    tag: list[DcminfoTag] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DcminfoConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> DcminfoOutputs:
    """
    Output DICOM fields in human-readable format.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        file: the DICOM file to be scanned.
        all_: print all DICOM fields.
        csa: print all Siemens CSA fields (excluding Phoenix unless requested).
        phoenix: print Siemens Phoenix protocol information.
        tag: print field specified by the group & element tags supplied. Tags\
            should be supplied as Hexadecimal (i.e. as they appear in the -all\
            listing).
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
        NamedTuple of outputs (described in `DcminfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMINFO_METADATA)
    cargs = []
    cargs.append("dcminfo")
    if all_:
        cargs.append("-all")
    if csa:
        cargs.append("-csa")
    if phoenix:
        cargs.append("-phoenix")
    if tag is not None:
        cargs.extend([a for c in [s.run(execution) for s in tag] for a in c])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend([
            "-nthreads",
            str(nthreads)
        ])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(file))
    ret = DcminfoOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DCMINFO_METADATA",
    "DcminfoConfig",
    "DcminfoOutputs",
    "DcminfoTag",
    "dcminfo",
]
