# DRF orjson renderer and parse

[![CI](https://github.com/ArtemIsmagilov/drf_orjson_rp/actions/workflows/ci.yaml/badge.svg)](https://github.com/ArtemIsmagilov/drf_orjson_rp/actions/workflows/ci.yaml)
[![Upload Python Package](https://github.com/ArtemIsmagilov/drf_orjson_rp/actions/workflows/python-publish.yml/badge.svg)](https://github.com/ArtemIsmagilov/drf_orjson_rp/actions/workflows/python-publish.yml)

Rendering and parsing JSON with orjson.
Made on example drf_orjson_renderer package.

## Installation

- Install package

  ```bash
  pip install drf_orjson_rp
  ```

- Rewrite settings by example.

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_RENDERER_CLASSES': [
          # replace default json on orjson renderer
          'drf_orjson_rp.renderers.ORJSONRenderer',
          # defaults
          'rest_framework.renderers.BrowsableAPIRenderer',
      ],
      'DEFAULT_PARSER_CLASSES': [
          # replace default json on orjson parser
          'drf_orjson_rp.parsers.ORJSONParser',
          # defaults
          'rest_framework.parsers.FormParser',
          'rest_framework.parsers.MultiPartParser'
      ],
      # add orjson renderer option
      'ORJSON_RENDERER_OPTION': orjson.OPT_APPEND_NEWLINE | orjson.OPT_INDENT_2,
  }
  ```

- [Check settings by default in source code DRF. DEFAULTS](https://github.com/encode/django-rest-framework/blob/master/rest_framework/settings.py)
- Renderer and parser made by example from source code DRF.
  - [DRF Renderer](https://github.com/encode/django-rest-framework/blob/master/rest_framework/renderers.py)
  - [DRF Parser](https://github.com/encode/django-rest-framework/blob/master/rest_framework/parsers.py)

## Developing

- Clone your fork and cd into the repo directory

```bash
  git clone git@github.com:<your username>/drf_orjson_rp.git
  cd drf_orjson_rp
```

- Create a virtual environment

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

- Install uv and dev dependencies

  ```bash
  pip install uv
  bash scripts/install.bash
  ```

- Run tests

  ```bash
  bash scripts/test.bash
  ```

- Run linters

  ```bash
  bash scripts/lint.bash
  ```

- Run test coverage

  ```bash
  bash scripts/coverage.bash
  ```

## Links

- [drf_ujson_renderer](https://github.com/gizmag/drf-ujson-renderer)
- [drf_orjson_renderer](https://github.com/brianjbuck/drf_orjson_renderer)
- [DRF stubs](https://github.com/typeddjango/djangorestframework-stubs)
- [pydantic workflows](https://github.com/pydantic/pydantic/blob/main/.github/workflows/ci.yml)
- [fastapi scripts](https://github.com/fastapi/fastapi/tree/master/scripts)
