import pytest


def solution(N):
    current_number = N
    count_flag = False
    zero_count = 0
    max_zero_count = zero_count
    for i in range(32, 0, -1):
        divisor = 2 ** i
        if divisor > current_number:
            zero_count += 1 if count_flag else zero_count
            if zero_count > max_zero_count:
                max_zero_count = zero_count
            continue
        count_flag = True
        remainder = current_number % divisor
        quotient = current_number // divisor
        if remainder == 0 and quotient == 1:
            break
        elif quotient > 0:
            zero_count = 0
        current_number = remainder
    return max_zero_count


@pytest.mark.parametrize(
    'N,result',
    [
        (9, 2),
        (529, 4),
        (32, 0),
        (15, 0),
        (20, 1),
        (1041, 5),
    ]
)
def test_solution(N, result):
    assert solution(N) == result
