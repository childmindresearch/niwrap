# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

AFNI_SYSTEM_CHECK_PY_METADATA = Metadata(
    id="e0985a91d76491809a46edfaec398aa39eb03ae8",
    name="afni_system_check.py",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AfniSystemCheckPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_system_check_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def afni_system_check_py(
    check_all: bool = False,
    find_prog: str | None = None,
    exact: str | None = None,
    disp_num_cpu: bool = False,
    disp_ver_matplotlib: bool = False,
    dot_file_list: bool = False,
    dot_file_show: bool = False,
    dot_file_pack: str | None = None,
    casematch: str | None = None,
    data_root: str | None = None,
    runner: Runner | None = None,
) -> AfniSystemCheckPyOutputs:
    """
    afni_system_check.py by AFNI Team.
    
    Perform various system checks for figuring out AFNI installation issues.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/afni_system_check.py.html
    
    Args:
        check_all: Perform all system checks.
        find_prog: Search PATH for PROG.
        exact: Search for PROG without wildcards in -find_prog.
        disp_num_cpu: Display number of CPUs available.
        disp_ver_matplotlib: Display matplotlib version (else 'None').
        dot_file_list: List all found dot files (startup files).
        dot_file_show: Display contents of all found dot files.
        dot_file_pack: Create a NAME.tgz package containing dot files.
        casematch: Match case in -find_prog.
        data_root: Search for class data under DDIR.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniSystemCheckPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_SYSTEM_CHECK_PY_METADATA)
    cargs = []
    cargs.append("afni_system_check.py")
    cargs.append("[TERMINAL_OPTS]")
    cargs.append("[ACTION_OPTS]")
    cargs.append("[OTHER_OPTS]")
    ret = AfniSystemCheckPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFNI_SYSTEM_CHECK_PY_METADATA",
    "AfniSystemCheckPyOutputs",
    "afni_system_check_py",
]