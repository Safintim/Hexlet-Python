import exercises
import challenges


def test_get_square_roots():
    assert exercises.get_square_roots(-1) == []
    assert exercises.get_square_roots(0) == [0]
    assert exercises.get_square_roots(9) == [-3.0, 3.0]


def test_get_square_roots():
    assert exercises.get_range(-5) == []
    assert exercises.get_range(0) == []
    assert exercises.get_range(5) == [0, 1, 2, 3, 4]


def test_duplicate():
    original = [1, 2, 3]
    ref = original[:]
    result = exercises.duplicate(ref)
    assert ref == original * 2
    assert result is None


def test_rotate():
    original = [1, 2, 3]
    ref = original[:]
    result = exercises.rotate(ref)
    assert ref == [3, 1, 2]


def test_rotated_left():
    assert exercises.rotated_left("ABCD") == "BCDA"


def test_rotated_left():
    assert exercises.rotated_right([1, 2, 3, 4]) == [4, 1, 2, 3]


def test_find_index():
    assert exercises.find_index(42, [1, 2, 3]) is None
    assert exercises.find_index(2, []) is None
    assert exercises.find_index(2, [1, 2, 3]) == 1
    assert exercises.find_index("l", "hello") == 2


def test_find_second_index():
    assert exercises.find_second_index('!', '') is None
    assert exercises.find_second_index('!', '!') is None
    assert exercises.find_second_index('n', 'clone') is None
    assert exercises.find_second_index('n', 'banana') == 4
    assert exercises.find_second_index('n', 'cannon') == 3


def test_hamming_weight():
    assert challenges.hamming_weight(0) == 0
    assert challenges.hamming_weight(4) == 1
    assert challenges.hamming_weight(101) == 4


def test_length_of_last_word():
    assert challenges.length_of_last_word('') == 0
    assert challenges.length_of_last_word('man in Black') == 5
    assert challenges.length_of_last_word('hello, world!     ') == 6
