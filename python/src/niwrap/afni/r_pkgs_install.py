# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

R_PKGS_INSTALL_METADATA = Metadata(
    id="9c9d4c7ec7df54a4bd835bc8c7156ea51895da44.boutiques",
    name="rPkgsInstall",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class RPkgsInstallOutputs(typing.NamedTuple):
    """
    Output object returned when calling `r_pkgs_install(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_packages: OutputPathType
    """Output R packages after installation, update, or removal"""


def r_pkgs_install(
    packages: str,
    download_site: str | None = None,
    check: bool = False,
    update_: bool = False,
    remove: bool = False,
    runner: Runner | None = None,
) -> RPkgsInstallOutputs:
    """
    A tool for installing, checking, updating, or removing R packages for AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        packages: List of R packages to install, update, or remove. Use 'ALL'\
            to refer to all AFNI-required packages.
        download_site: Specify the package repository website. Default is\
            'http://cloud.r-project.org'.
        check: Verify whether the specified R packages are installed on the\
            computer without installing/updating/removing them.
        update_: Update the specified R packages. If packages are not\
            installed, they will be installed.
        remove: Remove the specified R packages from the system.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RPkgsInstallOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(R_PKGS_INSTALL_METADATA)
    cargs = []
    cargs.append("rPkgsInstall")
    cargs.extend([
        "-pkgs",
        packages
    ])
    if download_site is not None:
        cargs.extend([
            "-site",
            download_site
        ])
    if check:
        cargs.append("-check")
    if update_:
        cargs.append("-update")
    if remove:
        cargs.append("-remove")
    ret = RPkgsInstallOutputs(
        root=execution.output_file("."),
        output_packages=execution.output_file(packages),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RPkgsInstallOutputs",
    "R_PKGS_INSTALL_METADATA",
    "r_pkgs_install",
]
