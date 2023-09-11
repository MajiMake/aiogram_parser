from dataclasses import dataclass
from environs import Env


@dataclass
class ClientBot:
    cl_id: int  # Токен для доступа к телеграм-боту
    cl_hash: str


@dataclass
class Config:
    cl_bot: ClientBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(cl_bot=ClientBot(
        cl_id=env('API_ID'),
        cl_hash=env('API_HASH')
    ))
