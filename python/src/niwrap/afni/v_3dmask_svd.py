# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DMASK_SVD_METADATA = Metadata(
    id="befb278fb0ea3598cbac3ecadbabb48616183c88",
    name="3dmaskSVD",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dmaskSvdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmask_svd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    svd_output: OutputPathType
    """Singular vector output redirected to this file"""


def v_3dmask_svd(
    input_dataset: InputPathType,
    vnorm: bool = False,
    sval: float | int | None = None,
    mask_file: InputPathType | None = None,
    automask: bool = False,
    polort: float | int | None = None,
    bandpass: list[str] | None = None,
    ort: list[InputPathType] | None = None,
    alt_input: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dmaskSvdOutputs:
    """
    3dmaskSVD by AFNI Team.
    
    Computes the principal singular vector of the time series vectors extracted
    from the input dataset over the input mask.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dmaskSVD.html
    
    Args:
        input_dataset: Input dataset.
        vnorm: L2 normalize all time series before SVD.
        sval: Output singular vectors 0 .. a (default a=0 = first one only).
        mask_file: Define the mask (default is entire dataset).
        automask: Automatic mask definition.
        polort: Remove polynomial trend (default 0 if not specified).
        bandpass: Bandpass filter (mutually exclusive with -polort).
        ort: Time series to remove from the data before SVD-ization. You can\
            give more than 1 '-ort' option. 'xx.1D' can contain more than 1 column.
        alt_input: Alternative way to give the input dataset name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmaskSvdOutputs`).
    """
    runner = runner or get_global_runner()
    if bandpass is not None and (len(bandpass) != 2): 
        raise ValueError(f"Length of 'bandpass' must be 2 but was {len(bandpass)}")
    if ort is not None and not (len(ort) <= 999): 
        raise ValueError(f"Length of 'ort' must be less than 999 but was {len(ort)}")
    execution = runner.start_execution(V_3DMASK_SVD_METADATA)
    cargs = []
    cargs.append("3dmaskSVD")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(input_dataset))
    ret = V3dmaskSvdOutputs(
        root=execution.output_file("."),
        svd_output=execution.output_file(f"../stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dmaskSvdOutputs",
    "V_3DMASK_SVD_METADATA",
    "v_3dmask_svd",
]
