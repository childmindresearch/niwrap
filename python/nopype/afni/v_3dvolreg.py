# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.610744

import typing

from ..styxdefs import *


V_3DVOLREG_METADATA = Metadata(
    id="a339444ae3607862ba884b4b742c84ec36053226",
    name="3dvolreg",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dvolregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dvolreg(...)`.
    """
    md1d_file: OutputPathType
    """Max displacement output file."""
    oned_file: OutputPathType
    """1d movement parameters output file."""
    oned_matrix_save: OutputPathType
    """Save the matrix transformation."""
    out_file: OutputPathType
    """Output image file name."""
    md1d_file_: OutputPathType
    """Max displacement info file."""
    oned_file_: OutputPathType
    """Movement parameters info file."""
    oned_matrix_save_: OutputPathType
    """Matrix transformation from base to input."""
    out_file_: OutputPathType
    """Registered file."""


def v_3dvolreg(
    runner: Runner,
    in_file: InputPathType,
    basefile: InputPathType | None = None,
    copyorigin: bool = False,
    in_weight_volume: list[str] = None,
    in_weight_volume_2: InputPathType | None = None,
    interp: typing.Literal["Fourier", "cubic", "heptic", "quintic", "linear"] | None = None,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    timeshift: bool = False,
    verbose: bool = False,
    zpad: int | None = None,
) -> V3dvolregOutputs:
    """
    Volreg, as implemented in Nipype (module: nipype.interfaces.afni.preprocess,
    interface: Volreg).
    Register input volumes to a base volume using AFNI 3dvolreg command
    For complete details, see the `3dvolreg Documentation.
    <https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dvolreg.html>`_
    
    Args:
        runner: Command runner
        in_file: Input file to 3dvolreg.
        basefile: Base file for registration.
        copyorigin: Copy base file origin coords to output.
        in_weight_volume: (file or string, an integer) or file or string.
            Weights for each voxel specified by a file with an optional volume
            number (defaults to 0).
        in_weight_volume_2: (file or string, an integer) or file or string.
            Weights for each voxel specified by a file with an optional volume
            number (defaults to 0).
        interp: 'fourier' or 'cubic' or 'heptic' or 'quintic' or 'linear'.
            Spatial interpolation methods [default = heptic].
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        timeshift: Time shift to mean slice time offset.
        verbose: More detailed description of the process.
        zpad: Zeropad around the edges by 'n' voxels during rotations.
    Returns:
        NamedTuple of outputs (described in `V3dvolregOutputs`).
    """
    if (
        (in_weight_volume is not None) +
        (in_weight_volume_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "in_weight_volume,\n"
            "in_weight_volume_2"
        )
    execution = runner.start_execution(V_3DVOLREG_METADATA)
    cargs = []
    cargs.append("3dvolreg")
    if basefile is not None:
        cargs.extend(["-base", execution.input_file(basefile)])
    if zpad is not None:
        cargs.extend(["-zpad", str(zpad)])
    cargs.append("[MD1D_FILE]")
    cargs.append(execution.input_file(in_file))
    cargs.append("[ARGS]")
    if copyorigin:
        cargs.append("-twodup")
    cargs.append("[ENVIRON]")
    if in_weight_volume_2 is not None:
        cargs.extend(["-weight '", execution.input_file(in_weight_volume_2)])
    if interp is not None:
        cargs.extend(["-", interp])
    if num_threads is not None:
        cargs.append(str(num_threads))
    cargs.append("[ONED_FILE]")
    cargs.append("[ONED_MATRIX_SAVE]")
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    if timeshift:
        cargs.append("-tshift 0")
    if verbose:
        cargs.append("-verbose")
    ret = V3dvolregOutputs(
        md1d_file=execution.output_file(f"{in_file}_md.1D", optional=True),
        oned_file=execution.output_file(f"{in_file}.1D", optional=True),
        oned_matrix_save=execution.output_file(f"{in_file}.aff12.1D", optional=True),
        out_file=execution.output_file(f"{in_file}_volreg", optional=True),
        md1d_file_=execution.output_file(f"md1d_file", optional=True),
        oned_file_=execution.output_file(f"oned_file", optional=True),
        oned_matrix_save_=execution.output_file(f"oned_matrix_save", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret
