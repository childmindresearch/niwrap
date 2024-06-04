import json
import pathlib
import re

PROJECT_DIR = pathlib.Path(__file__).parent.parent.parent
assert (PROJECT_DIR / "descriptors/c3d").exists()
FILE_MD_DOCS = PROJECT_DIR / "extraction/c3d/c3d.md"
FILE_OUT = PROJECT_DIR / "descriptors/c3d/c3d.json"

# Extracted from c3d source code with a regex (cmd == "[^"]+"(?:\s*\|\|\s*cmd == "[^"]+")*)
# https://sourceforge.net/p/c3d/git/ci/master/tree/ConvertImageND.cxx
commands = [
    ["-accum"],
    ["-acos"],
    ["-add"],
    ["-align-landmarks", "-alm"],
    ["-anisotropic-diffusion", "-ad"],
    ["-antialias", "-alias"],
    ["-as", "-set"],
    ["-asin"],
    ["-atan2"],
    ["-background"],
    ["-biascorr", "-n4", "-n4-bias-correction"],
    ["-binarize"],
    ["-canny"],
    ["-ceil"],
    ["-centroid"],
    ["-centroid-mark"],
    ["-connected-components", "-connected", "-comp"],
    ["-clear"],
    ["-clip"],
    ["-colormap", "-color-map"],
    ["-compress"],
    ["-no-compress"],
    ["-conv"],
    ["-coordinate-map-voxel", "-cmv"],
    ["-coordinate-map-physical", "-cmp"],
    ["-copy-transform", "-ct"],
    ["-cos"],
    ["-create"],
    ["-dicom-series-list"],
    ["-dicom-series-read"],
    ["-dilate"],
    ["-divide"],
    ["-dup", "-duplicate"],
    ["-endaccum"],
    ["-endfor"],
    ["-erode"],
    ["-erf"],
    ["-exp"],
    ["-export-patches", "-xp"],
    ["-export-patches-aug", "-xpa"],
    ["-extrude-seg"],
    ["-fill-background-with-noise", "-fbn"],
    ["-fft"],
    ["-flip"],
    ["-floor"],
    ["-foreach"],
    ["-foreach-comp"],
    ["-glm"],
    ["-grad", "-gradient"],
    ["-h", "-help", "--help"],
    ["-hf", "-holefill"],
    ["-hesseig", "-hessian-eigenvalues"],
    ["-hessobj", "-hessian-objectness"],
    ["-histmatch", "-histogram-match"],
    ["-info"],
    ["-info-full"],
    ["-insert", "-ins"],
    ["-interpolation", "-interp", "-int"],
    ["-iterations"],
    ["-label-overlap"],
    ["-label-statistics", "-lstat"],
    ["-landmarks-to-spheres", "-lts"],
    ["-laplacian", "-laplace"],
    ["-levelset"],
    ["-levelset-curvature"],
    ["-levelset-advection"],
    ["-ln", "-log"],
    ["-log10"],
    ["-manual"],
    ["-match-bounding-box", "-mbb"],
    ["-maximum", "-max"],
    ["-mcs", "-multicomponent-split"],
    ["-mean"],
    ["-median", "-median-filter"],
    ["-merge"],
    ["-mf", "-mean-filter"],
    ["-mi", "-mutual-info"],
    ["-minimum", "-min"],
    ["-mixture", "-mixture-model"],
    ["-moments"],
    ["-mmi", "-mattes-mutual-info"],
    ["-msq", "-mean-square"],
    ["-multiply", "-times"],
    ["-ncc", "-normalized-cross-correlation"],
    ["-ncor", "-normalized-correlation"],
    ["-nmi", "-normalized-mutual-info"],
    ["-noise-gaussian", "-noise"],
    ["-noise-poisson", "-noise-shot"],
    ["-noise-speckle"],
    ["-noise-salt-pepper"],
    ["-nomcs", "-no-multicomponent-split"],
    ["-nlw", "-normwin", "-normalize-local-window"],
    ["-normpdf"],
    ["-noround"],
    ["-nospm"],
    ["-o", "-output"],
    ["-omc", "-output-multicomponent"],
    ["-oomc", "-output-multiple-multicomponent"],
    ["-orient"],
    ["-oo", "-output-multiple"],
    ["-orient"],
    ["-origin"],
    ["-origin-voxel"],
    ["-origin-voxel-coord"],
    ["-overlap"],
    ["-overlay-label-image", "-oli"],
    ["-pad"],
    ["-padto", "-pad-to"],
    ["-pca"],
    ["-percent-intensity-mode", "-pim"],
    ["-pixel"],
    ["-pop"],
    ["-popas"],
    ["-probe"],
    ["-push", "-get"],
    ["-rank"],
    ["-reciprocal"],
    ["-region"],
    ["-reorder"],
    ["-retain-labels"],
    ["-rf-apply"],
    ["-rf-train"],
    ["-rf-param-patch"],
    ["-rf-param-usexyz"],
    ["-rf-param-nousexyz"],
    ["-rf-param-ntrees"],
    ["-rf-param-treedepth"],
    ["-set-sform"],
    ["-replace"],
    ["-resample"],
    ["-resample-iso"],
    ["-resample-mm"],
    ["-reslice-itk"],
    ["-reslice-matrix"],
    ["-reslice-identity"],
    ["-rgb2hsv"],
    ["-rms"],
    ["-round"],
    ["-scale"],
    ["-set-sform"],
    ["-sin"],
    ["-slice"],
    ["-slice-all"],
    ["-sharpen"],
    ["-shift"],
    ["-signed-distance-transform", "-sdt"],
    ["-smooth"],
    ["-smooth-fast"],
    ["-spacing"],
    ["-split"],
    ["-sqrt"],
    ["-staple"],
    ["-steig", "-structure-tensor-eigenvalues"],
    ["-spm"],
    ["-subtract"],
    ["-supervoxel", "-sv"],
    ["-stretch"],
    ["-swapdim"],
    ["-test-image"],
    ["-test-probe"],
    ["-threshold", "-thresh"],
    ["-tile"],
    ["-trim"],
    ["-trim-to-size"],
    ["-type"],
    ["-verbose"],
    ["-noverbose"],
    ["-version"],
    ["-vote"],
    ["-vote-mrf"],
    ["-vote-label"],
    ["-voxel-sum"],
    ["-voxel-integral", "-voxel-int"],
    ["-voxelwise-regression", "-voxreg"],
    ["-warp"],
    ["-warp-label"],
    ["-wrap"],
    ["-weighted-sum", "-wsum"],
    ["-weighted-sum-voxelwise", "-wsv"],
]

with open(FILE_MD_DOCS, "r") as f:
    md_docs = f.read()
md_docs = md_docs.split("####")
# Filter out sections without "Syntax: "
md_docs = [md for md in md_docs if "Syntax" in md]
# find command names "Syntax:? `(.+)"
md_docs = {re.search(r"Syntax:? `(.+)", md).group(1)+f"_{i}": md for i, md in enumerate(md_docs)}

def find_description(command):
    for alt in command:
        for syntax, doc in md_docs.items():
            if syntax.startswith(alt):
                return doc.strip()
    for alt in command:
        for syntax, doc in md_docs.items():
            if alt in syntax:
                return doc.strip()
    return None

def as_name(command):
    command = sorted(command, key=len, reverse=True)[0]
    return command[1:].replace("-", "_")

subcommands = []

for command in commands:
    command_name = as_name(command)
    command_flag = command[0]
    command_description = find_description(command) or "No description found."
    subcommands.append({
        "id": command_name,
        "name": command_name,
        "command-line": "[x]",
        "description": command_description,
        "inputs": [{
            "id": command_name,
            "name": command_name,
            "value-key": "[x]",
            "type": "String",
            "command-line-flag": command_flag,
            "optional": False,
            "description": command_description,
        }],
    })

boutiques_descriptor = {
    "name": "c3d",
    "description": "C3D is a command-line tool for medical image processing.",
    "tool-version": "1.0.0",
    "schema-version": "0.5",
    "command-line": "c3d [INPUT] [OPERATIONS] [OUTPUT]",
    "inputs": [
        {
            "id": "input",
            "name": "Input image",
            "value-key": "[INPUT]",
            "description": "The input image to process.",
            "type": "File",
            "command-line-flag": "-i",
            "optional": False,
        },
        {
            "id": "output",
            "name": "Output image",
            "value-key": "[OUTPUT]",
            "description": "The output image.",
            "type": "File",
            "command-line-flag": "-o",
            "optional": False,
        },
        {
            "id": "operations",
            "name": "Operations",
            "value-key": "[OPERATIONS]",
            "description": "The operations to perform.",
            "type": subcommands,
            "optional": False,
        },
    ],
}



    

#print(md_docs[22])

with open(FILE_OUT, "w") as f:
    json.dump(boutiques_descriptor, f, indent=2)
    f.write("\n")
