import doctest

from drf_orjson_rp import parsers, renderers

doctest.testmod(parsers)
doctest.testmod(renderers)
