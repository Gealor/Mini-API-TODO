import logging
from pathlib import Path
from typing import Annotated

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

SRC_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = SRC_DIR.parent
ENV_FILE = ROOT_DIR / ".env"
ENV_TEMPLATE_FILE = ROOT_DIR / ".env.template"

class RuntimeSettings(BaseModel):
    host: Annotated[str, Field(default='0.0.0.0', alias="HOST")]
    port: Annotated[int, Field(default=8000, alias="PORT")]
    reload: Annotated[bool, Field(default=True, alias="RELOAD")]

class LoggerSettings(BaseModel):
    LOG_DEFAULT_FORMAT: str = (
        "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
    )
    level: int = logging.INFO
    datefmt: str = "%Y-%m-%d %H:%M:%S"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(ENV_TEMPLATE_FILE, ENV_FILE),
        case_sensitive=False,
        env_nested_delimiter="__",
        extra="ignore",
    )

    runtime: RuntimeSettings
    log: LoggerSettings = LoggerSettings()

settings = Settings()

