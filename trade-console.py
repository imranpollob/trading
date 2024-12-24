import sys
from trade import trade_summary_with_fractional

def main():
    # Check the number of arguments
    if len(sys.argv) < 2:
        print(
            "Usage: python trade_summary.py <coin_price> <investment_amount> [current_coin_price]"
        )
        sys.exit(1)

    # Parse arguments
    coin_price = float(sys.argv[1])
    investment_amount = float(sys.argv[2]) if len(sys.argv) > 2 else 100
    current_coin_price = float(sys.argv[3]) if len(sys.argv) > 3 else None

    # Call the function
    trade_summary_with_fractional(
        coin_price=coin_price,
        investment_amount=investment_amount,
        current_coin_price=current_coin_price,
    )


if __name__ == "__main__":
    main()