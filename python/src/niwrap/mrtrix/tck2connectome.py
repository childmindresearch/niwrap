# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


TCK2CONNECTOME_METADATA = Metadata(
    id="a03e73d5d9c3da6ab052a08a432f74334689a0c3",
    name="tck2connectome",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


class ConfigOutputs(typing.NamedTuple):
    """
    Output object returned when calling `Config.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class Config:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
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
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> ConfigOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ConfigOutputs`).
        """
        ret = ConfigOutputs(
            root=execution.output_file("."),
        )
        return ret


class Tck2connectomeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tck2connectome(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    connectome_out: OutputPathType
    """the output .csv file containing edge weights"""
    out_assignments: OutputPathType | None
    """output the node assignments of each streamline to a file; this can be used subsequently e.g. by the command connectome2tck """
    config: ConfigOutputs
    """Subcommand outputs"""


def tck2connectome(
    tracks_in: InputPathType,
    nodes_in: InputPathType,
    connectome_out: InputPathType,
    assignment_end_voxels: bool = False,
    assignment_radial_search: float | int | None = None,
    assignment_reverse_search: float | int | None = None,
    assignment_forward_search: float | int | None = None,
    assignment_all_voxels: bool = False,
    scale_length: bool = False,
    scale_invlength: bool = False,
    scale_invnodevol: bool = False,
    scale_file: InputPathType | None = None,
    symmetric: bool = False,
    zero_diagonal: bool = False,
    stat_edge: typing.Literal["statistic"] | None = None,
    tck_weights_in: InputPathType | None = None,
    keep_unassigned: bool = False,
    out_assignments: InputPathType | None = None,
    vector: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Config] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Tck2connectomeOutputs:
    """
    tck2connectome by Robert E. Smith (robert.smith@florey.edu.au).
    
    Generate a connectome matrix from a streamlines file and a node parcellation
    image.
    
    
    
    References:
    
    If using the default streamline-parcel assignment mechanism (or
    -assignment_radial_search option): Smith, R. E.; Tournier, J.-D.; Calamante,
    F. & Connelly, A. The effects of SIFT on the reproducibility and biological
    accuracy of the structural connectome. NeuroImage, 2015, 104, 253-265
    
    If using -scale_invlength or -scale_invnodevol options: Hagmann, P.;
    Cammoun, L.; Gigandet, X.; Meuli, R.; Honey, C.; Wedeen, V. & Sporns, O.
    Mapping the Structural Core of Human Cerebral Cortex. PLoS Biology 6(7),
    e159.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/tck2connectome.html
    
    Args:
        tracks_in: the input track file
        nodes_in: the input node parcellation image
        connectome_out: the output .csv file containing edge weights
        assignment_end_voxels: use a simple voxel lookup value at each
            streamline endpoint
        assignment_radial_search: perform a radial search from each streamline
            endpoint to locate the nearest node. Argument is the maximum radius in
            mm; if no node is found within this radius, the streamline endpoint is
            not assigned to any node. Default search distance is 4mm.
        assignment_reverse_search: traverse from each streamline endpoint
            inwards along the streamline, in search of the last node traversed by
            the streamline. Argument is the maximum traversal length in mm (set to 0
            to allow search to continue to the streamline midpoint).
        assignment_forward_search: project the streamline forwards from the
            endpoint in search of a parcellation node voxel. Argument is the maximum
            traversal length in mm.
        assignment_all_voxels: assign the streamline to all nodes it intersects
            along its length (note that this means a streamline may be assigned to
            more than two nodes, or indeed none at all)
        scale_length: scale each contribution to the connectome edge by the
            length of the streamline
        scale_invlength: scale each contribution to the connectome edge by the
            inverse of the streamline length
        scale_invnodevol: scale each contribution to the connectome edge by the
            inverse of the two node volumes
        scale_file: scale each contribution to the connectome edge according to
            the values in a vector file
        symmetric: Make matrices symmetric on output
        zero_diagonal: Set matrix diagonal to zero on output
        stat_edge: statistic for combining the values from all streamlines in an
            edge into a single scale value for that edge (options are:
            sum,mean,min,max; default=sum)
        tck_weights_in: specify a text scalar file containing the streamline
            weights
        keep_unassigned: By default, the program discards the information
            regarding those streamlines that are not successfully assigned to a node
            pair. Set this option to keep these values (will be the first row/column
            in the output matrix)
        out_assignments: output the node assignments of each streamline to a
            file; this can be used subsequently e.g. by the command connectome2tck
        vector: output a vector representing connectivities from a given seed
            point to target nodes, rather than a matrix of node-node connectivities
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `Tck2connectomeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCK2CONNECTOME_METADATA)
    cargs = []
    cargs.append("tck2connectome")
    if assignment_end_voxels:
        cargs.append("-assignment_end_voxels")
    if assignment_radial_search is not None:
        cargs.extend(["-assignment_radial_search", str(assignment_radial_search)])
    if assignment_reverse_search is not None:
        cargs.extend(["-assignment_reverse_search", str(assignment_reverse_search)])
    if assignment_forward_search is not None:
        cargs.extend(["-assignment_forward_search", str(assignment_forward_search)])
    if assignment_all_voxels:
        cargs.append("-assignment_all_voxels")
    if scale_length:
        cargs.append("-scale_length")
    if scale_invlength:
        cargs.append("-scale_invlength")
    if scale_invnodevol:
        cargs.append("-scale_invnodevol")
    if scale_file is not None:
        cargs.extend(["-scale_file", execution.input_file(scale_file)])
    if symmetric:
        cargs.append("-symmetric")
    if zero_diagonal:
        cargs.append("-zero_diagonal")
    if stat_edge is not None:
        cargs.extend(["-stat_edge", stat_edge])
    if tck_weights_in is not None:
        cargs.extend(["-tck_weights_in", execution.input_file(tck_weights_in)])
    if keep_unassigned:
        cargs.append("-keep_unassigned")
    if out_assignments is not None:
        cargs.extend(["-out_assignments", execution.input_file(out_assignments)])
    if vector:
        cargs.append("-vector")
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(tracks_in))
    cargs.append(execution.input_file(nodes_in))
    cargs.append(execution.input_file(connectome_out))
    ret = Tck2connectomeOutputs(
        root=execution.output_file("."),
        connectome_out=execution.output_file(f"{pathlib.Path(connectome_out).name}"),
        out_assignments=execution.output_file(f"{pathlib.Path(out_assignments).name}") if out_assignments is not None else None,
        config=[config.outputs(execution) for config in config],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "Config",
    "ConfigOutputs",
    "TCK2CONNECTOME_METADATA",
    "Tck2connectomeOutputs",
    "tck2connectome",
]
