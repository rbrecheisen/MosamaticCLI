@echo off

setlocal

@REM set IMAGES_DIR="G:\My Drive\data\Mosamatic\testdata\L3"
set IMAGES_DIR="D:\Mosamatic\CLI\Output\\RescaleDicomFilesTask"
@REM set SEGMENTATIONS_DIR="G:\My Drive\data\Mosamatic\testdata\L3"
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