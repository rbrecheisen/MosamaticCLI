@echo off

setlocal

@REM KU LEUVEN T4 FRANCESCA
set IMAGES_DIR="L:\FHML_SURGERY\AImodel\T4\KU_Leuven"
set OUTPUT_DIR="D:\Mosamatic\CLI\Output"
set OVERWRITE="true"

del pyproject.toml
copy pyproject.toml.windows pyproject.toml

poetry run mosamatic decompressdicomfiles ^
    --images_dir %IMAGES_DIR% ^
    --output_dir %OUTPUT_DIR% ^
    --overwrite %OVERWRITE%

endlocal