from typing import Any, Optional

import orjson
from rest_framework.renderers import BaseRenderer
from rest_framework.settings import api_settings
from rest_framework.utils import encoders


class ORJSONRenderer(BaseRenderer):
    """
    Renderer which serializes to JSON.
    Rendering with orjson.

    >>> ORJSONRenderer().render(None) == b""
    True
    >>> ORJSONRenderer().render({}) == b"{}"
    True
    >>> api_settings.user_settings["ORJSON_RENDERER_OPTION"] = orjson.OPT_APPEND_NEWLINE
    >>> ORJSONRenderer().render({}) == b"{}\\n"
    True
    """  # noqa: E501

    media_type = "application/json"
    format = "json"
    encoder_class = encoders.JSONEncoder

    # We don't set a charset because JSON is a binary encoding,
    # that can be encoded as utf-8, utf-16 or utf-32.
    # See: https://www.ietf.org/rfc/rfc4627.txt
    # Also: http://lucumr.pocoo.org/2013/7/19/application-mimetypes-and-encodings/
    charset = None

    def render(
        self,
        data: Any,
        accepted_media_type: Optional[str] = None,
        renderer_context: Optional[dict] = None,
    ) -> bytes:
        """
        Render `data` into JSON, returning a bytestring.
        """
        if data is None:
            return b""

        option = api_settings.user_settings.get("ORJSON_RENDERER_OPTION")

        return orjson.dumps(
            data,
            default=self.encoder_class().default,
            option=option,
        )
