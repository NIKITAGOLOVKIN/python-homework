from bubble_sort import bubble_sort


def test_bubble_sort_basic():
    test_cases = [
        [4, 2, 1, 3],
        [1, 3, 2],
        [5, 1, 4, 2, 8],
    ]

    for arr in test_cases:
        expected = sorted(arr)
        arr = bubble_sort(arr)
        assert arr == expected

def test_empty_array():
    arr = []
    arr = bubble_sort(arr)
    assert arr == []

def test_single_element():
    arr = [42]
    arr = bubble_sort(arr)
    assert arr == [42]

def test_two_elements():
    test_cases = [
        [1, 2],
        [2, 1],
        [2, 2],
    ]

    for arr in test_cases:
        expected = sorted(arr)
        arr = bubble_sort(arr)
        assert arr == expected

def test_already_sorted():
    arr = [1, 2, 3, 4, 5]
    arr = bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    arr = bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_all_identical():
    test_cases = [
        [1, 1, 1],
        [0, 0, 0, 0],
        [-1, -1, -1],
    ]

    for arr in test_cases:
        expected = arr
        arr = bubble_sort(arr)
        assert arr == expected

def test_with_duplicates():
    test_cases = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [1, 2, 3, 2, 1],
        [5, 5, 3, 3, 1, 1],
    ]

    for arr in test_cases:
        expected = sorted(arr)
        arr = bubble_sort(arr)
        assert arr == expected

def test_negative_numbers():
    test_cases = [
        [-3, -1, -2],
        [3, -1, 0, -2, 5],
        [-5, -5, -3, -10],
    ]

    for arr in test_cases:
        expected = sorted(arr)
        arr = bubble_sort(arr)
        assert arr == expected

def test_floats():
    arr = [3.14, 1.41, 2.71, 0.0, -1.0]
    expected = sorted(arr)
    arr = bubble_sort(arr)
    assert arr == expected