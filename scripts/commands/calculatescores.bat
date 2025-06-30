@echo off

setlocal

set IMAGES_DIR="G:\My Drive\data\Mosamatic\testdata\L3"
set SEGMENTATIONS_DIR="G:\My Drive\data\Mosamatic\testdata\L3"
set OUTPUT_DIR="D:\Mosamatic\CLI\Output"
set FILETYPE="tag"
set OVERWRITE="true"

del pyproject.toml
copy pyproject.toml.windows pyproject.toml

poetry run mosamatic calculatescores ^
    --images_dir %IMAGES_DIR% ^
    --segmentations_dir %SEGMENTATIONS_DIR% ^
    --output_dir %OUTPUT_DIR% ^
    --filetype %FILETYPE% ^
    --overwrite %OVERWRITE%

endlocal