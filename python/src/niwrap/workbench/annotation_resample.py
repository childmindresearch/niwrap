# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

ANNOTATION_RESAMPLE_METADATA = Metadata(
    id="004ad055b2d3072224ec7561cee0be5f53d98235",
    name="annotation-resample",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class AnnotationResampleSurfacePair:
    """
    pair of surfaces for resampling surface annotations for one structure
    """
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        return cargs


class AnnotationResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `annotation_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def annotation_resample(
    annotation_in: InputPathType,
    annotation_out: str,
    surface_pair: list[AnnotationResampleSurfacePair] = None,
    runner: Runner = None,
) -> AnnotationResampleOutputs:
    """
    annotation-resample by Washington University School of Medicin.
    
    Resample an annotation file to different meshes.
    
    Resample an annotation file from the source mesh to the target mesh.
    
    Only annotations in surface space are modified, no changes are made to
    annotations in other spaces. The -surface-pair option may be repeated for
    additional structures used by surface space annotations.
    
    Args:
        annotation_in: the annotation file to resample.
        annotation_out: name of resampled annotation file.
        surface_pair: pair of surfaces for resampling surface annotations for\
            one structure.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AnnotationResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANNOTATION_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-annotation-resample")
    cargs.append(execution.input_file(annotation_in))
    cargs.append(annotation_out)
    if surface_pair is not None:
        cargs.extend(["-surface-pair", *[a for c in [s.run(execution) for s in surface_pair] for a in c]])
    ret = AnnotationResampleOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANNOTATION_RESAMPLE_METADATA",
    "AnnotationResampleOutputs",
    "AnnotationResampleSurfacePair",
    "annotation_resample",
]