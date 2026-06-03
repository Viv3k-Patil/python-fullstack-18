from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator
from functools import lru_cache


class Settings(BaseSettings):
    # ── App ──────────────────────────────────────────────
    app_name: str = "file-service"
    app_version: str = "0.1.0"
    app_env: str = "development"
    debug: bool = True

    # ── Server ───────────────────────────────────────────
    host: str = "0.0.0.0"
    port: int = 8001

    # ── Database ─────────────────────────────────────────
    database_user: str
    database_password: str
    database_url: str = ""                      # ✅ plain field, built by validator

    @model_validator(mode="after")              # ✅ runs after all fields are loaded
    def build_database_url(self):
        self.database_url = (
            f"postgresql+asyncpg://{self.database_user}:{self.database_password}"
            "@ep-quiet-voice-aplrv8k0-pooler.c-7.us-east-1.aws.neon.tech/neondb"
            "?ssl=require"
        )
        return self

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def is_production(self) -> bool:
        return self.app_env == "production"

    @property
    def is_development(self) -> bool:
        return self.app_env == "development"


@lru_cache
def get_settings() -> Settings:
    return Settings()