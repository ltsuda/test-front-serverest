import pytest
from src.fixtures.api import create_account  # noqa
from src.keywords.user_data import UserData
from src.model.user import UserWithIDProtocol


@pytest.fixture(scope="function")
def regular_user() -> UserData:
    return UserData(as_admin=False)


@pytest.fixture(scope="function")
def admin_user() -> UserData:
    return UserData(as_admin=True)


@pytest.fixture(scope="function")
def user_account(regular_user, create_account) -> UserWithIDProtocol:  # noqa
    return create_account(regular_user.data())


@pytest.fixture(scope="function")
def admin_account(admin_user, create_account) -> UserWithIDProtocol:  # noqa
    return create_account(admin_user.data())
