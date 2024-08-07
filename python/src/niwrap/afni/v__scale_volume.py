# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SCALE_VOLUME_METADATA = Metadata(
    id="b9c9ea3d721f6ffe5246ba53a763fa2d1205318c",
    name="ScaleVolume",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ScaleVolumeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scale_volume(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output scaled dataset"""


def scale_volume(
    input_dset: InputPathType,
    prefix: str,
    val_clip: list[float | int] | None = None,
    perc_clip: list[float | int] | None = None,
    scale_by_mean: bool = False,
    scale_by_median: bool = False,
    norm: bool = False,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> ScaleVolumeOutputs:
    """
    ScaleVolume by AFNI Team.
    
    A tool to scale the volume of datasets.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@ScaleVolume.html
    
    Args:
        input_dset: Dataset to scale.
        prefix: Prefix of output.
        val_clip: Min and Max of output dataset. Default V0 = 0 and V1 = 255.
        perc_clip: Set lowest P0 percentile to Min and highest P1 percentile to\
            Max. Default P0 = 2 and P1 = 98.
        scale_by_mean: Divide each sub-brick by mean of non-zero voxels.
        scale_by_median: Divide each sub-brick by median of non-zero voxels.
        norm: For each time series T, Tnorm = (T - mean(T)) / stdev(T).
        mask: Restrict to non-zero values of given mask dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ScaleVolumeOutputs`).
    """
    runner = runner or get_global_runner()
    if val_clip is not None and (len(val_clip) != 2): 
        raise ValueError(f"Length of 'val_clip' must be 2 but was {len(val_clip)}")
    if perc_clip is not None and (len(perc_clip) != 2): 
        raise ValueError(f"Length of 'perc_clip' must be 2 but was {len(perc_clip)}")
    execution = runner.start_execution(SCALE_VOLUME_METADATA)
    cargs = []
    cargs.append("@ScaleVolume")
    cargs.append("<-input")
    cargs.append("DSET>")
    cargs.append("<-prefix")
    cargs.append("PREFIX>")
    cargs.append("[-perc_clip")
    cargs.append("P0")
    cargs.append("P1]")
    cargs.append("[-val_clip")
    cargs.append("V0")
    cargs.append("V1]")
    cargs.append("[-scale_by_mean]")
    cargs.append("[-scale_by_median]")
    cargs.append("[-norm]")
    cargs.append("[-mask")
    cargs.append("MSET]")
    ret = ScaleVolumeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"<-prefix PREFIX>_scaled"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SCALE_VOLUME_METADATA",
    "ScaleVolumeOutputs",
    "scale_volume",
]
