@echo off

setlocal

@REM TEST DATA
@REM set IMAGES_DIR="G:\My Drive\data\Mosamatic\testdata\L3"
@REM set SEGMENTATIONS_DIR="G:\My Drive\data\Mosamatic\testdata\L3"
@REM set OUTPUT_DIR="D:\Mosamatic\CLI\Output"
@REM set FILE_TYPE="tag"
@REM set OVERWRITE="true"

@REM KU LEUVEN T4 FRANCESCA
set IMAGES_DIR="D:\Mosamatic\CLI\Output\\RescaleDicomFilesTask"
set SEGMENTATIONS_DIR="D:\Mosamatic\CLI\Output\\CopyFilesTask"
set OUTPUT_DIR="D:\Mosamatic\CLI\Output"
set FILE_TYPE="tag"
set OVERWRITE="true"

del pyproject.toml
copy pyproject.toml.windows pyproject.toml

poetry run mosamatic calculatescores ^
    --images_dir %IMAGES_DIR% ^
    --segmentations_dir %SEGMENTATIONS_DIR% ^
    --output_dir %OUTPUT_DIR% ^
    --file_type %FILE_TYPE% ^
    --overwrite %OVERWRITE%

endlocal