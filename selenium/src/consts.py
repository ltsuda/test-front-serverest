from dataclasses import dataclass


@dataclass(frozen=True, init=False, slots=True)
class URL:
    login: str = "/login"
    users: str = "/usuarios"
