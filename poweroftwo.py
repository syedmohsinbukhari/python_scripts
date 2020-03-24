import sys


def raiseit(n):
    if n == 0:
        return str(1)
    val = raiseit(n-1)
    ser = f"{val}, {2**n}"
    return ser


def main(argv):
    n = int(argv[1])
    print(f"n={n}")
    print(raiseit(n))


main(sys.argv)

