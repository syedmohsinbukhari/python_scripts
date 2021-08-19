import pytest


def solution_on2(n, arr):
    counters = []
    for i in range(n):
        counters.append(0)

    max_ele = float('-inf')
    for ele in arr:
        if ele > n:
            for i in range(n):
                counters[i] = max_ele
        else:
            counters[ele - 1] += 1
            if counters[ele - 1] > max_ele:
                max_ele = counters[ele - 1]

    return counters


def solution_better(n, arr):
    counters = [0 for _ in range(n)]

    max_ele = float('-inf')
    prev_max_ele = max_ele
    for ele in arr:
        if ele > n:
            prev_max_ele = max_ele
        else:
            if counters[ele - 1] < prev_max_ele:
                counters[ele - 1] = prev_max_ele + 1
            else:
                counters[ele - 1] += 1

            if counters[ele - 1] > max_ele:
                max_ele = counters[ele - 1]

    for i in range(n):
        if counters[i] < prev_max_ele:
            counters[i] = prev_max_ele

    return counters


@pytest.mark.parametrize(
    "n, arr, result",
    [
        (5, [4, 1, 4, 3, 6, 2, 2, 2, 5], [2, 5, 2, 2, 3]),
        (4, [4, 1, 4, 3, 5, 2, 2, 2, 5], [5, 5, 5, 5]),
    ]
)
def test_solution(n, arr, result):
    assert solution_on2(n, arr) == result
    assert solution_better(n, arr) == result
