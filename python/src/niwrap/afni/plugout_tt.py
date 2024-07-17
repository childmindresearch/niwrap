# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

PLUGOUT_TT_METADATA = Metadata(
    id="57cdae44df6d77cc63ff680b6d50b88c1aa97f99",
    name="plugout_tt",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class PlugoutTtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `plugout_tt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def plugout_tt(
    host: str | None = None,
    ijk_option: bool = False,
    verbose: bool = False,
    port: float | int | None = None,
    name: str | None = None,
    port_offset: float | int | None = None,
    port_offset_quiet: float | int | None = None,
    port_bloc: float | int | None = None,
    max_port_bloc: bool = False,
    max_port_bloc_quiet: bool = False,
    num_assigned_ports: bool = False,
    num_assigned_ports_quiet: bool = False,
    runner: Runner | None = None,
) -> PlugoutTtOutputs:
    """
    plugout_tt by AFNI Team.
    
    This program connects to AFNI and receives notification whenever the user
    changes Talairach coordinates.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/plugout_tt.html
    
    Args:
        host: Name of the host computer to connect to AFNI on. The default is\
            to connect on the current host using shared memory.
        ijk_option: Get voxel indices from AFNI instead of Talairach\
            coordinates.
        verbose: Enable verbose mode (prints lots of diagnostic messages).
        port: TCP/IP port number to use. The default is 8001.
        name: String to use as the name that AFNI assigns to this plugout. The\
            default is something silly.
        port_offset: Provide a port offset to allow multiple instances of\
            communicating programs to operate on the same computer. Use an integer\
            in the inclusive range [1025 to 65500].
        port_offset_quiet: Provide a port offset to allow multiple instances of\
            communicating programs to operate on the same computer with quiet\
            output in case of issues. Use an integer in the inclusive range [1025\
            to 65500].
        port_bloc: Provide a port offset bloc for easier configuration of\
            multiple instances. PORT_OFFSET_BLOC is an integer between 0 and\
            MAX_BLOC (around 4000).
        max_port_bloc: Print the current value of MAX_BLOC and exit. Stay under\
            2000 for safety.
        max_port_bloc_quiet: Print the current value of MAX_BLOC quietly and\
            exit.
        num_assigned_ports: Print the number of assigned ports used by AFNI,\
            then quit.
        num_assigned_ports_quiet: Print the number of assigned ports used by\
            AFNI quietly, then quit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PlugoutTtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PLUGOUT_TT_METADATA)
    cargs = []
    cargs.append("plugout_tt")
    if host is not None:
        cargs.extend(["-host", host])
    if ijk_option:
        cargs.append("-ijk")
    if verbose:
        cargs.append("-v")
    if port is not None:
        cargs.extend(["-port", str(port)])
    if name is not None:
        cargs.extend(["-name", name])
    if port_offset is not None:
        cargs.extend(["-np", str(port_offset)])
    if port_offset_quiet is not None:
        cargs.extend(["-npq", str(port_offset_quiet)])
    if port_bloc is not None:
        cargs.extend(["-npb", str(port_bloc)])
    if max_port_bloc:
        cargs.append("-max_port_bloc")
    if max_port_bloc_quiet:
        cargs.append("-max_port_bloc_quiet")
    if num_assigned_ports:
        cargs.append("-num_assigned_ports")
    if num_assigned_ports_quiet:
        cargs.append("-num_assigned_ports_quiet")
    ret = PlugoutTtOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PLUGOUT_TT_METADATA",
    "PlugoutTtOutputs",
    "plugout_tt",
]
