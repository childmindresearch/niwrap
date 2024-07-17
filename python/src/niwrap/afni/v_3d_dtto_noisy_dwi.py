# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_DTTO_NOISY_DWI_METADATA = Metadata(
    id="5e13dfd3027b3c2b8e1845ee32671c96b40a92b6",
    name="3dDTtoNoisyDWI",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dDttoNoisyDwiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_dtto_noisy_dwi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dwi: OutputPathType
    """Synthetic set of DWI measures with noise. Contains N+1 bricks mimicking B0+DWI data."""


def v_3d_dtto_noisy_dwi(
    dt_file: InputPathType,
    grad_file: InputPathType,
    noise_dwi: float | int,
    prefix: str,
    noise_b0: float | int | None = None,
    mask: InputPathType | None = None,
    bval: float | int | None = None,
    s0: float | int | None = None,
    runner: Runner | None = None,
) -> V3dDttoNoisyDwiOutputs:
    """
    3dDTtoNoisyDWI by AFNI Team.
    
    Generate a synthetic set of DWI measures with a given SNR from an AFNI-style
    DT file and a set of gradients. This can be useful for simulations and
    testing.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dDTtoNoisyDWI.html
    
    Args:
        dt_file: Diffusion tensor file with six bricks of DT components ordered\
            in the AFNI manner: Dxx,Dxy,Dyy,Dxz,Dyz,Dzz.
        grad_file: Text file of gradients arranged in three columns. There\
            should be no row of all zeros representing the b=0 line.
        noise_dwi: Fractional value of noise in DWIs. FF = sigma/S0 = 1/SNR0.\
            For example, FF=0.05 corresponds to SNR0=20.
        prefix: Output file name prefix. Will have N+1 bricks when GRADFILE has\
            N rows of gradients.
        noise_b0: Optional fraction of Rician noise in the b=0 reference image.\
            If not provided, FF2=FF.
        mask: Optional mask within which to calculate uncertainty. Data should\
            be masked already otherwise.
        bval: Optional DW factor to use if DT values are scaled to something\
            physical. Default is BB=1.
        s0: Optional reference b=0 signal strength. Default value is SS=1000.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDttoNoisyDwiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DTTO_NOISY_DWI_METADATA)
    cargs = []
    cargs.append("3dDTtoNoisyDWI")
    cargs.append(execution.input_file(dt_file))
    cargs.append(execution.input_file(grad_file))
    cargs.extend(["-noise_DWI", str(noise_dwi)])
    if noise_b0 is not None:
        cargs.extend(["-noise_B0", str(noise_b0)])
    cargs.extend(["-prefix", prefix])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if bval is not None:
        cargs.extend(["-bval", str(bval)])
    if s0 is not None:
        cargs.extend(["-S0", str(s0)])
    ret = V3dDttoNoisyDwiOutputs(
        root=execution.output_file("."),
        output_dwi=execution.output_file(f"{prefix}+orig"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dDttoNoisyDwiOutputs",
    "V_3D_DTTO_NOISY_DWI_METADATA",
    "v_3d_dtto_noisy_dwi",
]
