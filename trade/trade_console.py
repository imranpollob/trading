import sys
from trade.trade import trade_summary


def main():
    # Check the number of arguments
    if len(sys.argv) < 2:
        print(
            "Usage: python trade_summary.py <coin_price> <investment_amount> [current_coin_price]"
        )
        sys.exit(1)

    buy_fee_rate = 0.25
    sell_fee_rate = 0.25

    # Parse arguments
    try:
        coin_price = float(sys.argv[1])
        investment_amount = float(sys.argv[2]) if len(sys.argv) > 2 else 100
        current_coin_price = float(sys.argv[3]) if len(sys.argv) > 3 else None
        if len(sys.argv) > 5:
            buy_fee_rate = float(sys.argv[4])
            sell_fee_rate = float(sys.argv[5])
        elif len(sys.argv) > 4:
            buy_fee_rate = float(sys.argv[4])
            sell_fee_rate = float(sys.argv[4])

    except ValueError:
        print("Error: All inputs must be valid numbers.")
        sys.exit(1)

    # Call the function
    trade_summary(
        coin_price=coin_price,
        investment_amount=investment_amount,
        current_coin_price=current_coin_price,
        buy_fee_rate=buy_fee_rate / 100,
        sell_fee_rate=sell_fee_rate / 100,
    )


if __name__ == "__main__":
    main()
