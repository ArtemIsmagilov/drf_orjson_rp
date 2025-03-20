#!/usr/bin/env bash

set -e
set -x

coverage run -m tests.doc_test
coverage report -m
