# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__DICE_METRIC_METADATA = Metadata(
    id="98eaa1a4d4837bef42b0135a72612d83719e6632.boutiques",
    name="@DiceMetric",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VDiceMetricParameters = typing.TypedDict('VDiceMetricParameters', {
    "__STYX_TYPE__": typing.Literal["@DiceMetric"],
    "base": InputPathType,
    "dsets": list[InputPathType],
    "max_roi": typing.NotRequired[float | None],
    "forceoutput": typing.NotRequired[InputPathType | None],
    "forceoutput_1": typing.NotRequired[InputPathType | None],
    "echo": bool,
    "save_match": bool,
    "save_diff": bool,
    "do_not_mask_by_base": bool,
    "mask_by_base": bool,
    "prefix": typing.NotRequired[str | None],
    "ignore_bad": bool,
    "keep_tmp": bool,
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
        "@DiceMetric": v__dice_metric_cargs,
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
    }.get(t)


class VDiceMetricOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__dice_metric(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__dice_metric_params(
    base: InputPathType,
    dsets: list[InputPathType],
    max_roi: float | None = None,
    forceoutput: InputPathType | None = None,
    forceoutput_1: InputPathType | None = None,
    echo: bool = False,
    save_match: bool = False,
    save_diff: bool = False,
    do_not_mask_by_base: bool = False,
    mask_by_base: bool = False,
    prefix: str | None = None,
    ignore_bad: bool = False,
    keep_tmp: bool = False,
) -> VDiceMetricParameters:
    """
    Build parameters.
    
    Args:
        base: Name of base (reference) segmentation.
        dsets: Data sets for which the Dice Metric with BASE is computed. This\
            should be the last option on the command line.
        max_roi: The maximum possible ROI index. Default is 12 or based on\
            LTFILE if specified.
        forceoutput: If given, force output for each class in LTFILE.
        forceoutput_1: If given, force output for each class in LTFILE.
        echo: Set echo.
        save_match: Save volume showing BASE*equals(BASE,DSET).
        save_diff: Save volume showing BASE*(1-equals(BASE,DSET)).
        do_not_mask_by_base: Do not mask dset by step(base) before computing\
            Dice coefficient.
        mask_by_base: Mask dset by the step(base) before computing Dice\
            coefficient.
        prefix: Use PREFIX for the output table. Default is separate results\
            for each dset to stdout.
        ignore_bad: Warn if encountering bad scenarios, but do not create a\
            zero entry.
        keep_tmp: Keep temporary files for debugging. Note that you should\
            delete temporary files before rerunning the script.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@DiceMetric",
        "base": base,
        "dsets": dsets,
        "echo": echo,
        "save_match": save_match,
        "save_diff": save_diff,
        "do_not_mask_by_base": do_not_mask_by_base,
        "mask_by_base": mask_by_base,
        "ignore_bad": ignore_bad,
        "keep_tmp": keep_tmp,
    }
    if max_roi is not None:
        params["max_roi"] = max_roi
    if forceoutput is not None:
        params["forceoutput"] = forceoutput
    if forceoutput_1 is not None:
        params["forceoutput_1"] = forceoutput_1
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v__dice_metric_cargs(
    params: VDiceMetricParameters,
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
    cargs.append("@DiceMetric")
    cargs.extend([
        "-base",
        execution.input_file(params.get("base"))
    ])
    cargs.extend([
        "-dsets",
        *[execution.input_file(f) for f in params.get("dsets")]
    ])
    if params.get("max_roi") is not None:
        cargs.extend([
            "-max_N_roi",
            str(params.get("max_roi"))
        ])
    if params.get("forceoutput") is not None:
        cargs.extend([
            "-forceoutput",
            execution.input_file(params.get("forceoutput"))
        ])
    if params.get("forceoutput_1") is not None:
        cargs.extend([
            "-forceoutput",
            execution.input_file(params.get("forceoutput_1"))
        ])
    if params.get("echo"):
        cargs.append("-echo")
    if params.get("save_match"):
        cargs.append("-save_match")
    if params.get("save_diff"):
        cargs.append("-save_diff")
    if params.get("do_not_mask_by_base"):
        cargs.append("-do_not_mask_by_base")
    if params.get("mask_by_base"):
        cargs.append("-mask_by_base")
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("ignore_bad"):
        cargs.append("-ignore_bad")
    if params.get("keep_tmp"):
        cargs.append("-keep_tmp")
    return cargs


def v__dice_metric_outputs(
    params: VDiceMetricParameters,
    execution: Execution,
) -> VDiceMetricOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VDiceMetricOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__dice_metric_execute(
    params: VDiceMetricParameters,
    execution: Execution,
) -> VDiceMetricOutputs:
    """
    Computes Dice Metric between BASE and each of the DSET volumes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VDiceMetricOutputs`).
    """
    params = execution.params(params)
    cargs = v__dice_metric_cargs(params, execution)
    ret = v__dice_metric_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__dice_metric(
    base: InputPathType,
    dsets: list[InputPathType],
    max_roi: float | None = None,
    forceoutput: InputPathType | None = None,
    forceoutput_1: InputPathType | None = None,
    echo: bool = False,
    save_match: bool = False,
    save_diff: bool = False,
    do_not_mask_by_base: bool = False,
    mask_by_base: bool = False,
    prefix: str | None = None,
    ignore_bad: bool = False,
    keep_tmp: bool = False,
    runner: Runner | None = None,
) -> VDiceMetricOutputs:
    """
    Computes Dice Metric between BASE and each of the DSET volumes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        base: Name of base (reference) segmentation.
        dsets: Data sets for which the Dice Metric with BASE is computed. This\
            should be the last option on the command line.
        max_roi: The maximum possible ROI index. Default is 12 or based on\
            LTFILE if specified.
        forceoutput: If given, force output for each class in LTFILE.
        forceoutput_1: If given, force output for each class in LTFILE.
        echo: Set echo.
        save_match: Save volume showing BASE*equals(BASE,DSET).
        save_diff: Save volume showing BASE*(1-equals(BASE,DSET)).
        do_not_mask_by_base: Do not mask dset by step(base) before computing\
            Dice coefficient.
        mask_by_base: Mask dset by the step(base) before computing Dice\
            coefficient.
        prefix: Use PREFIX for the output table. Default is separate results\
            for each dset to stdout.
        ignore_bad: Warn if encountering bad scenarios, but do not create a\
            zero entry.
        keep_tmp: Keep temporary files for debugging. Note that you should\
            delete temporary files before rerunning the script.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDiceMetricOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DICE_METRIC_METADATA)
    params = v__dice_metric_params(base=base, dsets=dsets, max_roi=max_roi, forceoutput=forceoutput, forceoutput_1=forceoutput_1, echo=echo, save_match=save_match, save_diff=save_diff, do_not_mask_by_base=do_not_mask_by_base, mask_by_base=mask_by_base, prefix=prefix, ignore_bad=ignore_bad, keep_tmp=keep_tmp)
    return v__dice_metric_execute(params, execution)


__all__ = [
    "VDiceMetricOutputs",
    "VDiceMetricParameters",
    "V__DICE_METRIC_METADATA",
    "v__dice_metric",
    "v__dice_metric_params",
]
