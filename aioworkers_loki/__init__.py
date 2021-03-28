from pathlib import Path
from queue import Queue
from typing import Mapping, Sequence, Union

import logging_loki

__version__ = "0.0.0"

BASE = Path(__file__).parent

configs = (BASE / "config.ini",)


class Handler(logging_loki.LokiQueueHandler):
    def __init__(
        self,
        url: str = None,
        host: str = "localhost:3100",
        tags: Mapping[str, str] = None,
        auth: Union[Sequence, Mapping] = None,
        version: str = "1",
    ):
        self._queue: Queue = Queue()
        if auth and isinstance(auth, Mapping):
            username = auth.get("username") or auth.get("user")
            password = auth.get("password")
            auth = (username, password)
        if isinstance(version, int):
            version = str(version)
        if not url and host:
            url = f"http://{host}/loki/api/v1/push"
        super().__init__(
            self._queue,
            url=url,
            tags=tags,
            auth=auth,
            version=version,
        )
