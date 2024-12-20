# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DBUCKET_METADATA = Metadata(
    id="a07bb3d6d6114eb899f05be41e593f262e6cd274.boutiques",
    name="3dbucket",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dbucketOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dbucket(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3dbucket(
    input_files: list[str],
    prefix: str | None = None,
    session: str | None = None,
    glueto: str | None = None,
    aglueto: str | None = None,
    dry: bool = False,
    verbose: bool = False,
    fbuc: bool = False,
    abuc: bool = False,
    runner: Runner | None = None,
) -> V3dbucketOutputs:
    """
    Concatenate sub-bricks from input datasets into one big bucket dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input datasets with optional sub-brick selection.
        prefix: Use 'pname' for the output dataset prefix name.
        session: Use 'dir' for the output dataset session directory.\
            [default='./'=current working directory].
        glueto: Append bricks to the end of the 'fname' dataset.
        aglueto: If fname dataset does not exist, create it (like -prefix).\
            Otherwise append to fname (like -glueto).
        dry: Execute a 'dry run'; only print out what would be done.
        verbose: Print out some verbose output as the program proceeds.
        fbuc: Create a functional bucket.
        abuc: Create an anatomical bucket. If neither of these options is\
            given, the output type is determined from the first input type.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dbucketOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DBUCKET_METADATA)
    cargs = []
    cargs.append("3dbucket")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if session is not None:
        cargs.extend([
            "-session",
            session
        ])
    if glueto is not None:
        cargs.extend([
            "-glueto",
            glueto
        ])
    if aglueto is not None:
        cargs.extend([
            "-aglueto",
            aglueto
        ])
    if dry:
        cargs.append("-dry")
    if verbose:
        cargs.append("-verb")
    if fbuc:
        cargs.append("-fbuc")
    if abuc:
        cargs.append("-abuc")
    cargs.extend(input_files)
    ret = V3dbucketOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dbucketOutputs",
    "V_3DBUCKET_METADATA",
    "v_3dbucket",
]
