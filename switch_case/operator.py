import operator
from typing import Any, Callable

from .curry import curry


class Operator:
    def __eq__(self, other: Any) -> Callable[[Any], bool]:  # type: ignore
        return curry(operator.eq, other)

    def __ne__(self, other: Any) -> Callable[[Any], bool]:  # type: ignore
        return curry(operator.ne, other)

    def __lt__(self, other: Any) -> Callable[[Any], bool]:  # type: ignore
        return curry(operator.lt, other)

    def __le__(self, other: Any) -> Callable[[Any], bool]:  # type: ignore
        return curry(operator.le, other)

    def __gt__(self, other: Any) -> Callable[[Any], bool]:  # type: ignore
        return curry(operator.gt, other)

    def __ge__(self, other: Any) -> Callable[[Any], bool]:  # type: ignore
        return curry(operator.ge, other)

    def __call__(self, fn: Callable, *args: Any, **kwargs: Any) -> Callable:
        return curry(fn, *args, **kwargs)
