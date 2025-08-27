@echo off

copy /Y pyproject.toml.windows pyproject.toml

for /f "usebackq tokens=* delims=" %%a in ("requirements-win.txt") do (
    echo %%a
    poetry add %%a
)

copy /Y pyproject.toml pyproject.toml.windows