from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str
    DATABASE_PASSWORD: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        if value not in ("dev", "test", "prod"):
            raise ValueError(
                f"ENVIRONMENT musi być jednym z: 'dev', 'test', 'prod'. Dostałeś: {value}"
            )
        return value
