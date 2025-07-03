@echo off

setlocal

copy /Y pyproject.toml.windows pyproject.toml

@REM poetry run pytest -s
pytest -s

endlocal