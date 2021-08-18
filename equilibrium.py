import pytest


def solution(arr):
    sum_till_now = 0
    sum_arr = [sum_till_now, ]
    for i in range(len(arr)):
        sum_till_now += arr[i]
        sum_arr.append(sum_till_now)

    index_of_minimum = -1
    actual_minimum = float('inf')
    for i in range(len(sum_arr) - 1):
        current_difference = abs(sum_arr[i] - abs(sum_arr[i] - sum_till_now))
        if current_difference < actual_minimum:
            actual_minimum = current_difference
            index_of_minimum = i

    return index_of_minimum


@pytest.mark.parametrize(
    'arr, result',
    [
        ([2, 3, 1, 4], 2),
        ([3, 1, 2, 4, 3], 3),
        ([-3, 1, 2, -4, 3], 0),
        ([-3, 2, 2, -1, 3], 3),
    ]
)
def test_solution(arr, result):
    assert solution(arr) == result
