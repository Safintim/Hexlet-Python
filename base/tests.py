import pytest

from binary_sum import binary_sum
from diff import diff
from fibonacci import fib_cycle, fib_recursion
from palindrome import is_palindrome
from power_of_three import is_power_of_three
from rotate_triple import rotate_left, rotate_right
from segments import is_degenerated, is_horizontal, is_inclined, is_vertical

FIBONACCI_CHECK_RESULT = (
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (5, 5),
    (10, 55),
)

PALINDROME_CHECK_RESULT = (
    ('', True),
    ('radar', True),
    ('a', True),
    ('abs', False),
)


@pytest.mark.parametrize('input_number, output_number', FIBONACCI_CHECK_RESULT)
def test_fib_recursion(input_number, output_number):
    assert fib_recursion(input_number) == output_number


@pytest.mark.parametrize('input_number, output_number', FIBONACCI_CHECK_RESULT)
def test_fib_cycle(input_number, output_number):
    assert fib_cycle(input_number) == output_number


def test_binary_sum():
    assert binary_sum('10', '1') == '11'
    assert binary_sum('1101', '101') == '10010'


@pytest.mark.parametrize('input_string, expected', PALINDROME_CHECK_RESULT)
def test_is_palindrome(input_string, expected):
    assert is_palindrome(input_string) == expected


def test_is_degenerated():
    line1 = (0, 10), (100, 130)
    line2 = (0, 10), (0, 10)
    assert is_degenerated(line1) is False
    assert is_degenerated(line2) is True


def test_is_vertical():
    line1 = (42, 1), (42, 2)
    line2 = (41, 1), (42, 1)
    assert is_vertical(line1) is True
    assert is_vertical(line2) is False


def test_is_horizontal():
    line1 = (100, 50), (200, 50)
    line2 = (41, 100), (42, 1)
    assert is_horizontal(line1) is True
    assert is_horizontal(line2) is False


def test_is_inclined():
    line1 = (100, 50), (200, 50)
    line2 = (41, 1), (42, 1)
    line3 = (41, 123), (42, 1)
    assert is_inclined(line1) is False
    assert is_inclined(line2) is False
    assert is_inclined(line3) is True


def test_rotate_left():
    triple = ('A', 'B', 'C')
    assert rotate_left(triple) == ('B', 'C', 'A')


def test_rotate_right():
    triple = ('A', 'B', 'C')
    assert rotate_right(triple) == ('C', 'A', 'B')


def test_is_power_of_three():
    assert is_power_of_three(1) is True
    assert is_power_of_three(2) is False
    assert is_power_of_three(9) is True


def test_diff():
    assert diff(0, 45) == 45
    assert diff(0, 180) == 180
    assert diff(0, 190) == 170
    assert diff(120, 280) == 160