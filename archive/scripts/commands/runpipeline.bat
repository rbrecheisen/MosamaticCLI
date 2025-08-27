@echo off

setlocal

set IMAGES_DIR="G:\My Drive\data\Mosamatic\testdata\L3"
set MODEL_FILES_DIR="G:\My Drive\data\Mosamatic\models\tensorflow\1.0\L3"
set TARGET_SIZE="512"
set MODEL_TYPE="tensorflow"
set MODEL_VERSION="1.0"
set FIG_WIDTH="10"
set FIG_HEIGHT="10"
set FULL_SCAN="false"
set OUTPUT_DIR="D:\Mosamatic\CLI\Output"
set OVERWRITE="true"

del pyproject.toml
copy pyproject.toml.windows pyproject.toml

poetry run mosamatic runpipeline ^
    --images_dir %IMAGES_DIR% ^
    --model_files_dir %MODEL_FILES_DIR% ^
    --target_size %TARGET_SIZE% ^
    --model_type %MODEL_TYPE% ^
    --model_version %MODEL_VERSION% ^
    --fig_width %FIG_WIDTH% ^
    --fig_height %FIG_HEIGHT% ^
    --full_scan %FULL_SCAN% ^
    --output_dir %OUTPUT_DIR% ^
    --overwrite %OVERWRITE%

endlocal