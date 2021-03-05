import sys


def calculate_growth(capital, growth, years):
    return capital * (growth ** years)


def calculate_growth_on_consist_invest(capital, investment, growth, years):
    accumulated_capital = calculate_growth(capital, growth, years)
    original_capital = capital
    for i in range(years - 1, 0, -1):
        grown_investment = calculate_growth(investment, growth, i)
        accumulated_capital += grown_investment
        original_capital += investment
        print(f"{investment} grew to {grown_investment} in {i} time units")

    return accumulated_capital, original_capital


def main():
    capital = float(sys.argv[1])
    investment = float(sys.argv[2])
    growth = float(sys.argv[3])
    years = int(sys.argv[4])
    accumulated_capital, original_capital = calculate_growth_on_consist_invest(
        capital, investment, growth, years
    )

    capital_growth = accumulated_capital / original_capital

    print(f"original_capital: {original_capital}")
    print(f"accumulated_capital: {accumulated_capital}")
    print(f"capital_growth: {capital_growth}")


if __name__ == '__main__':
    main()
