# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRISP_PAINT_METADATA = Metadata(
    id="ee10714d3437e3ff63bdc4e23471b26ed9cb9121.boutiques",
    name="mrisp_paint",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrispPaintParameters = typing.TypedDict('MrispPaintParameters', {
    "__STYX_TYPE__": typing.Literal["mrisp_paint"],
    "template_file": InputPathType,
    "input_surface": InputPathType,
    "output_name": str,
    "subjects_dir": typing.NotRequired[str | None],
    "vertex_coords": typing.NotRequired[str | None],
    "average_flag": typing.NotRequired[float | None],
    "normalize_flag": bool,
    "frame_number": typing.NotRequired[float | None],
    "square_root_flag": bool,
    "variance_params": typing.NotRequired[str | None],
    "usage_flag": bool,
    "birn_info_flag": bool,
    "help_flag": bool,
    "diag_vertex": typing.NotRequired[float | None],
    "version_flag": bool,
    "diag_write_flag": bool,
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
        "mrisp_paint": mrisp_paint_cargs,
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
        "mrisp_paint": mrisp_paint_outputs,
    }.get(t)


class MrispPaintOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrisp_paint(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file containing a surface-worth of per-vertex values in
    'curvature' format."""


def mrisp_paint_params(
    template_file: InputPathType,
    input_surface: InputPathType,
    output_name: str,
    subjects_dir: str | None = None,
    vertex_coords: str | None = None,
    average_flag: float | None = None,
    normalize_flag: bool = False,
    frame_number: float | None = None,
    square_root_flag: bool = False,
    variance_params: str | None = None,
    usage_flag: bool = False,
    birn_info_flag: bool = False,
    help_flag: bool = False,
    diag_vertex: float | None = None,
    version_flag: bool = False,
    diag_write_flag: bool = False,
) -> MrispPaintParameters:
    """
    Build parameters.
    
    Args:
        template_file: Full path to the template file. Template may contain\
            multiple parameters. Example: 'somepath/mytemplate.tif#1'.
        input_surface: Full path to the input surface file, which provides the\
            grid onto which the template data is sampled.
        output_name: Output file name. Saves the surface-worth of per-vertex\
            values.
        subjects_dir: Set the SUBJECTS_DIR. Default: use environment variable.
        vertex_coords: Treat overlay as a surface and write it into a 3 frame\
            parameterization.
        average_flag: Average curvature patterns a given number of times.
        normalize_flag: Normalize curvature by variance.
        frame_number: Paint the specified frame number to the output file.\
            Default: 0.
        square_root_flag: Take the square-root of the output variable.
        variance_params: Generate variance map. Requires subject name,\
            hemisphere, and field number.
        usage_flag: Print usage.
        birn_info_flag: Print BIRN-standard program information.
        help_flag: Print help message.
        diag_vertex: Invoke diagnostics for a specific vertex number.
        version_flag: Print version information.
        diag_write_flag: Write some diagnostics (DIAG_WRITE).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mrisp_paint",
        "template_file": template_file,
        "input_surface": input_surface,
        "output_name": output_name,
        "normalize_flag": normalize_flag,
        "square_root_flag": square_root_flag,
        "usage_flag": usage_flag,
        "birn_info_flag": birn_info_flag,
        "help_flag": help_flag,
        "version_flag": version_flag,
        "diag_write_flag": diag_write_flag,
    }
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if vertex_coords is not None:
        params["vertex_coords"] = vertex_coords
    if average_flag is not None:
        params["average_flag"] = average_flag
    if frame_number is not None:
        params["frame_number"] = frame_number
    if variance_params is not None:
        params["variance_params"] = variance_params
    if diag_vertex is not None:
        params["diag_vertex"] = diag_vertex
    return params


def mrisp_paint_cargs(
    params: MrispPaintParameters,
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
    cargs.append("mrisp_paint")
    cargs.append(execution.input_file(params.get("template_file")))
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(params.get("output_name"))
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "-SDIR",
            params.get("subjects_dir")
        ])
    if params.get("vertex_coords") is not None:
        cargs.extend([
            "-coords",
            params.get("vertex_coords")
        ])
    if params.get("average_flag") is not None:
        cargs.extend([
            "-A",
            str(params.get("average_flag"))
        ])
    if params.get("normalize_flag"):
        cargs.append("-N")
    if params.get("frame_number") is not None:
        cargs.extend([
            "-f",
            str(params.get("frame_number"))
        ])
    if params.get("square_root_flag"):
        cargs.append("-S")
    if params.get("variance_params") is not None:
        cargs.extend([
            "-variance",
            params.get("variance_params")
        ])
    if params.get("usage_flag"):
        cargs.append("-?")
    if params.get("birn_info_flag"):
        cargs.append("--all-info")
    if params.get("help_flag"):
        cargs.append("--help")
    if params.get("diag_vertex") is not None:
        cargs.extend([
            "-V",
            str(params.get("diag_vertex"))
        ])
    if params.get("version_flag"):
        cargs.append("--version")
    if params.get("diag_write_flag"):
        cargs.append("-W")
    return cargs


def mrisp_paint_outputs(
    params: MrispPaintParameters,
    execution: Execution,
) -> MrispPaintOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrispPaintOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_name")),
    )
    return ret


def mrisp_paint_execute(
    params: MrispPaintParameters,
    execution: Execution,
) -> MrispPaintOutputs:
    """
    A tool for extracting arrays from a surface-registration template file and
    sampling them onto a surface mesh.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrispPaintOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mrisp_paint_cargs(params, execution)
    ret = mrisp_paint_outputs(params, execution)
    execution.run(cargs)
    return ret


def mrisp_paint(
    template_file: InputPathType,
    input_surface: InputPathType,
    output_name: str,
    subjects_dir: str | None = None,
    vertex_coords: str | None = None,
    average_flag: float | None = None,
    normalize_flag: bool = False,
    frame_number: float | None = None,
    square_root_flag: bool = False,
    variance_params: str | None = None,
    usage_flag: bool = False,
    birn_info_flag: bool = False,
    help_flag: bool = False,
    diag_vertex: float | None = None,
    version_flag: bool = False,
    diag_write_flag: bool = False,
    runner: Runner | None = None,
) -> MrispPaintOutputs:
    """
    A tool for extracting arrays from a surface-registration template file and
    sampling them onto a surface mesh.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        template_file: Full path to the template file. Template may contain\
            multiple parameters. Example: 'somepath/mytemplate.tif#1'.
        input_surface: Full path to the input surface file, which provides the\
            grid onto which the template data is sampled.
        output_name: Output file name. Saves the surface-worth of per-vertex\
            values.
        subjects_dir: Set the SUBJECTS_DIR. Default: use environment variable.
        vertex_coords: Treat overlay as a surface and write it into a 3 frame\
            parameterization.
        average_flag: Average curvature patterns a given number of times.
        normalize_flag: Normalize curvature by variance.
        frame_number: Paint the specified frame number to the output file.\
            Default: 0.
        square_root_flag: Take the square-root of the output variable.
        variance_params: Generate variance map. Requires subject name,\
            hemisphere, and field number.
        usage_flag: Print usage.
        birn_info_flag: Print BIRN-standard program information.
        help_flag: Print help message.
        diag_vertex: Invoke diagnostics for a specific vertex number.
        version_flag: Print version information.
        diag_write_flag: Write some diagnostics (DIAG_WRITE).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrispPaintOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRISP_PAINT_METADATA)
    params = mrisp_paint_params(template_file=template_file, input_surface=input_surface, output_name=output_name, subjects_dir=subjects_dir, vertex_coords=vertex_coords, average_flag=average_flag, normalize_flag=normalize_flag, frame_number=frame_number, square_root_flag=square_root_flag, variance_params=variance_params, usage_flag=usage_flag, birn_info_flag=birn_info_flag, help_flag=help_flag, diag_vertex=diag_vertex, version_flag=version_flag, diag_write_flag=diag_write_flag)
    return mrisp_paint_execute(params, execution)


__all__ = [
    "MRISP_PAINT_METADATA",
    "MrispPaintOutputs",
    "MrispPaintParameters",
    "mrisp_paint",
    "mrisp_paint_params",
]
