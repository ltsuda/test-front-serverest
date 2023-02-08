from dataclasses import dataclass


@dataclass(frozen=True, init=False, slots=False)
class URL:
    external_backend: str = "http://localhost:3000"
    login: str = "/login"
    users: str = "/usuarios"
