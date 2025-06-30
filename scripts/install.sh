#!/bin/bash

rm -rf ./.venv

rm poetry.lock
rm pyproject.toml
cp pyproject.toml.macos pyproject.toml

poetry cache clear pypi --all
poetry update
poetry install