# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

BAYCEST_METADATA = Metadata(
    id="ae3b42b963b4c243d395709910b8502ef7829164",
    name="baycest",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="baycest/baycest:latest",
)


class BaycestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `baycest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Main output file"""


def baycest(
    data_file: InputPathType,
    mask_file: InputPathType,
    output_dir: str,
    pools_file: InputPathType,
    spec_file: InputPathType,
    ptrain_file: InputPathType,
    spatial_flag: bool = False,
    t12prior_flag: bool = False,
    runner: Runner | None = None,
) -> BaycestOutputs:
    """
    baycest by Bayesian Analysis Group.
    
    Bayesian analysis for chemical exchange saturation transfer z-spectra.
    
    Args:
        data_file: Specify data file (nifti image).
        mask_file: Specify mask file (nifti image).
        output_dir: Specify output directory name.
        pools_file: Specify pools to be included in model (ascii matrix).
        spec_file: Data specification (ascii matrix).
        ptrain_file: Specify pulse shape (ascii matrix).
        spatial_flag: Use spatial prior (appropriate for in vivo data).
        t12prior_flag: Include uncertainty in T1 and T2 values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BaycestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BAYCEST_METADATA)
    cargs = []
    cargs.append("baycest")
    cargs.append(
        "--data=" +
        execution.input_file(data_file) +
        ""
    )
    cargs.append(
        "--mask=" +
        execution.input_file(mask_file) +
        ""
    )
    cargs.append(
        "--output=" +
        output_dir +
        ""
    )
    cargs.append(
        "--pools=" +
        execution.input_file(pools_file) +
        ""
    )
    cargs.append(
        "--spec=" +
        execution.input_file(spec_file) +
        ""
    )
    cargs.append(
        "--ptrain=" +
        execution.input_file(ptrain_file) +
        ""
    )
    if spatial_flag:
        cargs.append("--spatial")
    if t12prior_flag:
        cargs.append("--t12prior")
    ret = BaycestOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{output_dir}/output_file.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BAYCEST_METADATA",
    "BaycestOutputs",
    "baycest",
]
