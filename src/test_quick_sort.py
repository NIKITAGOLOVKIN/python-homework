from quick_sort import separation, quick_sort


def test_separation():
    arr = [10, 5, 3, 2, 4]
    separation(arr, 0, len(arr) - 1)
    assert arr == [3, 2, 4, 5, 10]

def test_quick_sort_basic():
    test_cases = [
        [4, 2, 1, 3],
        [1, 3, 2],
        [5, 1, 4, 2, 8],
    ]

    for arr in test_cases:
        expected = sorted(arr)
        quick_sort(arr, 0, len(arr) - 1)
        assert arr == expected

def test_empty_array():
    arr = []
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == []

def test_single_element():
    arr = [42]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [42]

def test_two_elements():
    test_cases = [
        [1, 2],
        [2, 1],
        [2, 2],
    ]

    for arr in test_cases:
        expected = sorted(arr)
        quick_sort(arr, 0, len(arr) - 1)
        assert arr == expected

def test_already_sorted():
    arr = [1, 2, 3, 4, 5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5]

def test_all_identical():
    test_cases = [
        [1, 1, 1],
        [0, 0, 0, 0],
        [-1, -1, -1],
    ]

    for arr in test_cases:
        expected = arr
        quick_sort(arr, 0, len(arr) - 1)
        assert arr == expected

def test_with_duplicates():
    test_cases = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [1, 2, 3, 2, 1],
        [5, 5, 3, 3, 1, 1],
    ]

    for arr in test_cases:
        expected = sorted(arr)
        quick_sort(arr, 0, len(arr) - 1)
        assert arr == expected

def test_negative_numbers():
    test_cases = [
        [-3, -1, -2],
        [3, -1, 0, -2, 5],
        [-5, -5, -3, -10],
    ]

    for arr in test_cases:
        expected = sorted(arr)
        quick_sort(arr, 0, len(arr) - 1)
        assert arr == expected

def test_floats():
    arr = [3.14, 1.41, 2.71, 0.0, -1.0]
    expected = sorted(arr)
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == expected

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def test_against_other_sorts():
        arr = [1, 5, 2, 4, 3]
        assert bubble_sort(arr) == quick_sort(arr, 0, len(arr) - 1)