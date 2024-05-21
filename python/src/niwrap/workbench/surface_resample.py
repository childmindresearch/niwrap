# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


SURFACE_RESAMPLE_METADATA = Metadata(
    id="8c9ec436b90201a5bb8bc6d1923c86d542627afe",
    name="surface-resample",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the output surface file"""


def surface_resample(
    surface_in: InputPathType,
    current_sphere: InputPathType,
    new_sphere: InputPathType,
    method: str,
    surface_out: InputPathType,
    opt_bypass_sphere_check: bool = False,
    runner: Runner = None,
) -> SurfaceResampleOutputs:
    """
    surface-resample by Washington University School of Medicin.
    
    RESAMPLE A SURFACE TO A DIFFERENT MESH.
    
    Resamples a surface file, given two spherical surfaces that are in register.
    If ADAP_BARY_AREA is used, exactly one of -area-surfs or -area-metrics must
    be specified. This method is not generally recommended for surface
    resampling, but is provided for completeness.
    
    The BARYCENTRIC method is generally recommended for anatomical surfaces, in
    order to minimize smoothing.
    
    For cut surfaces (including flatmaps), use -surface-cut-resample.
    
    Instead of resampling a spherical surface, the
    -surface-sphere-project-unproject command is recommended.
    
    The <method> argument must be one of the following:
    
    ADAP_BARY_AREA
    BARYCENTRIC
    .
    
    Args:
        surface_in: the surface file to resample
        current_sphere: a sphere surface with the mesh that the input surface is
            currently on
        new_sphere: a sphere surface that is in register with <current-sphere>
            and has the desired output mesh
        method: the method name
        surface_out: the output surface file
        opt_bypass_sphere_check: ADVANCED: allow the current and new 'spheres'
            to have arbitrary shape as long as they follow the same contour
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SurfaceResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-resample")
    cargs.append(execution.input_file(surface_in))
    cargs.append(execution.input_file(current_sphere))
    cargs.append(execution.input_file(new_sphere))
    cargs.append(method)
    cargs.append(execution.input_file(surface_out))
    if opt_bypass_sphere_check:
        cargs.append("-bypass-sphere-check")
    ret = SurfaceResampleOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(f"{pathlib.Path(surface_out).stem}"),
    )
    execution.run(cargs)
    return ret
