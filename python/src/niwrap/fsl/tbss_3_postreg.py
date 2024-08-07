# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

TBSS_3_POSTREG_METADATA = Metadata(
    id="3c5334c9ce8b20040564096b7966a15d4acc10dc",
    name="tbss_3_postreg",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class Tbss3PostregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_3_postreg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tbss_3_postreg(
    derive_mean_from_study: bool = False,
    use_fmrib58: bool = False,
    runner: Runner | None = None,
) -> Tbss3PostregOutputs:
    """
    tbss_3_postreg by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    TBSS post-registration processing.
    
    More information:
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/TBSS/UserGuide#tbss_3_postreg
    
    Args:
        derive_mean_from_study: Derive mean_FA and mean_FA_skeleton from mean\
            of all subjects in study (recommended).
        use_fmrib58: Use FMRIB58_FA and its skeleton instead of study-derived\
            mean and skeleton.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tbss3PostregOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        derive_mean_from_study +
        use_fmrib58
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "derive_mean_from_study,\n"
            "use_fmrib58"
        )
    execution = runner.start_execution(TBSS_3_POSTREG_METADATA)
    cargs = []
    cargs.append("tbss_3_postreg")
    cargs.append("[OPTIONS]")
    ret = Tbss3PostregOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TBSS_3_POSTREG_METADATA",
    "Tbss3PostregOutputs",
    "tbss_3_postreg",
]
