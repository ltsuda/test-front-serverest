from dataclasses import dataclass
from typing import Protocol


@dataclass(slots=True)
class User:
    name: str
    email: str
    password: str
    as_admin: bool


class UserProtocol(Protocol):
    name: str
    email: str
    password: str
    as_admin: bool
