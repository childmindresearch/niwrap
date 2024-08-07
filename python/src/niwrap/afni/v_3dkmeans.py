# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DKMEANS_METADATA = Metadata(
    id="82051ad50367309d63f1f638a14edc23645b7da6",
    name="3dkmeans",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dkmeansOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dkmeans(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cluster_membership: OutputPathType | None
    """Output volume for the cluster membership."""
    cluster_distance: OutputPathType | None
    """Output volume for the cluster distance measures."""
    distances_text_file: OutputPathType
    """Output text file containing distances between clusters."""
    centroids_text_file: OutputPathType
    """Output text file containing cluster centroids."""
    within_cluster_sum_text_file: OutputPathType
    """Output text file containing within cluster sum of distances."""
    max_distance_text_file: OutputPathType
    """Output text file containing maximum distance within each cluster."""
    voxel_distance_to_centroid: OutputPathType
    """Output text file containing distance from voxel to its centroid."""


def v_3dkmeans(
    input_: list[InputPathType],
    version: bool = False,
    mask: InputPathType | None = None,
    mask_range: list[float | int] | None = None,
    cmask: str | None = None,
    jobname: str | None = None,
    prefix: str | None = None,
    distance_measure: float | int | None = None,
    num_clusters: float | int | None = None,
    remap_method: str | None = None,
    labeltable: InputPathType | None = None,
    clabels: list[str] | None = None,
    clust_init: InputPathType | None = None,
    num_repeats: float | int | None = None,
    rsigs: InputPathType | None = None,
    verbose: bool = False,
    write_dists: bool = False,
    voxdbg: list[float | int] | None = None,
    seed: float | int | None = None,
    runner: Runner | None = None,
) -> V3dkmeansOutputs:
    """
    3dkmeans by AFNI Team.
    
    3d+t Clustering segmentation based on The C clustering library.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dkmeans.html
    
    Args:
        input_: Input data to be clustered. You can specify multiple filenames\
            in sequence and they will be concatenated internally.
        version: Description missing.
        mask: Dataset to be used as a mask; only voxels with nonzero values in\
            'mset' will be used.
        mask_range: Restrict the voxels from 'mset' to only those mask values\
            between 'a' and 'b' (inclusive).
        cmask: Execute the options enclosed in single quotes as a 3dcalc-like\
            program to produce a mask from the resulting 3D brick.
        jobname: Specify a different name for the output files. Default is\
            derived from the input file name.
        prefix: Specify a prefix for the output volumes. Default is the same as\
            jobname.
        distance_measure: Specifies distance measure for clustering. Supported\
            values: 0 (No clustering), 1 (Uncentered correlation distance), 2\
            (Pearson distance), 3 (Uncentered correlation distance, absolute\
            value), 4 (Pearson distance, absolute value), 5 (Spearman's rank\
            distance), 6 (Kendall's distance), 7 (Euclidean distance), 8\
            (City-block distance).
        num_clusters: Specify number of clusters.
        remap_method: Reassign clusters numbers based on METHOD: NONE\
            (default), COUNT, iCOUNT, MAG, iMAG.
        labeltable: Attach labeltable to clustering output.
        clabels: Provide a label for each cluster. Labels cannot start with\
            '-'.
        clust_init: Specify a dataset to initialize clustering. If provided,\
            sets -r 0.
        num_repeats: Number of times the k-means clustering algorithm is run.
        rsigs: Calculate distances from each voxel's signature to the\
            signatures in this multi-column file. No clustering done.
        verbose: Enable verbose mode.
        write_dists: Output text files containing various distance measures.
        voxdbg: Output debugging info for specified voxel (I J K).
        seed: Seed for the random number generator. Default is 1234567.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dkmeansOutputs`).
    """
    runner = runner or get_global_runner()
    if mask_range is not None and (len(mask_range) != 2): 
        raise ValueError(f"Length of 'mask_range' must be 2 but was {len(mask_range)}")
    if voxdbg is not None and (len(voxdbg) != 3): 
        raise ValueError(f"Length of 'voxdbg' must be 3 but was {len(voxdbg)}")
    execution = runner.start_execution(V_3DKMEANS_METADATA)
    cargs = []
    cargs.append("3dkmeans")
    cargs.append("[OPTIONS]")
    ret = V3dkmeansOutputs(
        root=execution.output_file("."),
        cluster_membership=execution.output_file(f"{jobname}_membership.nii.gz", optional=True) if jobname is not None else None,
        cluster_distance=execution.output_file(f"{jobname}_distance.nii.gz", optional=True) if jobname is not None else None,
        distances_text_file=execution.output_file(f"FILE.dis.1D", optional=True),
        centroids_text_file=execution.output_file(f"FILE.cen.1D", optional=True),
        within_cluster_sum_text_file=execution.output_file(f"FILE.info1.1D", optional=True),
        max_distance_text_file=execution.output_file(f"FILE.info2.1D", optional=True),
        voxel_distance_to_centroid=execution.output_file(f"FILE.vcd.1D", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dkmeansOutputs",
    "V_3DKMEANS_METADATA",
    "v_3dkmeans",
]
