# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VECTORSTATS_METADATA = Metadata(
    id="a8a67c93f9ad1cdf03ad2a1e473010538e53830b.boutiques",
    name="vectorstats",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class VectorstatsColumn:
    """
    add a column to the design matrix corresponding to subject element-wise
    values (note that the contrast matrix must include an additional column for
    each use of this option); the text file provided via this option should
    contain a file name for each subject.
    """
    path: InputPathType
    """add a column to the design matrix corresponding to subject element-wise
    values (note that the contrast matrix must include an additional column for
    each use of this option); the text file provided via this option should
    contain a file name for each subject"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-column")
        cargs.append(execution.input_file(self.path))
        return cargs


@dataclasses.dataclass
class VectorstatsConfig:
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
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class VectorstatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `vectorstats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def vectorstats(
    input_: InputPathType,
    design: InputPathType,
    contrast: InputPathType,
    output: str,
    notest: bool = False,
    errors: str | None = None,
    exchange_within: InputPathType | None = None,
    exchange_whole: InputPathType | None = None,
    strong: bool = False,
    nshuffles: int | None = None,
    permutations: InputPathType | None = None,
    variance: InputPathType | None = None,
    ftests: InputPathType | None = None,
    fonly: bool = False,
    column: list[VectorstatsColumn] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[VectorstatsConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> VectorstatsOutputs:
    """
    Statistical testing of vector data using non-parametric permutation testing.
    
    This command can be used to perform permutation testing of any form of data.
    The data for each input subject must be stored in a text file, with one
    value per row. The data for each row across subjects will be tested
    independently, i.e. there is no statistical enhancement that occurs between
    the data; however family-wise error control will be used.
    
    In some software packages, a column of ones is automatically added to the
    GLM design matrix; the purpose of this column is to estimate the "global
    intercept", which is the predicted value of the observed variable if all
    explanatory variables were to be zero. However there are rare situations
    where including such a column would not be appropriate for a particular
    experimental design. Hence, in MRtrix3 statistical inference commands, it is
    up to the user to determine whether or not this column of ones should be
    included in their design matrix, and add it explicitly if necessary. The
    contrast matrix must also reflect the presence of this additional column.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_: a text file listing the file names of the input subject data.
        design: the design matrix.
        contrast: the contrast matrix.
        output: the filename prefix for all output.
        notest: don't perform statistical inference; only output population\
            statistics (effect size, stdev etc).
        errors: specify nature of errors for shuffling; options are:\
            ee,ise,both (default: ee).
        exchange_within: specify blocks of observations within each of which\
            data may undergo restricted exchange.
        exchange_whole: specify blocks of observations that may be exchanged\
            with one another (for independent and symmetric errors, sign-flipping\
            will occur block-wise).
        strong: use strong familywise error control across multiple hypotheses.
        nshuffles: the number of shuffles (default: 5000).
        permutations: manually define the permutations (relabelling). The input\
            should be a text file defining a m x n matrix, where each relabelling\
            is defined as a column vector of size m, and the number of columns, n,\
            defines the number of permutations. Can be generated with the\
            palm_quickperms function in PALM\
            (http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PALM). Overrides the -nshuffles\
            option.
        variance: define variance groups for the G-statistic; measurements for\
            which the expected variance is equivalent should contain the same index.
        ftests: perform F-tests; input text file should contain, for each\
            F-test, a row containing ones and zeros, where ones indicate the rows\
            of the contrast matrix to be included in the F-test.
        fonly: only assess F-tests; do not perform statistical inference on\
            entries in the contrast matrix.
        column: add a column to the design matrix corresponding to subject\
            element-wise values (note that the contrast matrix must include an\
            additional column for each use of this option); the text file provided\
            via this option should contain a file name for each subject.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VectorstatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VECTORSTATS_METADATA)
    cargs = []
    cargs.append("vectorstats")
    if notest:
        cargs.append("-notest")
    if errors is not None:
        cargs.extend([
            "-errors",
            errors
        ])
    if exchange_within is not None:
        cargs.extend([
            "-exchange_within",
            execution.input_file(exchange_within)
        ])
    if exchange_whole is not None:
        cargs.extend([
            "-exchange_whole",
            execution.input_file(exchange_whole)
        ])
    if strong:
        cargs.append("-strong")
    if nshuffles is not None:
        cargs.extend([
            "-nshuffles",
            str(nshuffles)
        ])
    if permutations is not None:
        cargs.extend([
            "-permutations",
            execution.input_file(permutations)
        ])
    if variance is not None:
        cargs.extend([
            "-variance",
            execution.input_file(variance)
        ])
    if ftests is not None:
        cargs.extend([
            "-ftests",
            execution.input_file(ftests)
        ])
    if fonly:
        cargs.append("-fonly")
    if column is not None:
        cargs.extend([a for c in [s.run(execution) for s in column] for a in c])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend([
            "-nthreads",
            str(nthreads)
        ])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(input_))
    cargs.append(execution.input_file(design))
    cargs.append(execution.input_file(contrast))
    cargs.append(output)
    ret = VectorstatsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VECTORSTATS_METADATA",
    "VectorstatsColumn",
    "VectorstatsConfig",
    "VectorstatsOutputs",
    "vectorstats",
]
