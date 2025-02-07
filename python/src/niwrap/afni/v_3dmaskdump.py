# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DMASKDUMP_METADATA = Metadata(
    id="9cb4c849a9357c37ec67fbe234f23f59f3a3a158.boutiques",
    name="3dmaskdump",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dmaskdumpParameters = typing.TypedDict('V3dmaskdumpParameters', {
    "__STYX_TYPE__": typing.Literal["3dmaskdump"],
    "input_files": list[InputPathType],
    "mask_dataset": typing.NotRequired[InputPathType | None],
    "mask_range": typing.NotRequired[list[str] | None],
    "output_index": bool,
    "output_noijk": bool,
    "output_xyz": bool,
    "output_filename": typing.NotRequired[str | None],
    "calc_mask_opts": typing.NotRequired[str | None],
    "xbox_coords": typing.NotRequired[str | None],
    "dbox_coords": typing.NotRequired[str | None],
    "nbox_coords": typing.NotRequired[str | None],
    "ibox_coords": typing.NotRequired[str | None],
    "xball_coords": typing.NotRequired[str | None],
    "dball_coords": typing.NotRequired[str | None],
    "nball_coords": typing.NotRequired[str | None],
    "nozero_output": bool,
    "random_voxels": typing.NotRequired[float | None],
    "random_seed": typing.NotRequired[float | None],
    "output_niml": typing.NotRequired[str | None],
    "quiet_mode": bool,
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
        "3dmaskdump": v_3dmaskdump_cargs,
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
        "3dmaskdump": v_3dmaskdump_outputs,
    }.get(t)


class V3dmaskdumpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dmaskdump(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Output ASCII file with voxel values"""


def v_3dmaskdump_params(
    input_files: list[InputPathType],
    mask_dataset: InputPathType | None = None,
    mask_range: list[str] | None = None,
    output_index: bool = False,
    output_noijk: bool = False,
    output_xyz: bool = False,
    output_filename: str | None = None,
    calc_mask_opts: str | None = None,
    xbox_coords: str | None = None,
    dbox_coords: str | None = None,
    nbox_coords: str | None = None,
    ibox_coords: str | None = None,
    xball_coords: str | None = None,
    dball_coords: str | None = None,
    nball_coords: str | None = None,
    nozero_output: bool = False,
    random_voxels: float | None = None,
    random_seed: float | None = None,
    output_niml: str | None = None,
    quiet_mode: bool = False,
) -> V3dmaskdumpParameters:
    """
    Build parameters.
    
    Args:
        input_files: Input datasets to dump voxel values.
        mask_dataset: Use the dataset as a mask. Only voxels with nonzero\
            values in the mask will be printed from the input dataset.
        mask_range: Further restrict the voxels from mask dataset to those mask\
            values between 'a' and 'b' (inclusive).
        output_index: Write out the dataset index values.
        output_noijk: Do not write out the i,j,k values.
        output_xyz: Write the x,y,z coordinates from the first input dataset at\
            the start of each output line.
        output_filename: Write output to specified file.
        calc_mask_opts: Execute options enclosed as a 3dcalc-like program to\
            produce a mask from the resulting 3D brick.
        xbox_coords: Put a 'mask' at dataset coordinates 'x y z' mm.
        dbox_coords: Put a 'mask' at RAI/DICOM coordinates of 'x y z' mm.
        nbox_coords: Put a 'mask' at LPI/SPM coordinates of 'x y z' mm.
        ibox_coords: Put a 'mask' at voxel indexes 'i j k'.
        xball_coords: Put a ball (sphere) mask at dataset coordinates (x,y,z)\
            with radius r.
        dball_coords: Put a ball (sphere) mask at RAI/DICOM coordinates (x,y,z)\
            with radius r.
        nball_coords: Put a ball (sphere) mask at LPI/SPM coordinates (x,y,z)\
            with radius r.
        nozero_output: Skip output of any voxel where all the data values are\
            zero.
        random_voxels: Keep only N_RAND randomly selected voxels from what\
            would have been the output.
        random_seed: Seed the random number generator with SEED.
        output_niml: Output data in the XML/NIML format compatible with input\
            back to AFNI via the READ_NIML_FILE command.
        quiet_mode: Do not print progress messages to stderr.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dmaskdump",
        "input_files": input_files,
        "output_index": output_index,
        "output_noijk": output_noijk,
        "output_xyz": output_xyz,
        "nozero_output": nozero_output,
        "quiet_mode": quiet_mode,
    }
    if mask_dataset is not None:
        params["mask_dataset"] = mask_dataset
    if mask_range is not None:
        params["mask_range"] = mask_range
    if output_filename is not None:
        params["output_filename"] = output_filename
    if calc_mask_opts is not None:
        params["calc_mask_opts"] = calc_mask_opts
    if xbox_coords is not None:
        params["xbox_coords"] = xbox_coords
    if dbox_coords is not None:
        params["dbox_coords"] = dbox_coords
    if nbox_coords is not None:
        params["nbox_coords"] = nbox_coords
    if ibox_coords is not None:
        params["ibox_coords"] = ibox_coords
    if xball_coords is not None:
        params["xball_coords"] = xball_coords
    if dball_coords is not None:
        params["dball_coords"] = dball_coords
    if nball_coords is not None:
        params["nball_coords"] = nball_coords
    if random_voxels is not None:
        params["random_voxels"] = random_voxels
    if random_seed is not None:
        params["random_seed"] = random_seed
    if output_niml is not None:
        params["output_niml"] = output_niml
    return params


def v_3dmaskdump_cargs(
    params: V3dmaskdumpParameters,
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
    cargs.append("3dmaskdump")
    cargs.extend([execution.input_file(f) for f in params.get("input_files")])
    if params.get("mask_dataset") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_dataset"))
        ])
    if params.get("mask_range") is not None:
        cargs.extend([
            "-mrange",
            *params.get("mask_range")
        ])
    if params.get("output_index"):
        cargs.append("-index")
    if params.get("output_noijk"):
        cargs.append("-noijk")
    if params.get("output_xyz"):
        cargs.append("-xyz")
    if params.get("output_filename") is not None:
        cargs.extend([
            "-o",
            params.get("output_filename")
        ])
    if params.get("calc_mask_opts") is not None:
        cargs.extend([
            "-cmask",
            params.get("calc_mask_opts")
        ])
    if params.get("xbox_coords") is not None:
        cargs.extend([
            "-xbox",
            params.get("xbox_coords")
        ])
    if params.get("dbox_coords") is not None:
        cargs.extend([
            "-dbox",
            params.get("dbox_coords")
        ])
    if params.get("nbox_coords") is not None:
        cargs.extend([
            "-nbox",
            params.get("nbox_coords")
        ])
    if params.get("ibox_coords") is not None:
        cargs.extend([
            "-ibox",
            params.get("ibox_coords")
        ])
    if params.get("xball_coords") is not None:
        cargs.extend([
            "-xball",
            params.get("xball_coords")
        ])
    if params.get("dball_coords") is not None:
        cargs.extend([
            "-dball",
            params.get("dball_coords")
        ])
    if params.get("nball_coords") is not None:
        cargs.extend([
            "-nball",
            params.get("nball_coords")
        ])
    if params.get("nozero_output"):
        cargs.append("-nozero")
    if params.get("random_voxels") is not None:
        cargs.extend([
            "-n_rand",
            str(params.get("random_voxels"))
        ])
    if params.get("random_seed") is not None:
        cargs.extend([
            "-n_randseed",
            str(params.get("random_seed"))
        ])
    if params.get("output_niml") is not None:
        cargs.extend([
            "-niml",
            params.get("output_niml")
        ])
    if params.get("quiet_mode"):
        cargs.append("-quiet")
    return cargs


def v_3dmaskdump_outputs(
    params: V3dmaskdumpParameters,
    execution: Execution,
) -> V3dmaskdumpOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dmaskdumpOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_filename")) if (params.get("output_filename") is not None) else None,
    )
    return ret


def v_3dmaskdump_execute(
    params: V3dmaskdumpParameters,
    execution: Execution,
) -> V3dmaskdumpOutputs:
    """
    Outputs voxel values from AFNI datasets satisfying mask criteria to an ASCII
    file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dmaskdumpOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3dmaskdump_cargs(params, execution)
    ret = v_3dmaskdump_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dmaskdump(
    input_files: list[InputPathType],
    mask_dataset: InputPathType | None = None,
    mask_range: list[str] | None = None,
    output_index: bool = False,
    output_noijk: bool = False,
    output_xyz: bool = False,
    output_filename: str | None = None,
    calc_mask_opts: str | None = None,
    xbox_coords: str | None = None,
    dbox_coords: str | None = None,
    nbox_coords: str | None = None,
    ibox_coords: str | None = None,
    xball_coords: str | None = None,
    dball_coords: str | None = None,
    nball_coords: str | None = None,
    nozero_output: bool = False,
    random_voxels: float | None = None,
    random_seed: float | None = None,
    output_niml: str | None = None,
    quiet_mode: bool = False,
    runner: Runner | None = None,
) -> V3dmaskdumpOutputs:
    """
    Outputs voxel values from AFNI datasets satisfying mask criteria to an ASCII
    file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input datasets to dump voxel values.
        mask_dataset: Use the dataset as a mask. Only voxels with nonzero\
            values in the mask will be printed from the input dataset.
        mask_range: Further restrict the voxels from mask dataset to those mask\
            values between 'a' and 'b' (inclusive).
        output_index: Write out the dataset index values.
        output_noijk: Do not write out the i,j,k values.
        output_xyz: Write the x,y,z coordinates from the first input dataset at\
            the start of each output line.
        output_filename: Write output to specified file.
        calc_mask_opts: Execute options enclosed as a 3dcalc-like program to\
            produce a mask from the resulting 3D brick.
        xbox_coords: Put a 'mask' at dataset coordinates 'x y z' mm.
        dbox_coords: Put a 'mask' at RAI/DICOM coordinates of 'x y z' mm.
        nbox_coords: Put a 'mask' at LPI/SPM coordinates of 'x y z' mm.
        ibox_coords: Put a 'mask' at voxel indexes 'i j k'.
        xball_coords: Put a ball (sphere) mask at dataset coordinates (x,y,z)\
            with radius r.
        dball_coords: Put a ball (sphere) mask at RAI/DICOM coordinates (x,y,z)\
            with radius r.
        nball_coords: Put a ball (sphere) mask at LPI/SPM coordinates (x,y,z)\
            with radius r.
        nozero_output: Skip output of any voxel where all the data values are\
            zero.
        random_voxels: Keep only N_RAND randomly selected voxels from what\
            would have been the output.
        random_seed: Seed the random number generator with SEED.
        output_niml: Output data in the XML/NIML format compatible with input\
            back to AFNI via the READ_NIML_FILE command.
        quiet_mode: Do not print progress messages to stderr.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dmaskdumpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DMASKDUMP_METADATA)
    params = v_3dmaskdump_params(input_files=input_files, mask_dataset=mask_dataset, mask_range=mask_range, output_index=output_index, output_noijk=output_noijk, output_xyz=output_xyz, output_filename=output_filename, calc_mask_opts=calc_mask_opts, xbox_coords=xbox_coords, dbox_coords=dbox_coords, nbox_coords=nbox_coords, ibox_coords=ibox_coords, xball_coords=xball_coords, dball_coords=dball_coords, nball_coords=nball_coords, nozero_output=nozero_output, random_voxels=random_voxels, random_seed=random_seed, output_niml=output_niml, quiet_mode=quiet_mode)
    return v_3dmaskdump_execute(params, execution)


__all__ = [
    "V3dmaskdumpOutputs",
    "V3dmaskdumpParameters",
    "V_3DMASKDUMP_METADATA",
    "v_3dmaskdump",
    "v_3dmaskdump_params",
]
