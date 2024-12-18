import sys


def trade_summary_with_fractional(
    coin_price, investment_amount, current_coin_price=None, fee_percent=0.25
):
    # Input validation
    if coin_price <= 0 or investment_amount <= 0 or fee_percent < 0:
        raise ValueError(
            "Invalid input: coin_price, investment_amount must be > 0 and fee_percent >= 0"
        )

    # Step 1: Calculate the fractional quantity bought
    quantity = investment_amount / coin_price
    buy_fee = investment_amount * (fee_percent / 100)  # Fee for buying
    actual_total_cost = investment_amount + buy_fee
    actual_price_per_unit = actual_total_cost / quantity

    # Step 2: Break-even Selling Price
    break_even_price = actual_price_per_unit / (1 - (fee_percent / 100))

    # Step 3: Calculate Target Prices for Gains
    target_prices = {}
    profits = {}
    net_sell_values = {}
    for gain in range(1, 6):  # Gains from 1% to 5%
        target_price = break_even_price * (1 + gain / 100)
        sell_fee_at_target = target_price * quantity * (fee_percent / 100)
        total_sell_value_at_target = target_price * quantity - sell_fee_at_target
        profit_at_target = total_sell_value_at_target - actual_total_cost
        target_prices[gain] = target_price
        profits[gain] = profit_at_target
        net_sell_values[gain] = total_sell_value_at_target

    # Step 4: Profit/Loss at Current Coin Price (if provided)
    if current_coin_price:
        sell_fee_at_current = (
            current_coin_price * quantity * (fee_percent / 100)
        )  # Sell fee at current price
        total_sell_value_at_current = (
            current_coin_price * quantity - sell_fee_at_current
        )  # Net sell value
        profit_at_current = (
            total_sell_value_at_current - actual_total_cost
        )  # Profit or loss at current price
        percentage_profit_loss = (
            profit_at_current / actual_total_cost
        ) * 100  # Percentage profit/loss
    else:
        profit_at_current = None
        percentage_profit_loss = None
        total_sell_value_at_current = None

    # Display results
    print("=== Trading Information ===")
    print(f"Coin Price per Unit:   ${coin_price:.2f}")
    print(f"Investment Amount:     ${investment_amount:.2f}")
    # print(f"Fee Percentage (Per Trade): {fee_percent}%")
    print(f"Quantity Purchased:    {quantity:.6f}")
    print(f"Buying Fee:            ${buy_fee:.6f}")
    print(f"Total Cost with Fee:   ${actual_total_cost:.6f}")
    print(f"Actual Price per Unit: ${actual_price_per_unit:.6f}")
    print(f"Break-even Sell Price: ${break_even_price:.6f}")

    if current_coin_price:
        print("\n=== Current Price Analysis ===")
        print(f"Current Coin Price: ${current_coin_price:.2f}")
        print(f"Sell Value:         ${total_sell_value_at_current:.6f}")
        print(f"Net Profit/Loss:    ${profit_at_current:.6f}")
        print(f"Percentage:         {percentage_profit_loss:.2f}%")

    print("\n=== Target Prices and Profits ===")
    for gain, price in target_prices.items():
        print(f"For {gain}% Gain")
        print(f"Target Price: ${price:.6f}")
        print(f"Sell Value:   ${net_sell_values[gain]:.6f}")
        print(f"Net Profit:   ${profits[gain]:.6f}")
        print()


def trade_summary(buy_price, quantity):
    investment_amount = buy_price * quantity
    trade_summary_with_fractional(buy_price, investment_amount)


def main():
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: python trade_summary.py <coin_price> <investment_amount> [current_coin_price]")
        sys.exit(1)

    # Parse arguments
    coin_price = float(sys.argv[1])
    investment_amount = float(sys.argv[2])
    current_coin_price = float(sys.argv[3]) if len(sys.argv) > 3 else None

    # Call the function
    trade_summary_with_fractional(
        coin_price=coin_price,
        investment_amount=investment_amount,
        current_coin_price=current_coin_price
    )

if __name__ == "__main__":
    main()

