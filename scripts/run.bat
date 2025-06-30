@echo off

setlocal

del pyproject.toml
copy pyproject.toml.windows pyproject.toml

poetry run mosamatic

endlocal