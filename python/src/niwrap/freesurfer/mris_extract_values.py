# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_EXTRACT_VALUES_METADATA = Metadata(
    id="d71ebcb707ea3a328def8029909fffc5889d56d6.boutiques",
    name="mris_extract_values",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisExtractValuesParameters = typing.TypedDict('MrisExtractValuesParameters', {
    "__STYX_TYPE__": typing.Literal["mris_extract_values"],
    "surface": InputPathType,
    "overlay": InputPathType,
    "annotation": InputPathType,
    "csvfile": str,
    "num_images": float,
    "image_files": list[InputPathType],
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
        "mris_extract_values": mris_extract_values_cargs,
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
        "mris_extract_values": mris_extract_values_outputs,
    }.get(t)


class MrisExtractValuesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_extract_values(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_csv: OutputPathType
    """The CSV file generated by the tool"""


def mris_extract_values_params(
    surface: InputPathType,
    overlay: InputPathType,
    annotation: InputPathType,
    csvfile: str,
    num_images: float,
    image_files: list[InputPathType],
) -> MrisExtractValuesParameters:
    """
    Build parameters.
    
    Args:
        surface: Path to the surface file.
        overlay: Path to the overlay file.
        annotation: Path to the annotation file.
        csvfile: Name of the output CSV file.
        num_images: Number of image files to process.
        image_files: List of image files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_extract_values",
        "surface": surface,
        "overlay": overlay,
        "annotation": annotation,
        "csvfile": csvfile,
        "num_images": num_images,
        "image_files": image_files,
    }
    return params


def mris_extract_values_cargs(
    params: MrisExtractValuesParameters,
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
    cargs.append("mris_extract_values")
    cargs.extend([
        "-i",
        execution.input_file(params.get("surface"))
    ])
    cargs.extend([
        "-v",
        execution.input_file(params.get("overlay"))
    ])
    cargs.extend([
        "-a",
        execution.input_file(params.get("annotation"))
    ])
    cargs.extend([
        "-o",
        params.get("csvfile")
    ])
    cargs.extend([
        "-m",
        str(params.get("num_images"))
    ])
    cargs.extend([
        "--images",
        *[execution.input_file(f) for f in params.get("image_files")]
    ])
    return cargs


def mris_extract_values_outputs(
    params: MrisExtractValuesParameters,
    execution: Execution,
) -> MrisExtractValuesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisExtractValuesOutputs(
        root=execution.output_file("."),
        output_csv=execution.output_file(params.get("csvfile")),
    )
    return ret


def mris_extract_values_execute(
    params: MrisExtractValuesParameters,
    execution: Execution,
) -> MrisExtractValuesOutputs:
    """
    Extracts values from surface, overlay, and annotation files and outputs them to
    a CSV file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisExtractValuesOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_extract_values_cargs(params, execution)
    ret = mris_extract_values_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_extract_values(
    surface: InputPathType,
    overlay: InputPathType,
    annotation: InputPathType,
    csvfile: str,
    num_images: float,
    image_files: list[InputPathType],
    runner: Runner | None = None,
) -> MrisExtractValuesOutputs:
    """
    Extracts values from surface, overlay, and annotation files and outputs them to
    a CSV file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Path to the surface file.
        overlay: Path to the overlay file.
        annotation: Path to the annotation file.
        csvfile: Name of the output CSV file.
        num_images: Number of image files to process.
        image_files: List of image files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisExtractValuesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_EXTRACT_VALUES_METADATA)
    params = mris_extract_values_params(surface=surface, overlay=overlay, annotation=annotation, csvfile=csvfile, num_images=num_images, image_files=image_files)
    return mris_extract_values_execute(params, execution)


__all__ = [
    "MRIS_EXTRACT_VALUES_METADATA",
    "MrisExtractValuesOutputs",
    "MrisExtractValuesParameters",
    "mris_extract_values",
    "mris_extract_values_params",
]
