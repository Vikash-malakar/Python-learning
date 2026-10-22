from typing import TypeVar, Generic, Optional

T = TypeVar("T")

class Repository(Generic[T]):

    def __init__(self):
        self._storage: dict[int, T] = {}

    def add(self, key: int, value: T) -> None:
        self._storage[key] = value

    def get(self, key: int) -> Optional[T]:
        return self._storage.get(key)

    def get_all(self) -> list[T]:
        return list(self._storage.values())


users = Repository[dict]()

users.add(1, {"name": "Vikash", "role": "Developer"})
users.add(2, {"name": "Aman", "role": "Admin"})

print(users.get(1))
print(users.get_all())