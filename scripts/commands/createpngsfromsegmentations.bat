@echo off

setlocal

@REM KU LEUVEN T4 FRANCESCA
set IMAGES_DIR="L:\FHML_SURGERY\AImodel\T4\KU_Leuven"
set SEGMENTATIONS_DIR="D:\Mosamatic\CLI\Output\SegmentMuscleFatL3TensorFlowTask"
set FIG_WIDTH="10"
set FIG_HEIGHT="10"
set OUTPUT_DIR="D:\Mosamatic\CLI\Output"
set OVERWRITE="true"

del pyproject.toml
copy pyproject.toml.windows pyproject.toml

poetry run mosamatic createpngsfromsegmentations ^
    --images_dir %IMAGES_DIR% ^
    --segmentations_dir %SEGMENTATIONS_DIR% ^
    --fig_width %FIG_WIDTH% ^
    --fig_height %FIG_HEIGHT% ^
    --output_dir %OUTPUT_DIR% ^
    --overwrite %OVERWRITE%

endlocal