import sys
import json
import os
from trade.trade import trade_summary


CONFIG_FILE = "trade_config.json"


# Load the configuration file
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"buy_fee_rate": 0.0025, "sell_fee_rate": 0.0025}


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)


def set_fee_rates():
    config = load_config()
    buy_fee_rate = float(input("Enter the buy fee rate (%): ")) / 100
    sell_fee_rate = float(input("Enter the sell fee rate (%): ")) / 100
    config["buy_fee_rate"] = buy_fee_rate
    config["sell_fee_rate"] = sell_fee_rate
    save_config(config)
    print("Fee rates updated successfully.")


def main():
    # Check the number of arguments
    if len(sys.argv) < 2:
        print(
            "Usage: t <coin_price> [<investment_amount>] [<current_coin_price>] [<buy_fee_rate>] [<sell_fee_rate>]",
            "t --set-fee",
        )
        sys.exit(1)

    # Check for special commands
    if sys.argv[1] == "--set-fee":
        set_fee_rates()
        sys.exit(0)

    config = load_config()
    buy_fee_rate = config["buy_fee_rate"]
    sell_fee_rate = config["sell_fee_rate"]

    # Parse arguments
    try:
        coin_price = float(sys.argv[1])
        investment_amount = float(sys.argv[2]) if len(sys.argv) > 2 else 100
        current_coin_price = float(sys.argv[3]) if len(sys.argv) > 3 else None
        if len(sys.argv) > 5:
            buy_fee_rate = float(sys.argv[4]) / 100
            sell_fee_rate = float(sys.argv[5]) / 100
        elif len(sys.argv) > 4:
            buy_fee_rate = float(sys.argv[4]) / 100
            sell_fee_rate = float(sys.argv[4]) / 100

    except ValueError:
        print("Error: All inputs must be valid numbers.")
        sys.exit(1)

    # Call the function
    trade_summary(
        coin_price=coin_price,
        investment_amount=investment_amount,
        current_coin_price=current_coin_price,
        buy_fee_rate=buy_fee_rate,
        sell_fee_rate=sell_fee_rate,
    )


if __name__ == "__main__":
    main()
