@echo off

setlocal

rmdir /s /q .venv

del poetry.lock

copy /Y pyproject.toml.windows pyproject.toml

poetry cache clear pypi --all
poetry update
poetry install

endlocal