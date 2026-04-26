import time
from typing import Awaitable
from typing import Callable

from fastapi import Request
from fastapi import Response
from starlette.middleware.base import BaseHTTPMiddleware

from core.logger import log


class LoggerMiddleware(BaseHTTPMiddleware):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def dispatch(
        self,
        request: Request,
        call_next : Callable[[Request], Awaitable[Response]]
    ) -> Response:
        start_time = time.time()
        log.info(
            "Начало %s запроса на %s | " \
            "Параметры запроса: %s | " \
            "Параметры пути: %s",
            request.method, request.url.path,
            dict(request.query_params), request.path_params,
        )
        response = await call_next(request)
        process_time = time.time() - start_time
        log.info(
            "Ответ %d %s запроса на %s | " \
            "Время: %.3f",
            response.status_code, request.method, request.url.path, process_time
        )
        return response
