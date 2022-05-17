import pytest


def solution(arr):
    arr_sum = 0
    max_element = len(arr)
    expected_sum = (max_element * (max_element + 1) // 2)
    for i in range(len(arr)):
        arr_sum += arr[i]

    return max_element + 1 - (arr_sum - expected_sum)


@pytest.mark.parametrize(
    'arr, result',
    [
        ([2, 3, 1, 5], 4),
        ([2, 3, 1, 5, 6], 4),
        ([2, 3, 4, 5, 6], 1),
        ([4, 3, 1, 5, 6], 2),
        ([4, 3, 1, 6, 2], 5),
        ([4, 3, 1, 5, 2], 6),
        ([], 1),
    ]
)
def test_solution(arr, result):
    assert solution(arr) == result
