import pytest


def solution(A):
    global_m = float('inf')
    global_s = 0
    for cur_l in [2, 3]:
        for cur_s in range(len(A)-cur_l+1):
            cur_m = sum(A[cur_s:cur_s+cur_l]) / cur_l
            if cur_m < global_m:
                global_m = cur_m
                global_s = cur_s

    return global_s


@pytest.mark.parametrize(
    'A, result',
    [
        ([4, 2, 2, 5, 1, 5, 8], 1),
    ]
)
def test_solution(A, result):
    assert solution(A) == result
