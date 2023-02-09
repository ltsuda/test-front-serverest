from dataclasses import dataclass
from typing import Protocol


@dataclass(slots=True)
class User:
    name: str
    email: str
    password: str
    as_admin: bool

    def data_as_dict(self):
        return {
            "nome": self.name,
            "email": self.email,
            "password": self.password,
            "administrador": "true" if self.as_admin else "false",
        }


@dataclass(slots=True)
class UserWithID:
    name: str
    email: str
    password: str
    _id: str
    as_admin: bool = False


class UserProtocol(Protocol):
    name: str
    email: str
    password: str
    as_admin: bool

    def data_as_dict(self) -> dict:
        ...


class UserWithIDProtocol(Protocol):
    name: str
    email: str
    password: str
    _id: str
    as_admin: bool
