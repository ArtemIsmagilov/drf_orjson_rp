#!/usr/bin/env bash

set -e
set -x

basedpyright
ruff check
ruff format --check
