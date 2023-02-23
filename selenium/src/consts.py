from enum import StrEnum


class URL(StrEnum):
    external_backend = "http://localhost:3000"
    backend_users = "/usuarios"
    base_url = "http://frontend:3001"
    login = "/login"
    register = "/cadastrarusuarios"
    user_home = "/admin/home"
    admin_home = "/home"

