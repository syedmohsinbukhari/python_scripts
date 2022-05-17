import pytest


def solution(A):
    ref_dict = {}
    for ele in A:
        ref_dict[ele] = ref_dict[ele] + 1 if ele in ref_dict.keys() else 1

    for ele in A:
        if (ref_dict[ele] % 2) != 0:
            return ele

    return None


@pytest.mark.parametrize(
    'A, result',
    [
        ([9, 3, 9, 3, 9, 7, 9], 7),
        ([9, 3, 9, 3, 9, 7, 7], 9),
        ([8], 8),
    ]
)
def test_solution(A, result):
    assert solution(A) == result
