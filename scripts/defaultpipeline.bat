@echo off

setlocal

SET INPUT=%1%
SET MODEL_FILES=%2%
SET OUTPUT=%3%


poetry run mosamatic decompressdicomfiles --input %INPUT% --output %OUTPUT% --overwrite=true

set NEXT_INPUT=%OUTPUT%\DecompressDicomFilesTask
poetry run mosamatic rescaledicomfiles --input %NEXT_INPUT% --output %OUTPUT% --params target_size=512 --overwrite=true

set NEXT_INPUT=%OUTPUT%\RescaleDicomFilesTask
poetry run mosamatic segmentmusclefatl3 --input images=%NEXT_INPUT% --input model_files=%MODEL_FILES% --output %OUTPUT% --params model_version=2.2 --overwrite=true

endlocal