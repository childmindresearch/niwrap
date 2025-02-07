# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FIXELCFESTATS_METADATA = Metadata(
    id="85b1cb9bb9525faf62a80ea0820d52c7ae94777f.boutiques",
    name="fixelcfestats",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
FixelcfestatsColumnParameters = typing.TypedDict('FixelcfestatsColumnParameters', {
    "__STYX_TYPE__": typing.Literal["column"],
    "path": InputPathType,
})
FixelcfestatsConfigParameters = typing.TypedDict('FixelcfestatsConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
FixelcfestatsVariousStringParameters = typing.TypedDict('FixelcfestatsVariousStringParameters', {
    "__STYX_TYPE__": typing.Literal["VariousString"],
    "obj": str,
})
FixelcfestatsVariousFileParameters = typing.TypedDict('FixelcfestatsVariousFileParameters', {
    "__STYX_TYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})
FixelcfestatsParameters = typing.TypedDict('FixelcfestatsParameters', {
    "__STYX_TYPE__": typing.Literal["fixelcfestats"],
    "mask": typing.NotRequired[InputPathType | None],
    "notest": bool,
    "errors": typing.NotRequired[str | None],
    "exchange_within": typing.NotRequired[InputPathType | None],
    "exchange_whole": typing.NotRequired[InputPathType | None],
    "strong": bool,
    "nshuffles": typing.NotRequired[int | None],
    "permutations": typing.NotRequired[InputPathType | None],
    "nonstationarity": bool,
    "skew_nonstationarity": typing.NotRequired[float | None],
    "nshuffles_nonstationarity": typing.NotRequired[int | None],
    "permutations_nonstationarity": typing.NotRequired[InputPathType | None],
    "cfe_dh": typing.NotRequired[float | None],
    "cfe_e": typing.NotRequired[float | None],
    "cfe_h": typing.NotRequired[float | None],
    "cfe_c": typing.NotRequired[float | None],
    "cfe_legacy": bool,
    "variance": typing.NotRequired[InputPathType | None],
    "ftests": typing.NotRequired[InputPathType | None],
    "fonly": bool,
    "column": typing.NotRequired[list[FixelcfestatsColumnParameters] | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[FixelcfestatsConfigParameters] | None],
    "help": bool,
    "version": bool,
    "in_fixel_directory": InputPathType,
    "subjects": InputPathType,
    "design": InputPathType,
    "contrast": InputPathType,
    "connectivity": typing.Union[FixelcfestatsVariousStringParameters, FixelcfestatsVariousFileParameters],
    "out_fixel_directory": str,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "fixelcfestats": fixelcfestats_cargs,
        "column": fixelcfestats_column_cargs,
        "config": fixelcfestats_config_cargs,
        "VariousString": fixelcfestats_various_string_cargs,
        "VariousFile": fixelcfestats_various_file_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "fixelcfestats": fixelcfestats_outputs,
        "column": fixelcfestats_column_outputs,
        "config": fixelcfestats_config_outputs,
        "VariousString": fixelcfestats_various_string_outputs,
        "VariousFile": fixelcfestats_various_file_outputs,
    }.get(t)


def fixelcfestats_column_params(
    path: InputPathType,
) -> FixelcfestatsColumnParameters:
    """
    Build parameters.
    
    Args:
        path: add a column to the design matrix corresponding to subject\
            fixel-wise values (note that the contrast matrix must include an\
            additional column for each use of this option); the text file provided\
            via this option should contain a file name for each subject.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "column",
        "path": path,
    }
    return params


def fixelcfestats_column_cargs(
    params: FixelcfestatsColumnParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-column")
    cargs.append(execution.input_file(params.get("path")))
    return cargs


def fixelcfestats_config_params(
    key: str,
    value: str,
) -> FixelcfestatsConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def fixelcfestats_config_cargs(
    params: FixelcfestatsConfigParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


def fixelcfestats_various_string_params(
    obj: str,
) -> FixelcfestatsVariousStringParameters:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString",
        "obj": obj,
    }
    return params


def fixelcfestats_various_string_cargs(
    params: FixelcfestatsVariousStringParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append(params.get("obj"))
    return cargs


def fixelcfestats_various_file_params(
    obj: InputPathType,
) -> FixelcfestatsVariousFileParameters:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile",
        "obj": obj,
    }
    return params


def fixelcfestats_various_file_cargs(
    params: FixelcfestatsVariousFileParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


class FixelcfestatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixelcfestats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fixelcfestats_params(
    in_fixel_directory: InputPathType,
    subjects: InputPathType,
    design: InputPathType,
    contrast: InputPathType,
    connectivity: typing.Union[FixelcfestatsVariousStringParameters, FixelcfestatsVariousFileParameters],
    out_fixel_directory: str,
    mask: InputPathType | None = None,
    notest: bool = False,
    errors: str | None = None,
    exchange_within: InputPathType | None = None,
    exchange_whole: InputPathType | None = None,
    strong: bool = False,
    nshuffles: int | None = None,
    permutations: InputPathType | None = None,
    nonstationarity: bool = False,
    skew_nonstationarity: float | None = None,
    nshuffles_nonstationarity: int | None = None,
    permutations_nonstationarity: InputPathType | None = None,
    cfe_dh: float | None = None,
    cfe_e: float | None = None,
    cfe_h: float | None = None,
    cfe_c: float | None = None,
    cfe_legacy: bool = False,
    variance: InputPathType | None = None,
    ftests: InputPathType | None = None,
    fonly: bool = False,
    column: list[FixelcfestatsColumnParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelcfestatsConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> FixelcfestatsParameters:
    """
    Build parameters.
    
    Args:
        in_fixel_directory: the fixel directory containing the data files for\
            each subject (after obtaining fixel correspondence.
        subjects: a text file listing the subject identifiers (one per line).\
            This should correspond with the filenames in the fixel directory\
            (including the file extension), and be listed in the same order as the\
            rows of the design matrix.
        design: the design matrix.
        contrast: the contrast matrix, specified as rows of weights.
        connectivity: the fixel-fixel connectivity matrix.
        out_fixel_directory: the output directory where results will be saved.\
            Will be created if it does not exist.
        mask: provide a fixel data file containing a mask of those fixels to be\
            used during processing.
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
        nonstationarity: perform non-stationarity correction.
        skew_nonstationarity: specify the skew parameter for empirical\
            statistic calculation (default for this command is 1).
        nshuffles_nonstationarity: the number of shuffles to use when\
            precomputing the empirical statistic image for non-stationarity\
            correction (default: 5000).
        permutations_nonstationarity: manually define the permutations\
            (relabelling) for computing the emprical statistics for\
            non-stationarity correction. The input should be a text file defining a\
            m x n matrix, where each relabelling is defined as a column vector of\
            size m, and the number of columns, n, defines the number of\
            permutations. Can be generated with the palm_quickperms function in\
            PALM (http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PALM) Overrides the\
            -nshuffles_nonstationarity option.
        cfe_dh: the height increment used in the cfe integration (default: 0.1).
        cfe_e: cfe extent exponent (default: 2).
        cfe_h: cfe height exponent (default: 3).
        cfe_c: cfe connectivity exponent (default: 0.5).
        cfe_legacy: use the legacy (non-normalised) form of the cfe equation.
        variance: define variance groups for the G-statistic; measurements for\
            which the expected variance is equivalent should contain the same index.
        ftests: perform F-tests; input text file should contain, for each\
            F-test, a row containing ones and zeros, where ones indicate the rows\
            of the contrast matrix to be included in the F-test.
        fonly: only assess F-tests; do not perform statistical inference on\
            entries in the contrast matrix.
        column: add a column to the design matrix corresponding to subject\
            fixel-wise values (note that the contrast matrix must include an\
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fixelcfestats",
        "notest": notest,
        "strong": strong,
        "nonstationarity": nonstationarity,
        "cfe_legacy": cfe_legacy,
        "fonly": fonly,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "in_fixel_directory": in_fixel_directory,
        "subjects": subjects,
        "design": design,
        "contrast": contrast,
        "connectivity": connectivity,
        "out_fixel_directory": out_fixel_directory,
    }
    if mask is not None:
        params["mask"] = mask
    if errors is not None:
        params["errors"] = errors
    if exchange_within is not None:
        params["exchange_within"] = exchange_within
    if exchange_whole is not None:
        params["exchange_whole"] = exchange_whole
    if nshuffles is not None:
        params["nshuffles"] = nshuffles
    if permutations is not None:
        params["permutations"] = permutations
    if skew_nonstationarity is not None:
        params["skew_nonstationarity"] = skew_nonstationarity
    if nshuffles_nonstationarity is not None:
        params["nshuffles_nonstationarity"] = nshuffles_nonstationarity
    if permutations_nonstationarity is not None:
        params["permutations_nonstationarity"] = permutations_nonstationarity
    if cfe_dh is not None:
        params["cfe_dh"] = cfe_dh
    if cfe_e is not None:
        params["cfe_e"] = cfe_e
    if cfe_h is not None:
        params["cfe_h"] = cfe_h
    if cfe_c is not None:
        params["cfe_c"] = cfe_c
    if variance is not None:
        params["variance"] = variance
    if ftests is not None:
        params["ftests"] = ftests
    if column is not None:
        params["column"] = column
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def fixelcfestats_cargs(
    params: FixelcfestatsParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("fixelcfestats")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("notest"):
        cargs.append("-notest")
    if params.get("errors") is not None:
        cargs.extend([
            "-errors",
            params.get("errors")
        ])
    if params.get("exchange_within") is not None:
        cargs.extend([
            "-exchange_within",
            execution.input_file(params.get("exchange_within"))
        ])
    if params.get("exchange_whole") is not None:
        cargs.extend([
            "-exchange_whole",
            execution.input_file(params.get("exchange_whole"))
        ])
    if params.get("strong"):
        cargs.append("-strong")
    if params.get("nshuffles") is not None:
        cargs.extend([
            "-nshuffles",
            str(params.get("nshuffles"))
        ])
    if params.get("permutations") is not None:
        cargs.extend([
            "-permutations",
            execution.input_file(params.get("permutations"))
        ])
    if params.get("nonstationarity"):
        cargs.append("-nonstationarity")
    if params.get("skew_nonstationarity") is not None:
        cargs.extend([
            "-skew_nonstationarity",
            str(params.get("skew_nonstationarity"))
        ])
    if params.get("nshuffles_nonstationarity") is not None:
        cargs.extend([
            "-nshuffles_nonstationarity",
            str(params.get("nshuffles_nonstationarity"))
        ])
    if params.get("permutations_nonstationarity") is not None:
        cargs.extend([
            "-permutations_nonstationarity",
            execution.input_file(params.get("permutations_nonstationarity"))
        ])
    if params.get("cfe_dh") is not None:
        cargs.extend([
            "-cfe_dh",
            str(params.get("cfe_dh"))
        ])
    if params.get("cfe_e") is not None:
        cargs.extend([
            "-cfe_e",
            str(params.get("cfe_e"))
        ])
    if params.get("cfe_h") is not None:
        cargs.extend([
            "-cfe_h",
            str(params.get("cfe_h"))
        ])
    if params.get("cfe_c") is not None:
        cargs.extend([
            "-cfe_c",
            str(params.get("cfe_c"))
        ])
    if params.get("cfe_legacy"):
        cargs.append("-cfe_legacy")
    if params.get("variance") is not None:
        cargs.extend([
            "-variance",
            execution.input_file(params.get("variance"))
        ])
    if params.get("ftests") is not None:
        cargs.extend([
            "-ftests",
            execution.input_file(params.get("ftests"))
        ])
    if params.get("fonly"):
        cargs.append("-fonly")
    if params.get("column") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("column")] for a in c])
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(execution.input_file(params.get("in_fixel_directory")))
    cargs.append(execution.input_file(params.get("subjects")))
    cargs.append(execution.input_file(params.get("design")))
    cargs.append(execution.input_file(params.get("contrast")))
    cargs.extend(dyn_cargs(params.get("connectivity")["__STYXTYPE__"])(params.get("connectivity"), execution))
    cargs.append(params.get("out_fixel_directory"))
    return cargs


def fixelcfestats_outputs(
    params: FixelcfestatsParameters,
    execution: Execution,
) -> FixelcfestatsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FixelcfestatsOutputs(
        root=execution.output_file("."),
    )
    return ret


def fixelcfestats_execute(
    params: FixelcfestatsParameters,
    execution: Execution,
) -> FixelcfestatsOutputs:
    """
    Fixel-based analysis using connectivity-based fixel enhancement and
    non-parametric permutation testing.
    
    Unlike previous versions of this command, where a whole-brain tractogram
    file would be provided as input in order to generate the fixel-fixel
    connectivity matrix and smooth fixel data, this version expects to be
    provided with the directory path to a pre-calculated fixel-fixel
    connectivity matrix (likely generated using the MRtrix3 command
    fixelconnectivity), and for the input fixel data to have already been
    smoothed (likely using the MRtrix3 command fixelfilter).
    
    Note that if the -mask option is used, the output fixel directory will still
    contain the same set of fixels as that present in the input fixel template,
    in order to retain fixel correspondence. However a consequence of this is
    that all fixels in the template will be initialy visible when the output
    fixel directory is loaded in mrview. Those fixels outside the processing
    mask will immediately disappear from view as soon as any data-file-based
    fixel colouring or thresholding is applied.
    
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
    
    Raffelt, D.; Smith, RE.; Ridgway, GR.; Tournier, JD.; Vaughan, DN.; Rose,
    S.; Henderson, R.; Connelly, A. Connectivity-based fixel enhancement:
    Whole-brain statistical analysis of diffusion MRI measures in the presence
    of crossing fibres.Neuroimage, 2015, 15(117):40-55
    
    * If not using the -cfe_legacy option:
    Smith, RE.; Dimond, D; Vaughan, D.; Parker, D.; Dhollander, T.; Jackson, G.;
    Connelly, A. Intrinsic non-stationarity correction for Fixel-Based Analysis.
    In Proc OHBM 2019 M789
    
    * If using the -nonstationary option:
    Salimi-Khorshidi, G. Smith, S.M. Nichols, T.E. Adjusting the effect of
    nonstationarity in cluster-based and TFCE inference. NeuroImage, 2011,
    54(3), 2006-19.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FixelcfestatsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fixelcfestats_cargs(params, execution)
    ret = fixelcfestats_outputs(params, execution)
    execution.run(cargs)
    return ret


def fixelcfestats(
    in_fixel_directory: InputPathType,
    subjects: InputPathType,
    design: InputPathType,
    contrast: InputPathType,
    connectivity: typing.Union[FixelcfestatsVariousStringParameters, FixelcfestatsVariousFileParameters],
    out_fixel_directory: str,
    mask: InputPathType | None = None,
    notest: bool = False,
    errors: str | None = None,
    exchange_within: InputPathType | None = None,
    exchange_whole: InputPathType | None = None,
    strong: bool = False,
    nshuffles: int | None = None,
    permutations: InputPathType | None = None,
    nonstationarity: bool = False,
    skew_nonstationarity: float | None = None,
    nshuffles_nonstationarity: int | None = None,
    permutations_nonstationarity: InputPathType | None = None,
    cfe_dh: float | None = None,
    cfe_e: float | None = None,
    cfe_h: float | None = None,
    cfe_c: float | None = None,
    cfe_legacy: bool = False,
    variance: InputPathType | None = None,
    ftests: InputPathType | None = None,
    fonly: bool = False,
    column: list[FixelcfestatsColumnParameters] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelcfestatsConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> FixelcfestatsOutputs:
    """
    Fixel-based analysis using connectivity-based fixel enhancement and
    non-parametric permutation testing.
    
    Unlike previous versions of this command, where a whole-brain tractogram
    file would be provided as input in order to generate the fixel-fixel
    connectivity matrix and smooth fixel data, this version expects to be
    provided with the directory path to a pre-calculated fixel-fixel
    connectivity matrix (likely generated using the MRtrix3 command
    fixelconnectivity), and for the input fixel data to have already been
    smoothed (likely using the MRtrix3 command fixelfilter).
    
    Note that if the -mask option is used, the output fixel directory will still
    contain the same set of fixels as that present in the input fixel template,
    in order to retain fixel correspondence. However a consequence of this is
    that all fixels in the template will be initialy visible when the output
    fixel directory is loaded in mrview. Those fixels outside the processing
    mask will immediately disappear from view as soon as any data-file-based
    fixel colouring or thresholding is applied.
    
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
    
    Raffelt, D.; Smith, RE.; Ridgway, GR.; Tournier, JD.; Vaughan, DN.; Rose,
    S.; Henderson, R.; Connelly, A. Connectivity-based fixel enhancement:
    Whole-brain statistical analysis of diffusion MRI measures in the presence
    of crossing fibres.Neuroimage, 2015, 15(117):40-55
    
    * If not using the -cfe_legacy option:
    Smith, RE.; Dimond, D; Vaughan, D.; Parker, D.; Dhollander, T.; Jackson, G.;
    Connelly, A. Intrinsic non-stationarity correction for Fixel-Based Analysis.
    In Proc OHBM 2019 M789
    
    * If using the -nonstationary option:
    Salimi-Khorshidi, G. Smith, S.M. Nichols, T.E. Adjusting the effect of
    nonstationarity in cluster-based and TFCE inference. NeuroImage, 2011,
    54(3), 2006-19.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        in_fixel_directory: the fixel directory containing the data files for\
            each subject (after obtaining fixel correspondence.
        subjects: a text file listing the subject identifiers (one per line).\
            This should correspond with the filenames in the fixel directory\
            (including the file extension), and be listed in the same order as the\
            rows of the design matrix.
        design: the design matrix.
        contrast: the contrast matrix, specified as rows of weights.
        connectivity: the fixel-fixel connectivity matrix.
        out_fixel_directory: the output directory where results will be saved.\
            Will be created if it does not exist.
        mask: provide a fixel data file containing a mask of those fixels to be\
            used during processing.
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
        nonstationarity: perform non-stationarity correction.
        skew_nonstationarity: specify the skew parameter for empirical\
            statistic calculation (default for this command is 1).
        nshuffles_nonstationarity: the number of shuffles to use when\
            precomputing the empirical statistic image for non-stationarity\
            correction (default: 5000).
        permutations_nonstationarity: manually define the permutations\
            (relabelling) for computing the emprical statistics for\
            non-stationarity correction. The input should be a text file defining a\
            m x n matrix, where each relabelling is defined as a column vector of\
            size m, and the number of columns, n, defines the number of\
            permutations. Can be generated with the palm_quickperms function in\
            PALM (http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PALM) Overrides the\
            -nshuffles_nonstationarity option.
        cfe_dh: the height increment used in the cfe integration (default: 0.1).
        cfe_e: cfe extent exponent (default: 2).
        cfe_h: cfe height exponent (default: 3).
        cfe_c: cfe connectivity exponent (default: 0.5).
        cfe_legacy: use the legacy (non-normalised) form of the cfe equation.
        variance: define variance groups for the G-statistic; measurements for\
            which the expected variance is equivalent should contain the same index.
        ftests: perform F-tests; input text file should contain, for each\
            F-test, a row containing ones and zeros, where ones indicate the rows\
            of the contrast matrix to be included in the F-test.
        fonly: only assess F-tests; do not perform statistical inference on\
            entries in the contrast matrix.
        column: add a column to the design matrix corresponding to subject\
            fixel-wise values (note that the contrast matrix must include an\
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
        NamedTuple of outputs (described in `FixelcfestatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXELCFESTATS_METADATA)
    params = fixelcfestats_params(mask=mask, notest=notest, errors=errors, exchange_within=exchange_within, exchange_whole=exchange_whole, strong=strong, nshuffles=nshuffles, permutations=permutations, nonstationarity=nonstationarity, skew_nonstationarity=skew_nonstationarity, nshuffles_nonstationarity=nshuffles_nonstationarity, permutations_nonstationarity=permutations_nonstationarity, cfe_dh=cfe_dh, cfe_e=cfe_e, cfe_h=cfe_h, cfe_c=cfe_c, cfe_legacy=cfe_legacy, variance=variance, ftests=ftests, fonly=fonly, column=column, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, in_fixel_directory=in_fixel_directory, subjects=subjects, design=design, contrast=contrast, connectivity=connectivity, out_fixel_directory=out_fixel_directory)
    return fixelcfestats_execute(params, execution)


__all__ = [
    "FIXELCFESTATS_METADATA",
    "FixelcfestatsColumnParameters",
    "FixelcfestatsConfigParameters",
    "FixelcfestatsOutputs",
    "FixelcfestatsParameters",
    "FixelcfestatsVariousFileParameters",
    "FixelcfestatsVariousStringParameters",
    "fixelcfestats",
    "fixelcfestats_column_params",
    "fixelcfestats_config_params",
    "fixelcfestats_params",
    "fixelcfestats_various_file_params",
    "fixelcfestats_various_string_params",
]
