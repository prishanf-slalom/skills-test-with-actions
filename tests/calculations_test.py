import sys
import os

import pytest

# Ensure src is on the path so imports work during tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test area with a positive radius."""
    radius = 1
    result = area_of_circle(radius)
    assert abs(result - 3.141592653589793) < 1e-12


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    assert area_of_circle(0) == 0


def test_area_of_circle_negative_radius_raises():
    """area_of_circle should raise on negative radius."""
    with pytest.raises(ValueError):
        area_of_circle(-2)


@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (10, 55),
    (20, 6765),
])
def test_get_nth_fibonacci_values(n, expected):
    """Parametrized tests for several Fibonacci values."""
    assert get_nth_fibonacci(n) == expected


def test_get_nth_fibonacci_negative_raises():
    """get_nth_fibonacci should raise on negative input."""
    with pytest.raises(ValueError):
        get_nth_fibonacci(-5)
