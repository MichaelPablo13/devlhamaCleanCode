from typing import Dict
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface

class UserFinder(UserFinderInterface):
    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self._users_repository = user_repository
        
    def find(self, first_name: str) -> Dict:
        pass
