# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

AP_RUN_SIMPLE_REST_METADATA = Metadata(
    id="51acc3d2305cb727e55055aa552281969a79036d.boutiques",
    name="ap_run_simple_rest",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ApRunSimpleRestParameters = typing.TypedDict('ApRunSimpleRestParameters', {
    "__STYX_TYPE__": typing.Literal["ap_run_simple_rest"],
    "anat": typing.NotRequired[InputPathType | None],
    "epi": list[InputPathType],
    "nt_rm": typing.NotRequired[float | None],
    "run_ap": bool,
    "run_proc": bool,
    "subjid": typing.NotRequired[str | None],
    "template": typing.NotRequired[InputPathType | None],
    "compressor": typing.NotRequired[str | None],
    "verb": typing.NotRequired[float | None],
    "echo": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "ap_run_simple_rest": ap_run_simple_rest_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "ap_run_simple_rest": ap_run_simple_rest_outputs,
    }.get(t)


class ApRunSimpleRestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ap_run_simple_rest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    run_ap_script: OutputPathType | None
    """afni_proc.py command script"""
    proc_script: OutputPathType | None
    """proc script (if AP is run)"""
    proc_results_dir: OutputPathType | None
    """proc results directory (if run)"""
    text_output_files: OutputPathType
    """Text output files from AP and proc scripts"""


def ap_run_simple_rest_params(
    epi: list[InputPathType],
    anat: InputPathType | None = None,
    nt_rm: float | None = None,
    run_ap: bool = False,
    run_proc: bool = False,
    subjid: str | None = None,
    template: InputPathType | None = None,
    compressor: str | None = None,
    verb: float | None = None,
    echo: bool = False,
) -> ApRunSimpleRestParameters:
    """
    Build parameters.
    
    Args:
        epi: EPI datasets.
        anat: Single anatomical dataset.
        nt_rm: Number of time points to remove from starts of runs.
        run_ap: Run the afni_proc.py command.
        run_proc: Run the proc script from afni_proc.py command.
        subjid: Specify subject ID for file names.
        template: Specify template for standard space.
        compressor: Control automatic compression of *.BRIK files.
        verb: Specify verbosity level.
        echo: Same as verbosity level 3.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ap_run_simple_rest",
        "epi": epi,
        "run_ap": run_ap,
        "run_proc": run_proc,
        "echo": echo,
    }
    if anat is not None:
        params["anat"] = anat
    if nt_rm is not None:
        params["nt_rm"] = nt_rm
    if subjid is not None:
        params["subjid"] = subjid
    if template is not None:
        params["template"] = template
    if compressor is not None:
        params["compressor"] = compressor
    if verb is not None:
        params["verb"] = verb
    return params


def ap_run_simple_rest_cargs(
    params: ApRunSimpleRestParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("ap_run_simple_rest.tcsh")
    if params.get("anat") is not None:
        cargs.extend([
            "-anat",
            execution.input_file(params.get("anat"))
        ])
    cargs.extend([
        "-epi",
        *[execution.input_file(f) for f in params.get("epi")]
    ])
    if params.get("nt_rm") is not None:
        cargs.extend([
            "-nt_rm",
            str(params.get("nt_rm"))
        ])
    if params.get("run_ap"):
        cargs.append("-run_ap")
    if params.get("run_proc"):
        cargs.append("-run_proc")
    if params.get("subjid") is not None:
        cargs.extend([
            "-subjid",
            params.get("subjid")
        ])
    if params.get("template") is not None:
        cargs.extend([
            "-template",
            execution.input_file(params.get("template"))
        ])
    if params.get("compressor") is not None:
        cargs.extend([
            "-compressor",
            params.get("compressor")
        ])
    if params.get("verb") is not None:
        cargs.extend([
            "-verb",
            str(params.get("verb"))
        ])
    if params.get("echo"):
        cargs.append("-echo")
    return cargs


def ap_run_simple_rest_outputs(
    params: ApRunSimpleRestParameters,
    execution: Execution,
) -> ApRunSimpleRestOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ApRunSimpleRestOutputs(
        root=execution.output_file("."),
        run_ap_script=execution.output_file("run_ap_" + params.get("subjid")) if (params.get("subjid") is not None) else None,
        proc_script=execution.output_file("proc." + params.get("subjid")) if (params.get("subjid") is not None) else None,
        proc_results_dir=execution.output_file(params.get("subjid") + ".results") if (params.get("subjid") is not None) else None,
        text_output_files=execution.output_file("out.*"),
    )
    return ret


def ap_run_simple_rest_execute(
    params: ApRunSimpleRestParameters,
    execution: Execution,
) -> ApRunSimpleRestOutputs:
    """
    Run a quick afni_proc.py analysis for QC.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ApRunSimpleRestOutputs`).
    """
    cargs = ap_run_simple_rest_cargs(params, execution)
    ret = ap_run_simple_rest_outputs(params, execution)
    execution.run(cargs)
    return ret


def ap_run_simple_rest(
    epi: list[InputPathType],
    anat: InputPathType | None = None,
    nt_rm: float | None = None,
    run_ap: bool = False,
    run_proc: bool = False,
    subjid: str | None = None,
    template: InputPathType | None = None,
    compressor: str | None = None,
    verb: float | None = None,
    echo: bool = False,
    runner: Runner | None = None,
) -> ApRunSimpleRestOutputs:
    """
    Run a quick afni_proc.py analysis for QC.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        epi: EPI datasets.
        anat: Single anatomical dataset.
        nt_rm: Number of time points to remove from starts of runs.
        run_ap: Run the afni_proc.py command.
        run_proc: Run the proc script from afni_proc.py command.
        subjid: Specify subject ID for file names.
        template: Specify template for standard space.
        compressor: Control automatic compression of *.BRIK files.
        verb: Specify verbosity level.
        echo: Same as verbosity level 3.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ApRunSimpleRestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AP_RUN_SIMPLE_REST_METADATA)
    params = ap_run_simple_rest_params(anat=anat, epi=epi, nt_rm=nt_rm, run_ap=run_ap, run_proc=run_proc, subjid=subjid, template=template, compressor=compressor, verb=verb, echo=echo)
    return ap_run_simple_rest_execute(params, execution)


__all__ = [
    "AP_RUN_SIMPLE_REST_METADATA",
    "ApRunSimpleRestOutputs",
    "ApRunSimpleRestParameters",
    "ap_run_simple_rest",
    "ap_run_simple_rest_params",
]
