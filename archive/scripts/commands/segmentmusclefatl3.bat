@echo off

setlocal

@REM KU LEUVEN T4 FRANCESCA
set IMAGES_DIR="L:\FHML_SURGERY\AImodel\T4\KU_Leuven"
set MODEL_FILES_DIR="G:\My Drive\data\Mosamatic\models\pytorch\2.2\L3"
set MODEL_VERSION="2.2"
set OUTPUT_DIR="D:\Mosamatic\CLI\Output"
set OVERWRITE="true"

del pyproject.toml
copy pyproject.toml.windows pyproject.toml

poetry run mosamatic segmentmusclefatl3 ^
    --images_dir %IMAGES_DIR% ^
    --model_files_dir %MODEL_FILES_DIR% ^
    --model_version %MODEL_VERSION% ^
    --output_dir %OUTPUT_DIR% ^
    --overwrite %OVERWRITE%

endlocal