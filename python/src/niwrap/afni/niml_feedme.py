# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

NIML_FEEDME_METADATA = Metadata(
    id="23663cf53d4823ff642f7ddb0b1d228a321f193f",
    name="niml_feedme",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class NimlFeedmeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `niml_feedme(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def niml_feedme(
    dataset: InputPathType,
    host: str | None = None,
    interval: float | int | None = None,
    verbose: bool = False,
    accum: bool = False,
    target_dataset: str | None = None,
    drive_cmds: list[str] | None = None,
    runner: Runner | None = None,
) -> NimlFeedmeOutputs:
    """
    niml_feedme by AFNI Team.
    
    Sends volumes from the dataset to AFNI via the NIML socket interface.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/niml_feedme.html
    
    Args:
        dataset: Input dataset to be sent to AFNI.
        host: Send data, via TCP/IP, to AFNI running on the computer system\
            'sname'. By default, uses the current system (localhost), if you don't\
            use this option.
        interval: Tries to maintain an inter-transmit interval of 'ms'\
            milliseconds. The default is 1000 msec per volume.
        verbose: Be (very) talkative about actions.
        accum: Send sub-bricks so that they accumulate in AFNI. The default is\
            to create only a 1 volume dataset inside AFNI, and each sub-brick just\
            replaces that one volume when it is received.
        target_dataset: Change the dataset name transmitted to AFNI from\
            'niml_feedme' to 'nam'.
        drive_cmds: Send 'cmd' as a DRIVE_AFNI command. If cmd contains blanks,\
            it must be in 'quotes'. Multiple -drive options may be used. These\
            commands will be sent to AFNI just after the first volume is\
            transmitted. See file README.driver for a list of commands.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NimlFeedmeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NIML_FEEDME_METADATA)
    cargs = []
    cargs.append("niml_feedme")
    if host is not None:
        cargs.extend(["-host", host])
    if interval is not None:
        cargs.extend(["-dt", str(interval)])
    if verbose:
        cargs.append("-verb")
    if accum:
        cargs.append("-accum")
    if target_dataset is not None:
        cargs.extend(["-target", target_dataset])
    if drive_cmds is not None:
        cargs.extend(["-drive", *drive_cmds])
    cargs.append(execution.input_file(dataset))
    ret = NimlFeedmeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "NIML_FEEDME_METADATA",
    "NimlFeedmeOutputs",
    "niml_feedme",
]
