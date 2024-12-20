# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AVW2FSL_METADATA = Metadata(
    id="4bd3a4636820978ce77e10fce31f85d6ab419486.boutiques",
    name="avw2fsl",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class Avw2fslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `avw2fsl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dest: OutputPathType
    """Destination file or directory where the source is copied."""


def avw2fsl(
    source: list[str],
    destination: str,
    archive: bool = False,
    attributes_only: bool = False,
    backup: str | None = None,
    backup_noarg: bool = False,
    copy_contents: bool = False,
    no_dereference_preserve_links: bool = False,
    force: bool = False,
    interactive: bool = False,
    follow_symlinks_cmdline: bool = False,
    hard_link: bool = False,
    dereference: bool = False,
    no_clobber: bool = False,
    no_dereference: bool = False,
    preserve: bool = False,
    preserve_attr: str | None = None,
    preserve_context: bool = False,
    no_preserve: str | None = None,
    parents: bool = False,
    recursive: bool = False,
    reflink: str | None = None,
    remove_destination: bool = False,
    sparse: str | None = None,
    strip_trailing_slashes: bool = False,
    symbolic_link: bool = False,
    suffix: str | None = None,
    target_directory: str | None = None,
    no_target_directory: bool = False,
    update_: bool = False,
    verbose: bool = False,
    one_file_system: bool = False,
    selinux_context: bool = False,
    context: str | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Avw2fslOutputs:
    """
    Processing script to copy files and directories.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        source: Source file(s) or directory to copy.
        destination: Destination file or directory where the source is to be\
            copied.
        archive: Archive mode; same as -dR --preserve=all.
        attributes_only: Don't copy the file data, just the attributes.
        backup: Make a backup of each existing destination file.
        backup_noarg: Like --backup but does not accept an argument.
        copy_contents: Copy contents of special files when recursive.
        no_dereference_preserve_links: Same as --no-dereference\
            --preserve=links.
        force: If an existing destination file cannot be opened, remove it and\
            try again.
        interactive: Prompt before overwrite.
        follow_symlinks_cmdline: Follow command-line symbolic links in SOURCE.
        hard_link: Hard link files instead of copying.
        dereference: Always follow symbolic links in SOURCE.
        no_clobber: Do not overwrite an existing file.
        no_dereference: Never follow symbolic links in SOURCE.
        preserve: Preserve mode, ownership, and timestamps.
        preserve_attr: Preserve the specified attributes (default:\
            mode,ownership,timestamps).
        preserve_context: Deprecated, same as --preserve=context.
        no_preserve: Don't preserve the specified attributes.
        parents: Use full source file name under DIRECTORY.
        recursive: Copy directories recursively.
        reflink: Control clone/CoW copies.
        remove_destination: Remove each existing destination file before\
            attempting to open it.
        sparse: Control creation of sparse files.
        strip_trailing_slashes: Remove any trailing slashes from each SOURCE\
            argument.
        symbolic_link: Make symbolic links instead of copying.
        suffix: Override the usual backup suffix.
        target_directory: Specify the target directory.
        no_target_directory: Treat DEST as a normal file.
        update_: Copy only when the SOURCE file is newer than the destination\
            file or when the destination file is missing.
        verbose: Explain what is being done.
        one_file_system: Stay on this file system.
        selinux_context: Set SELinux security context of destination file to\
            default type.
        context: Like -Z, or if CTX is specified set the SELinux or SMACK\
            security context to CTX.
        help_: Display this help and exit.
        version: Output version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Avw2fslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AVW2FSL_METADATA)
    cargs = []
    cargs.append("avw2fsl")
    cargs.extend(source)
    cargs.append(destination)
    if archive:
        cargs.append("-a")
    if attributes_only:
        cargs.append("--attributes-only")
    if backup is not None:
        cargs.append("--backup=" + backup)
    if backup_noarg:
        cargs.append("-b")
    if copy_contents:
        cargs.append("--copy-contents")
    if no_dereference_preserve_links:
        cargs.append("-d")
    if force:
        cargs.append("-f")
    if interactive:
        cargs.append("-i")
    if follow_symlinks_cmdline:
        cargs.append("-H")
    if hard_link:
        cargs.append("-l")
    if dereference:
        cargs.append("-L")
    if no_clobber:
        cargs.append("-n")
    if no_dereference:
        cargs.append("-P")
    if preserve:
        cargs.append("-p")
    if preserve_attr is not None:
        cargs.append("--preserve=" + preserve_attr)
    if preserve_context:
        cargs.append("-c")
    if no_preserve is not None:
        cargs.append("--no-preserve=" + no_preserve)
    if parents:
        cargs.append("--parents")
    if recursive:
        cargs.append("-R")
    if reflink is not None:
        cargs.append("--reflink=" + reflink)
    if remove_destination:
        cargs.append("--remove-destination")
    if sparse is not None:
        cargs.append("--sparse=" + sparse)
    if strip_trailing_slashes:
        cargs.append("--strip-trailing-slashes")
    if symbolic_link:
        cargs.append("-s")
    if suffix is not None:
        cargs.append("-S=" + suffix)
    if target_directory is not None:
        cargs.append("-t=" + target_directory)
    if no_target_directory:
        cargs.append("-T")
    if update_:
        cargs.append("-u")
    if verbose:
        cargs.append("-v")
    if one_file_system:
        cargs.append("-x")
    if selinux_context:
        cargs.append("-Z")
    if context is not None:
        cargs.append("--context=" + context)
    if help_:
        cargs.append("--help")
    if version:
        cargs.append("--version")
    ret = Avw2fslOutputs(
        root=execution.output_file("."),
        output_dest=execution.output_file(destination),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AVW2FSL_METADATA",
    "Avw2fslOutputs",
    "avw2fsl",
]
