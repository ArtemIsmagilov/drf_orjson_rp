import doctest

from drf_orjson_rp import parsers, renders

doctest.testmod(parsers)
doctest.testmod(renders)
