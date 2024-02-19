from .users_repository import UsersRepository

def test_insert_user():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 34

    user_repository = UsersRepository()
    user_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)
