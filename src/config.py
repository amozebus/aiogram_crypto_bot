from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    TELEGRAM_BOT_API_TOKEN: str
    CMC_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()