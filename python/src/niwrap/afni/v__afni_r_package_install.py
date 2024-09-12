# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__AFNI_R_PACKAGE_INSTALL_METADATA = Metadata(
    id="3d32ab792f67c9bb98ae4d1346a31520aa3ad424.boutiques",
    name="@afni_R_package_install",
    package="afni",
    container_image_tag="fcpindi/c-pac:latest",
)


class VAfniRPackageInstallOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__afni_r_package_install(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    install_log: OutputPathType
    """A log file listing all installed R packages."""


def v__afni_r_package_install(
    afni_: bool = False,
    shiny: bool = False,
    bayes_view_: bool = False,
    circos: bool = False,
    custom_packages: str | None = None,
    mirror: str | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> VAfniRPackageInstallOutputs:
    """
    Helper script to install R packages for various afni-ish purposes.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@afni_R_package_install.html
    
    Args:
        afni_: Install AFNI related R packages.
        shiny: Install AFNI related shiny app packages.
        bayes_view_: Install R packages for bayes_view.
        circos: Install OmicCircos for FATCAT_matplot.
        custom_packages: Install custom R packages (space-separated list). Must\
            start and end with double quotes.
        mirror: Set the CRAN mirror to a custom URL.
        help_: Show help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniRPackageInstallOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_R_PACKAGE_INSTALL_METADATA)
    cargs = []
    cargs.append("@afni_R_package_install")
    if afni_:
        cargs.append("-afni")
    if shiny:
        cargs.append("-shiny")
    if bayes_view_:
        cargs.append("-bayes_view")
    if circos:
        cargs.append("-circos")
    if custom_packages is not None:
        cargs.extend([
            "-custom",
            custom_packages
        ])
    if mirror is not None:
        cargs.extend([
            "-mirror",
            mirror
        ])
    if help_:
        cargs.append("-help")
    ret = VAfniRPackageInstallOutputs(
        root=execution.output_file("."),
        install_log=execution.output_file("R_packages_installed.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VAfniRPackageInstallOutputs",
    "V__AFNI_R_PACKAGE_INSTALL_METADATA",
    "v__afni_r_package_install",
]
