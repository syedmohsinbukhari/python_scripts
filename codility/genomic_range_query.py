import pytest


def solution_onm(S, P, Q):
    imp_f = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    result = []
    for i in range(len(P)):
        first = P[i]
        last = Q[i]

        this_result = float('inf')
        for j in range(first, last + 1):
            neoclotide = S[j]
            if imp_f[neoclotide] < this_result:
                this_result = imp_f[neoclotide]
        result.append(this_result)

    return result


def solution(S, P, Q):
    imp_f = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    min_s = [[i, ] for i in range(len(S))]
    for i in range(len(S) - 2, -1, -1):
        if imp_f[S[i]] >= imp_f[S[i+1]]:
            for ele in min_s[i+1]:
                if imp_f[S[ele]] < imp_f[S[min_s[i][-1]]]:
                    min_s[i] += [ele, ]
        else:
            if imp_f[S[min_s[i][-1]]] > imp_f[S[min_s[i+1][-1]]]:
                min_s[i] += min_s[i+1]

    result = []
    for j in range(len(P)):
        first = P[j]
        last = Q[j]
        result.append([])

        min_arr = min_s[first]
        for k in range(-1, -1 * (len(min_arr) + 1), -1):
            if min_arr[k] <= last:
                result[j] = imp_f[S[min_arr[k]]]
                break

    return result


@pytest.mark.parametrize(
    'S,P,Q,result',
    [
        ('CAGCCTA', [2, 5, 0], [4, 5, 6], [2, 4, 1]),
    ]
)
def test_solution(S, P, Q, result):
    assert solution_onm(S, P, Q) == result
    assert solution(S, P, Q) == result
