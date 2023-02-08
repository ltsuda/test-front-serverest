from dataclasses import dataclass, field

from faker import Faker
from src.model.user import User, UserProtocol

fake = Faker()


@dataclass(slots=True)
class UserData:
    first_name: str = field(init=False, default=fake.first_name())
    last_name: str = field(init=False, default=fake.last_name())
    password: str = field(init=False, default=fake.md5())
    full_name: str = field(init=False)
    email: str = field(init=False)
    as_admin: bool = False

    def __post_init__(self):
        self.full_name: str = f"{self.first_name} {self.last_name}"
        self.email: str = (
            f"{self.first_name[0].lower()}{self.last_name.lower()}-"
            f"{fake.unix_time()}@{fake.free_email_domain()}"
        )

    def data(self) -> UserProtocol:
        return User(self.full_name, self.email, self.password, self.as_admin)
