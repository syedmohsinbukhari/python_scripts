import sys


def main(rent, years, increment):
    print(f"{rent} is going to increase at {increment}% for {years} years")
    accumulated_rent = 0.0
    for i in range(int(years)):
        print(f"rent in year {i} is {rent}")
        accumulated_rent += rent
        prev_rent = rent
        rent = prev_rent * (1 + (increment / 100))
    print(f"accumulated rent is {accumulated_rent}")


if __name__ == '__main__':
    rent = float(sys.argv[1])
    years = float(sys.argv[2])
    increment = float(sys.argv[3])
    main(rent, years, increment)

