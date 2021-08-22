import pytest


class Fish:
    def __init__(self, size, dir):
        self._size = size
        self._dir = dir

    def get_size(self):
        return self._size

    def get_dir(self):
        return self._dir


def solution(A, B):
    stack = []

    alive_fish = 0
    fish_1 = Fish(A[0], B[0])
    for i in range(1, len(A)):
        if not fish_1.get_dir():
            won = True
            while len(stack) > 0:
                fish_cur = stack.pop()
                if fish_1.get_size() > fish_cur.get_size():
                    continue
                else:
                    fish_1 = fish_cur
                    won = False
                    break

            if won:
                alive_fish += 1
                fish_1 = Fish(A[i], B[i])
                continue

        fish_cur = Fish(A[i], B[i])

        if not fish_cur.get_dir():
            if fish_1.get_size() < fish_cur.get_size():
                fish_1 = fish_cur
        elif fish_cur.get_dir():
            stack.append(fish_1)
            fish_1 = fish_cur

    if not fish_1.get_dir():
        while len(stack) > 0:
            fish_cur = stack.pop()
            if fish_1.get_size() > fish_cur.get_size():
                continue
            else:
                break

    alive_fish += len(stack) + 1

    return alive_fish


@pytest.mark.parametrize(
    'A,B,result',
    [
        ([4, 3, 2, 1, 5], [0, 1, 0, 0, 0], 2),
        ([1, 1, 1, 5], [1, 1, 1, 0], 1),
        ([1, 2], [0, 0], 2),
        ([1, 2], [1, 1], 2),
    ]
)
def test_solution(A, B, result):
    assert solution(A, B) == result


if __name__ == '__main__':
    _ = solution([1, 2], [1, 1])
