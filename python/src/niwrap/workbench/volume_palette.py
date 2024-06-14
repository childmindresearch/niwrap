# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

VOLUME_PALETTE_METADATA = Metadata(
    id="7d160f781d93cfe02ff4aa4f84ec99aaa6d066e4",
    name="volume-palette",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class VolumePalettePosPercent:
    """
    percentage min/max for positive data coloring
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


@dataclasses.dataclass
class VolumePaletteNegPercent:
    """
    percentage min/max for negative data coloring
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


@dataclasses.dataclass
class VolumePalettePosUser:
    """
    user min/max values for positive data coloring
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


@dataclasses.dataclass
class VolumePaletteNegUser:
    """
    user min/max values for negative data coloring
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


@dataclasses.dataclass
class VolumePaletteThresholding:
    """
    set the thresholding
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


class VolumePaletteOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_palette(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_palette(
    volume: str,
    mode: str,
    opt_subvolume_subvolume: str | None = None,
    pos_percent: VolumePalettePosPercent | None = None,
    neg_percent: VolumePaletteNegPercent | None = None,
    pos_user: VolumePalettePosUser | None = None,
    neg_user: VolumePaletteNegUser | None = None,
    opt_interpolate_interpolate: typing.Literal["true", "false"] | None = None,
    opt_disp_pos_display: typing.Literal["true", "false"] | None = None,
    opt_disp_neg_display: typing.Literal["true", "false"] | None = None,
    opt_disp_zero_display: typing.Literal["true", "false"] | None = None,
    opt_palette_name_name: str | None = None,
    thresholding: VolumePaletteThresholding | None = None,
    opt_inversion_type: str | None = None,
    runner: Runner = None,
) -> VolumePaletteOutputs:
    """
    volume-palette by Washington University School of Medicin.
    
    Set the palette of a volume file.
    
    The original volume file is overwritten with the modified version. By
    default, all columns of the volume file are adjusted to the new settings,
    use the -subvolume option to change only one subvolume. Mapping settings not
    specified in options will be taken from the first subvolume. The <mode>
    argument must be one of the following:
    
    MODE_AUTO_SCALE
    MODE_AUTO_SCALE_ABSOLUTE_PERCENTAGE
    MODE_AUTO_SCALE_PERCENTAGE
    MODE_USER_SCALE
    
    The <name> argument to -palette-name must be one of the following:
    
    ROY-BIG-BL
    videen_style
    Gray_Interp_Positive
    Gray_Interp
    PSYCH-FIXED
    RBGYR20
    RBGYR20P
    RYGBR4_positive
    RGRBR_mirror90_pos
    Orange-Yellow
    POS_NEG_ZERO
    red-yellow
    blue-lightblue
    FSL
    power_surf
    black-red
    black-green
    black-blue
    black-red-positive
    black-green-positive
    black-blue-positive
    blue-black-green
    blue-black-red
    red-black-green
    fsl_red
    fsl_green
    fsl_blue
    fsl_yellow
    RedWhiteBlue
    cool-warm
    spectral
    RY-BC-BL
    magma
    JET256
    PSYCH
    PSYCH-NO-NONE
    ROY-BIG
    clear_brain
    fidl
    raich4_clrmid
    raich6_clrmid
    HSB8_clrmid
    POS_NEG
    Special-RGB-Volume
    
    The <type> argument to -thresholding must be one of the following:
    
    THRESHOLD_TYPE_OFF
    THRESHOLD_TYPE_NORMAL
    THRESHOLD_TYPE_FILE
    
    The <test> argument to -thresholding must be one of the following:
    
    THRESHOLD_TEST_SHOW_OUTSIDE
    THRESHOLD_TEST_SHOW_INSIDE
    
    The <type> argument to -inversion must be one of the following:
    
    OFF
    POSITIVE_WITH_NEGATIVE
    POSITIVE_NEGATIVE_SEPARATE
    .
    
    Args:
        volume: the volume file to modify.
        mode: the mapping mode.
        opt_subvolume_subvolume: select a single subvolume: the subvolume\
            number or name.
        pos_percent: percentage min/max for positive data coloring.
        neg_percent: percentage min/max for negative data coloring.
        pos_user: user min/max values for positive data coloring.
        neg_user: user min/max values for negative data coloring.
        opt_interpolate_interpolate: interpolate colors: boolean, whether to\
            interpolate.
        opt_disp_pos_display: display positive data: boolean, whether to\
            display.
        opt_disp_neg_display: display positive data: boolean, whether to\
            display.
        opt_disp_zero_display: display data closer to zero than the min cutoff:\
            boolean, whether to display.
        opt_palette_name_name: set the palette used: the name of the palette.
        thresholding: set the thresholding.
        opt_inversion_type: specify palette inversion: the type of inversion.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumePaletteOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_PALETTE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-palette")
    cargs.append(volume)
    cargs.append(mode)
    if opt_subvolume_subvolume is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvolume])
    if pos_percent is not None:
        cargs.extend(["-pos-percent", *pos_percent.run(execution)])
    if neg_percent is not None:
        cargs.extend(["-neg-percent", *neg_percent.run(execution)])
    if pos_user is not None:
        cargs.extend(["-pos-user", *pos_user.run(execution)])
    if neg_user is not None:
        cargs.extend(["-neg-user", *neg_user.run(execution)])
    if opt_interpolate_interpolate is not None:
        cargs.extend(["-interpolate", opt_interpolate_interpolate])
    if opt_disp_pos_display is not None:
        cargs.extend(["-disp-pos", opt_disp_pos_display])
    if opt_disp_neg_display is not None:
        cargs.extend(["-disp-neg", opt_disp_neg_display])
    if opt_disp_zero_display is not None:
        cargs.extend(["-disp-zero", opt_disp_zero_display])
    if opt_palette_name_name is not None:
        cargs.extend(["-palette-name", opt_palette_name_name])
    if thresholding is not None:
        cargs.extend(["-thresholding", *thresholding.run(execution)])
    if opt_inversion_type is not None:
        cargs.extend(["-inversion", opt_inversion_type])
    ret = VolumePaletteOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_PALETTE_METADATA",
    "VolumePaletteNegPercent",
    "VolumePaletteNegUser",
    "VolumePaletteOutputs",
    "VolumePalettePosPercent",
    "VolumePalettePosUser",
    "VolumePaletteThresholding",
    "volume_palette",
]