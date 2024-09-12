# Extracting lists of commands from software packages

In the docker containers:

## FSL

```bash
ls $FSLDIR/bin > /out/fsl_commands.txt
```

## AFNI

```bash
apsearch -list_all_afni_progs > /out/afni_commands.txt
```

## ANTS

```bash
ls /opt/ants/bin > /out/ants_commands.txt
```

## FreeSurfer

```bash
ls /usr/lib/freesurfer/bin > /out/freesurfer_commands.txt
```
