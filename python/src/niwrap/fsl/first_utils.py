# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FIRST_UTILS_METADATA = Metadata(
    id="751b014c963ee8344146242e7dac5534b50bf3cd.boutiques",
    name="first_utils",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FirstUtilsParameters = typing.TypedDict('FirstUtilsParameters', {
    "__STYX_TYPE__": typing.Literal["first_utils"],
    "input_file": InputPathType,
    "output_name": str,
    "norm_factors": typing.NotRequired[InputPathType | None],
    "reference_image": typing.NotRequired[InputPathType | None],
    "extra_path": typing.NotRequired[InputPathType | None],
    "flirt_matrices": typing.NotRequired[InputPathType | None],
    "use_scale": bool,
    "dice_overlap": bool,
    "input_mesh": typing.NotRequired[InputPathType | None],
    "use_norm": bool,
    "surface_out": bool,
    "threshold": typing.NotRequired[float | None],
    "mesh_label": typing.NotRequired[str | None],
    "use_bvars": bool,
    "use_recon_mni": bool,
    "vertex_analysis": bool,
    "use_recon_native": bool,
    "use_rigid_align": bool,
    "design_matrix": typing.NotRequired[InputPathType | None],
    "recon_mesh_from_bvars": bool,
    "read_bvars": bool,
    "mesh_to_vol": bool,
    "centre_origin": bool,
    "save_vertices": typing.NotRequired[InputPathType | None],
    "verbose": bool,
    "use_pca_filter": bool,
    "num_modes": typing.NotRequired[float | None],
    "single_boundary_corr": bool,
    "do_mvglm": bool,
    "concat_bvars": bool,
    "debug_mode": bool,
    "help": bool,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "first_utils": first_utils_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {}
    return vt.get(t)


class FirstUtilsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `first_utils(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def first_utils_params(
    input_file: InputPathType,
    output_name: str,
    norm_factors: InputPathType | None = None,
    reference_image: InputPathType | None = None,
    extra_path: InputPathType | None = None,
    flirt_matrices: InputPathType | None = None,
    use_scale: bool = False,
    dice_overlap: bool = False,
    input_mesh: InputPathType | None = None,
    use_norm: bool = False,
    surface_out: bool = False,
    threshold: float | None = None,
    mesh_label: str | None = None,
    use_bvars: bool = False,
    use_recon_mni: bool = False,
    vertex_analysis: bool = False,
    use_recon_native: bool = False,
    use_rigid_align: bool = False,
    design_matrix: InputPathType | None = None,
    recon_mesh_from_bvars: bool = False,
    read_bvars: bool = False,
    mesh_to_vol: bool = False,
    centre_origin: bool = False,
    save_vertices: InputPathType | None = None,
    verbose: bool = False,
    use_pca_filter: bool = False,
    num_modes: float | None = None,
    single_boundary_corr: bool = False,
    do_mvglm: bool = False,
    concat_bvars: bool = False,
    debug_mode: bool = False,
    help_: bool = False,
) -> FirstUtilsParameters:
    """
    Build parameters.
    
    Args:
        input_file: Filename of input image/mesh/bvars.
        output_name: Output name.
        norm_factors: Filename of normalization factors.
        reference_image: Filename of reference image.
        extra_path: Specifies extra path to image in .bvars file.
        flirt_matrices: Text file containing filenames of flirt matrices.
        use_scale: Do stats.
        dice_overlap: Calculates Dice overlap.
        input_mesh: Filename of input mesh.
        use_norm: Normalize volumes measurements.
        surface_out: Output vertex analysis on the surface.
        threshold: Threshold for clean up.
        mesh_label: Specifies the label used to fill the mesh.
        use_bvars: Operate using the mode parameters output from FIRST.
        use_recon_mni: Reconstruct meshes in MNI space.
        vertex_analysis: Perform vertex-wise stats from bvars.
        use_recon_native: Reconstruct meshes in native space.
        use_rigid_align: Register meshes using 6 degree of freedom (7 if\
            useScale is used).
        design_matrix: Filename of fsl design matrix.
        recon_mesh_from_bvars: Convert bvars to mesh.
        read_bvars: Read bvars from binary format.
        mesh_to_vol: Convert mesh to an image.
        centre_origin: Places origin of mesh at the centre of the image.
        save_vertices: Filename for saving matrix of vertex coords: (all x,\
            then all y, then all z) by Nsubjects.
        verbose: Output F-stats to standard out.
        use_pca_filter: Smooths the surface by truncating the mode parameters.
        num_modes: Number of modes to retain per structure.
        single_boundary_corr: Correct boundary voxels of a single structure.
        do_mvglm: Perform multivariate general linear model analysis.
        concat_bvars: Concat bvars from binary format.
        debug_mode: Turn on debugging mode.
        help_: Display help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "first_utils",
        "input_file": input_file,
        "output_name": output_name,
        "use_scale": use_scale,
        "dice_overlap": dice_overlap,
        "use_norm": use_norm,
        "surface_out": surface_out,
        "use_bvars": use_bvars,
        "use_recon_mni": use_recon_mni,
        "vertex_analysis": vertex_analysis,
        "use_recon_native": use_recon_native,
        "use_rigid_align": use_rigid_align,
        "recon_mesh_from_bvars": recon_mesh_from_bvars,
        "read_bvars": read_bvars,
        "mesh_to_vol": mesh_to_vol,
        "centre_origin": centre_origin,
        "verbose": verbose,
        "use_pca_filter": use_pca_filter,
        "single_boundary_corr": single_boundary_corr,
        "do_mvglm": do_mvglm,
        "concat_bvars": concat_bvars,
        "debug_mode": debug_mode,
        "help": help_,
    }
    if norm_factors is not None:
        params["norm_factors"] = norm_factors
    if reference_image is not None:
        params["reference_image"] = reference_image
    if extra_path is not None:
        params["extra_path"] = extra_path
    if flirt_matrices is not None:
        params["flirt_matrices"] = flirt_matrices
    if input_mesh is not None:
        params["input_mesh"] = input_mesh
    if threshold is not None:
        params["threshold"] = threshold
    if mesh_label is not None:
        params["mesh_label"] = mesh_label
    if design_matrix is not None:
        params["design_matrix"] = design_matrix
    if save_vertices is not None:
        params["save_vertices"] = save_vertices
    if num_modes is not None:
        params["num_modes"] = num_modes
    return params


def first_utils_cargs(
    params: FirstUtilsParameters,
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
    cargs.append("first_utils")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_file"))
    ])
    cargs.extend([
        "-o",
        params.get("output_name")
    ])
    if params.get("norm_factors") is not None:
        cargs.extend([
            "-g",
            execution.input_file(params.get("norm_factors"))
        ])
    if params.get("reference_image") is not None:
        cargs.extend([
            "-r",
            execution.input_file(params.get("reference_image"))
        ])
    if params.get("extra_path") is not None:
        cargs.extend([
            "-a",
            execution.input_file(params.get("extra_path"))
        ])
    if params.get("flirt_matrices") is not None:
        cargs.extend([
            "-f",
            execution.input_file(params.get("flirt_matrices"))
        ])
    if params.get("use_scale"):
        cargs.append("--useScale")
    if params.get("dice_overlap"):
        cargs.append("--overlap")
    if params.get("input_mesh") is not None:
        cargs.extend([
            "-m",
            execution.input_file(params.get("input_mesh"))
        ])
    if params.get("use_norm"):
        cargs.append("--useNorm")
    if params.get("surface_out"):
        cargs.append("--surfaceout")
    if params.get("threshold") is not None:
        cargs.extend([
            "-p",
            str(params.get("threshold"))
        ])
    if params.get("mesh_label") is not None:
        cargs.extend([
            "-l",
            params.get("mesh_label")
        ])
    if params.get("use_bvars"):
        cargs.append("--usebvars")
    if params.get("use_recon_mni"):
        cargs.append("--useReconMNI")
    if params.get("vertex_analysis"):
        cargs.append("--vertexAnalysis")
    if params.get("use_recon_native"):
        cargs.append("--useReconNative")
    if params.get("use_rigid_align"):
        cargs.append("--useRigidAlign")
    if params.get("design_matrix") is not None:
        cargs.extend([
            "-d",
            execution.input_file(params.get("design_matrix"))
        ])
    if params.get("recon_mesh_from_bvars"):
        cargs.append("--reconMeshFromBvars")
    if params.get("read_bvars"):
        cargs.append("--readBvars")
    if params.get("mesh_to_vol"):
        cargs.append("--meshToVol")
    if params.get("centre_origin"):
        cargs.append("--centreOrigin")
    if params.get("save_vertices") is not None:
        cargs.extend([
            "--saveVertices",
            execution.input_file(params.get("save_vertices"))
        ])
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("use_pca_filter"):
        cargs.append("--usePCAfilter")
    if params.get("num_modes") is not None:
        cargs.extend([
            "-n",
            str(params.get("num_modes"))
        ])
    if params.get("single_boundary_corr"):
        cargs.append("--singleBoundaryCorr")
    if params.get("do_mvglm"):
        cargs.append("--doMVGLM")
    if params.get("concat_bvars"):
        cargs.append("--concatBvars")
    if params.get("debug_mode"):
        cargs.append("--debug")
    if params.get("help"):
        cargs.append("-h")
    return cargs


def first_utils_outputs(
    params: FirstUtilsParameters,
    execution: Execution,
) -> FirstUtilsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FirstUtilsOutputs(
        root=execution.output_file("."),
    )
    return ret


def first_utils_execute(
    params: FirstUtilsParameters,
    execution: Execution,
) -> FirstUtilsOutputs:
    """
    Utilities for handling FIRST's input and output files.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FirstUtilsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = first_utils_cargs(params, execution)
    ret = first_utils_outputs(params, execution)
    execution.run(cargs)
    return ret


def first_utils(
    input_file: InputPathType,
    output_name: str,
    norm_factors: InputPathType | None = None,
    reference_image: InputPathType | None = None,
    extra_path: InputPathType | None = None,
    flirt_matrices: InputPathType | None = None,
    use_scale: bool = False,
    dice_overlap: bool = False,
    input_mesh: InputPathType | None = None,
    use_norm: bool = False,
    surface_out: bool = False,
    threshold: float | None = None,
    mesh_label: str | None = None,
    use_bvars: bool = False,
    use_recon_mni: bool = False,
    vertex_analysis: bool = False,
    use_recon_native: bool = False,
    use_rigid_align: bool = False,
    design_matrix: InputPathType | None = None,
    recon_mesh_from_bvars: bool = False,
    read_bvars: bool = False,
    mesh_to_vol: bool = False,
    centre_origin: bool = False,
    save_vertices: InputPathType | None = None,
    verbose: bool = False,
    use_pca_filter: bool = False,
    num_modes: float | None = None,
    single_boundary_corr: bool = False,
    do_mvglm: bool = False,
    concat_bvars: bool = False,
    debug_mode: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> FirstUtilsOutputs:
    """
    Utilities for handling FIRST's input and output files.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Filename of input image/mesh/bvars.
        output_name: Output name.
        norm_factors: Filename of normalization factors.
        reference_image: Filename of reference image.
        extra_path: Specifies extra path to image in .bvars file.
        flirt_matrices: Text file containing filenames of flirt matrices.
        use_scale: Do stats.
        dice_overlap: Calculates Dice overlap.
        input_mesh: Filename of input mesh.
        use_norm: Normalize volumes measurements.
        surface_out: Output vertex analysis on the surface.
        threshold: Threshold for clean up.
        mesh_label: Specifies the label used to fill the mesh.
        use_bvars: Operate using the mode parameters output from FIRST.
        use_recon_mni: Reconstruct meshes in MNI space.
        vertex_analysis: Perform vertex-wise stats from bvars.
        use_recon_native: Reconstruct meshes in native space.
        use_rigid_align: Register meshes using 6 degree of freedom (7 if\
            useScale is used).
        design_matrix: Filename of fsl design matrix.
        recon_mesh_from_bvars: Convert bvars to mesh.
        read_bvars: Read bvars from binary format.
        mesh_to_vol: Convert mesh to an image.
        centre_origin: Places origin of mesh at the centre of the image.
        save_vertices: Filename for saving matrix of vertex coords: (all x,\
            then all y, then all z) by Nsubjects.
        verbose: Output F-stats to standard out.
        use_pca_filter: Smooths the surface by truncating the mode parameters.
        num_modes: Number of modes to retain per structure.
        single_boundary_corr: Correct boundary voxels of a single structure.
        do_mvglm: Perform multivariate general linear model analysis.
        concat_bvars: Concat bvars from binary format.
        debug_mode: Turn on debugging mode.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FirstUtilsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIRST_UTILS_METADATA)
    params = first_utils_params(input_file=input_file, output_name=output_name, norm_factors=norm_factors, reference_image=reference_image, extra_path=extra_path, flirt_matrices=flirt_matrices, use_scale=use_scale, dice_overlap=dice_overlap, input_mesh=input_mesh, use_norm=use_norm, surface_out=surface_out, threshold=threshold, mesh_label=mesh_label, use_bvars=use_bvars, use_recon_mni=use_recon_mni, vertex_analysis=vertex_analysis, use_recon_native=use_recon_native, use_rigid_align=use_rigid_align, design_matrix=design_matrix, recon_mesh_from_bvars=recon_mesh_from_bvars, read_bvars=read_bvars, mesh_to_vol=mesh_to_vol, centre_origin=centre_origin, save_vertices=save_vertices, verbose=verbose, use_pca_filter=use_pca_filter, num_modes=num_modes, single_boundary_corr=single_boundary_corr, do_mvglm=do_mvglm, concat_bvars=concat_bvars, debug_mode=debug_mode, help_=help_)
    return first_utils_execute(params, execution)


__all__ = [
    "FIRST_UTILS_METADATA",
    "FirstUtilsOutputs",
    "FirstUtilsParameters",
    "first_utils",
    "first_utils_params",
]
