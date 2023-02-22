from dataclasses import dataclass


@dataclass(frozen=True, init=False)
class URL:
    external_backend: str = "http://localhost:3000"
    base_url: str = "http://frontend:3001"
    login: str = "/login"
    users: str = "/usuarios"
    register: str = "/cadastrarusuarios"
