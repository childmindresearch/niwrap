> [!NOTE]  
> In early development and is not yet ready for production use.

# CPAC Boutiques Descriptor Collection

This repository contains a collection of Boutiques descriptors for all command line brain imaging tools called by C-PAC. The descriptors are stored in the `descriptors` directory and are organized by the brain imaging software framework they belong to.

## Helpful resources

- [Boutiques documentation](https://boutiques.github.io/)
- [Boutiques schema](https://github.com/boutiques/boutiques/blob/master/boutiques/schema/descriptor.schema.json)
- [FSL help pages](https://childmindresearch.github.io/help-pages-fsl/)
- [FSL wiki](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)
- [Freesurfer wiki](https://surfer.nmr.mgh.harvard.edu/fswiki)
- [AFNI documentation](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/index.html)

## Index

| Framework | Interface |
| --- | --- |
| afni | [Automask](descriptors/afni/automask.json) |
|  | [Bandpass](descriptors/afni/bandpass.json) |
|  | [BlurToFWHM](descriptors/afni/blur_to_fwhm.json) |
|  | [Calc](descriptors/afni/calc.json) |
|  | [DegreeCentrality](descriptors/afni/degree_centrality.json) |
|  | [Despike](descriptors/afni/despike.json) |
|  | [Detrend](descriptors/afni/detrend.json) |
|  | [ECM](descriptors/afni/ecm.json) |
|  | [LFCD](descriptors/afni/lfcd.json) |
|  | [Maskave](descriptors/afni/maskave.json) |
|  | [MaskTool](descriptors/afni/mask_tool.json) |
|  | [Refit](descriptors/afni/refit.json) |
|  | [Resample](descriptors/afni/resample.json) |
|  | [ROIStats](descriptors/afni/roistats.json) |
|  | [SkullStrip](descriptors/afni/skull_strip.json) |
|  | [TCat](descriptors/afni/tcat.json) |
|  | [TCorr1D](descriptors/afni/tcorr1_d.json) |
|  | [TCorrelate](descriptors/afni/tcorrelate.json) |
|  | [TProject](descriptors/afni/tproject.json) |
|  | [TShift](descriptors/afni/tshift.json) |
|  | [TStat](descriptors/afni/tstat.json) |
|  | [Unifize](descriptors/afni/unifize.json) |
|  | [Volreg](descriptors/afni/volreg.json) |
| ants | [ApplyTransforms](descriptors/ants/apply_transforms.json) |
|  | [Atropos](descriptors/ants/atropos.json) |
|  | [DenoiseImage](descriptors/ants/denoise_image.json) |
|  | [MultiplyImages](descriptors/ants/multiply_images.json) |
|  | [N4BiasFieldCorrection](descriptors/ants/n4_bias_field_correction.json) |
|  | [Registration](descriptors/ants/registration.json) |
| c3 | [C3dAffineTool](descriptors/c3/c3d_affine_tool.json) |
| freesurfer | [ApplyVolTransform](descriptors/freesurfer/apply_vol_transform.json) |
|  | [Binarize](descriptors/freesurfer/binarize.json) |
|  | [ReconAll](descriptors/freesurfer/recon_all.json) |
| fsl | [ApplyMask](descriptors/fsl/apply_mask.json) |
|  | [ApplyWarp](descriptors/fsl/apply_warp.json) |
|  | [BET](descriptors/fsl/bet.json) |
|  | [BinaryMaths](descriptors/fsl/binary_maths.json) |
|  | [Cluster](descriptors/fsl/cluster.json) |
|  | [ConvertWarp](descriptors/fsl/convert_warp.json) |
|  | [ConvertXFM](descriptors/fsl/convert_xfm.json) |
|  | [DilateImage](descriptors/fsl/dilate_image.json) |
|  | [EpiReg](descriptors/fsl/epi_reg.json) |
|  | [ErodeImage](descriptors/fsl/erode_image.json) |
|  | [ExtractROI](descriptors/fsl/extract_roi.json) |
|  | [FAST](descriptors/fsl/fast.json) |
|  | [FLAMEO](descriptors/fsl/flameo.json) |
|  | [FLIRT](descriptors/fsl/flirt.json) |
|  | [FNIRT](descriptors/fsl/fnirt.json) |
|  | [FUGUE](descriptors/fsl/fugue.json) |
|  | [GLM](descriptors/fsl/glm.json) |
|  | [ICA_AROMA](descriptors/fsl/ica_aroma.json) |
|  | [ImageMaths](descriptors/fsl/image_maths.json) |
|  | [ImageStats](descriptors/fsl/image_stats.json) |
|  | [InvWarp](descriptors/fsl/inv_warp.json) |
|  | [MathsCommand](descriptors/fsl/maths_command.json) |
|  | [MCFLIRT](descriptors/fsl/mcflirt.json) |
|  | [MeanImage](descriptors/fsl/mean_image.json) |
|  | [Merge](descriptors/fsl/merge.json) |
|  | [MultiImageMaths](descriptors/fsl/multi_image_maths.json) |
|  | [Overlay](descriptors/fsl/overlay.json) |
|  | [PrepareFieldmap](descriptors/fsl/prepare_fieldmap.json) |
|  | [Randomise](descriptors/fsl/randomise.json) |
|  | [RobustFOV](descriptors/fsl/robust_fov.json) |
|  | [Slice](descriptors/fsl/slice.json) |
|  | [Slicer](descriptors/fsl/slicer.json) |
|  | [SmoothEstimate](descriptors/fsl/smooth_estimate.json) |
|  | [Split](descriptors/fsl/split.json) |
|  | [SwapDimensions](descriptors/fsl/swap_dimensions.json) |
|  | [Threshold](descriptors/fsl/threshold.json) |
|  | [UnaryMaths](descriptors/fsl/unary_maths.json) |
| workbench | [WBCommand](descriptors/workbench/wbcommand.json) |
