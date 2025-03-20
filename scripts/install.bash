#!/usr/bin/env bash

set -e
set -x

uv pip install -r pyproject.toml --group dev
