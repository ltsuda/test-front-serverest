from enum import StrEnum, auto


class URL(StrEnum):
    external_backend = "http://localhost:3000"
    backend_users = "/usuarios"
    base_url = "http://frontend:3001"
    login = "/login"
    register = "/cadastrarusuarios"
    user_home = "/home"
    admin_home = "/admin/home"


class Pages(StrEnum):
    LOGIN = auto()
    REGISTER = auto()
    USER_HOME = auto()
    ADMIN_HOME = auto()
