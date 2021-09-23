"""Contains various fixtures, especially pre-written problems."""

from pytest import fixture

from core import Problem, problem
from core import test_case as case  # renamed so pytest doesn't run it as a test


@fixture(name="square")
def fixture_square() -> Problem:
    """Generate a basic, correct implementation of a square problem."""

    @case(4)
    @case(2, output=4)
    @case(-2, output=4)
    @problem
    def square(x: int) -> int:
        """Square x."""
        return x * x

    return square


@fixture(name="diff")
def fixture_diff() -> Problem:
    """Generate a basic, correct implementation of a difference problem."""

    @case(17, 10)
    @case(2, 4, output=-2)
    @case(3, 1, output=2)
    @problem
    def difference(x: int, y: int) -> int:
        """Compute x - y."""
        return x - y

    return difference


@fixture(name="diff_bad_gt")
def fixture_diff_bad_gt(diff) -> Problem:
    """Generate an implementation of difference with an incorrect golden test."""
    return case(3, 1, output=1)(diff)


@fixture(name="diff_bad_impl")
def fixture_diff_bad_impl() -> Problem:
    """Generate a difference problem with an incorrect implementation."""

    @case(17, 10)
    @case(2, 4, output=-2)
    @case(3, 1, output=2)
    @problem
    def diff_should_fail(x: int, y: int) -> int:
        """Compute x - y."""
        return x + y

    return diff_should_fail
