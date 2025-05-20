from main import Fibonacci
import pytest


@pytest.fixture
def fibonacci():
    return Fibonacci()


@pytest.mark.parametrize("test, expected", [
    (0, 0),
    (1, 1),
    (10, 55),
    (100, 354224848179261915075),
    (200, 280571172992510140037611932413038677189525),
])
def test_fibonacci_normal(fibonacci, test, expected):
    assert fibonacci(test) == expected


def test_fibonacci_negative(fibonacci):
    with pytest.raises(ValueError, match=f'Positive integer number expected, got "{-1}"'):
        fibonacci(-1)


def test_fibonacci_float(fibonacci):
    with pytest.raises(ValueError, match=f'Positive integer number expected, got "{2.5}"'):
        fibonacci(2.5)


@pytest.mark.parametrize("test", ["", "10", "ten", "."])
def test_fibonacci_str(fibonacci, test):
    with pytest.raises(ValueError, match=f'Positive integer number expected, got "{test}"'):
        fibonacci(test)
