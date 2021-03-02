import sys


def calculate_growth(capital, growth, years):
    return capital * (growth ** years)


def calculate_growth_on_consist_invest(capital, investment, growth, years):
    accumulated_capital = calculate_growth(capital, growth, years)
    for i in range(1, years):
        accumulated_capital += calculate_growth(investment, growth, i)

    return accumulated_capital


def main():
    capital = float(sys.argv[1])
    investment = float(sys.argv[2])
    growth = float(sys.argv[3])
    years = int(sys.argv[4])
    accumulated_capital = calculate_growth_on_consist_invest(
        capital, investment, growth, years
    )

    capital_growth = accumulated_capital / capital

    print(f"accumulated_capital: {accumulated_capital}")
    print(f"capital_growth: {capital_growth}")


if __name__ == '__main__':
    main()
