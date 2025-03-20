from io import BytesIO
from typing import Optional

import orjson
from rest_framework import renderers
from rest_framework.parsers import BaseParser, ParseError


class ORJSONParser(BaseParser):
    """
    Parses JSON-serialized data.
    Parsing with orjson.
    >>> ORJSONParser().parse(BytesIO(b"{}")) == {}
    True
    >>> ORJSONParser().parse(BytesIO(b"wrong"))
    Traceback (most recent call last):
        ...
    rest_framework.exceptions.ParseError: JSON parse error - unexpected character: line 1 column 1 (char 0)
    """  # noqa: E501

    media_type = "application/json"
    renderer_class = renderers.JSONRenderer

    def parse(
        self,
        stream: BytesIO,
        media_type: Optional[str] = None,
        parser_context: Optional[dict] = None,
    ):
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        try:
            return orjson.loads(stream.read())
        except ValueError as exc:
            raise ParseError(f"JSON parse error - {exc}") from exc
