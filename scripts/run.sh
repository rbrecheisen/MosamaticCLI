#!/bin/bash

rm pyproject.toml
cp pyproject.toml.macos pyproject.toml

poetry run mosamatic