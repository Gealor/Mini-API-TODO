import uvicorn
from fastapi import FastAPI

from controllers import main_router
from core.config import settings
from middlewares import LoggerMiddleware

app = FastAPI(title="Tasks-Service")
app.include_router(main_router)
app.add_middleware(LoggerMiddleware)


if __name__=="__main__":
    uvicorn.run(
        "main:app",
        host = settings.runtime.host,
        port = settings.runtime.port,
        reload = settings.runtime.reload,
    )
