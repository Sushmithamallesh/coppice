from pydantic_settings import BaseSettings

class Config(BaseSettings):
    metaphor_key: str
    mongo_uri: str

    class Config:
        env_file = "../.env"

config = Config()
