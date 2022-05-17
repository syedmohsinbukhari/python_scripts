import pytest


def solution_on_on(arr):
    sum_till_now = 0
    sum_arr = [sum_till_now, ]
    for i in range(len(arr)):
        sum_till_now += arr[i]
        sum_arr.append(sum_till_now)

    actual_minimum = float('inf')
    for i in range(len(sum_arr) - 1):
        current_difference = abs(sum_arr[i] - abs(sum_arr[i] - sum_till_now))
        if current_difference < actual_minimum:
            actual_minimum = current_difference

    return actual_minimum


def solution_on_o1(arr):
    sum_left = arr[0]
    sum_right = sum(arr[1:])
    diff = abs(sum_right - sum_left)
    for i in range(1, len(arr) - 1):
        sum_left += arr[i]
        sum_right -= arr[i]
        current_difference = abs(sum_right - sum_left)
        if current_difference < diff:
            diff = current_difference

    return diff


@pytest.mark.parametrize(
    'arr, result',
    [
        ([2, 3, 1, 4], 0),
        ([3, 1, 2, 4, 3], 1),
        ([-3, 1, 2, -4, 3], 1),
        ([-3, 2, 2, -1, 3], 1),
    ]
)
def test_solution(arr, result):
    assert solution_on_on(arr) == result
    assert solution_on_o1(arr) == result
