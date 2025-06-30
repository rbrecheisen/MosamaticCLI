@echo off

setlocal

set INPUT_DIR="L:\FHML_SURGERY\AImodel\T4\KU_Leuven"
set OUTPUT_DIR="D:\Mosamatic\CLI\Output"
set EXTENSION="tag"
set FILE_TYPE="none"
set OVERWRITE="true"

del pyproject.toml
copy pyproject.toml.windows pyproject.toml

poetry run mosamatic copyfiles ^
    --input_dir %INPUT_DIR% ^
    --output_dir %OUTPUT_DIR% ^
    --extension %EXTENSION% ^
    --file_type %FILE_TYPE% ^
    --overwrite %OVERWRITE%

endlocal