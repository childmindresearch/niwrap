# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAP_TO_BASE_METADATA = Metadata(
    id="8c862381695fa9287f6e4158898dca7536db24a8.boutiques",
    name="map_to_base",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MapToBaseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `map_to_base(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_long_mri: OutputPathType
    """Output in base/mri directory when mapped from a longitudinal
    directory."""
    output_long_surf: OutputPathType
    """Output in base/surf directory when mapped from a longitudinal
    directory."""
    output_cross_mri: OutputPathType
    """Output in base/mri directory when mapped from a cross-sectional
    directory."""
    output_cross_surf: OutputPathType
    """Output in base/surf directory when mapped from a cross-sectional
    directory."""


def map_to_base(
    baseid: str,
    tpid: str,
    input_image: str,
    resample_type: str,
    cross: str | None = None,
    runner: Runner | None = None,
) -> MapToBaseOutputs:
    """
    Maps an image or surface from a time point directory (either cross-sectional or
    longitudinal) to the base space and outputs it in the appropriate base
    directory.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        baseid: Identifier of the base.
        tpid: Identifier of the time point, without the '.long.baseid' suffix.
        input_image: Input image, e.g., norm.mgz, aseg.mgz, lh.white.
        resample_type: Resample type. 'interpolate' for norm, T1, orig;\
            'nearest' for aseg; 'surface' for surfaces.
        cross: If '1', input is from cross sectionals; default is to use\
            longitudinal directories.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MapToBaseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAP_TO_BASE_METADATA)
    cargs = []
    cargs.append("map_to_base")
    cargs.append(baseid)
    cargs.append(tpid)
    cargs.append(input_image)
    cargs.append(resample_type)
    if cross is not None:
        cargs.append(cross)
    ret = MapToBaseOutputs(
        root=execution.output_file("."),
        output_long_mri=execution.output_file(baseid + "/mri/" + tpid + "-long." + input_image),
        output_long_surf=execution.output_file(baseid + "/surf/" + tpid + "-long." + input_image),
        output_cross_mri=execution.output_file(baseid + "/mri/" + tpid + "-cross." + input_image),
        output_cross_surf=execution.output_file(baseid + "/surf/" + tpid + "-cross." + input_image),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAP_TO_BASE_METADATA",
    "MapToBaseOutputs",
    "map_to_base",
]
