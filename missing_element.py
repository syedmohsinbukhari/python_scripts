import pytest


def solution(arr):
    arr_sum = 0
    expected_sum = 0
    max_element = -1 * float('inf')
    for i in range(len(arr)):
        expected_sum += (i + 1)
        arr_sum += arr[i]
        if arr[i] > max_element:
            max_element = arr[i]

    if arr_sum == expected_sum:
        return None
    else:
        return max_element - (arr_sum - expected_sum)


@pytest.mark.parametrize(
    'arr, result',
    [
        ([2, 3, 1, 5], 4),
        ([2, 3, 1, 5, 6], 4),
        ([2, 3, 4, 5, 6], 1),
        ([4, 3, 1, 5, 6], 2),
    ]
)
def test_solution(arr, result):
    assert solution(arr) == result
