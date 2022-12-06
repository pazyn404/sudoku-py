from typing import Iterable, Any


class Enumerator:
    def __init__(self, obj: Iterable) -> None:
        self._obj_iterator = iter(obj)
        self._current = None

    def move_next(self) -> bool:
        try:
            self._current = next(self._obj_iterator)
        except StopIteration:
            return False

        return True

    @property
    def current(self) -> Any:
        return self._current
