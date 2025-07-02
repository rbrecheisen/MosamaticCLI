#!/bin/bash

rm -rf ./.venv

rm poetry.lock

cp -f pyproject.toml.macos pyproject.toml

poetry cache clear pypi --all
poetry update
poetry install