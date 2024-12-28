def trade_summary_with_fractional(
    coin_price, investment_amount, current_coin_price=None, fee_percent=0.20
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
    # print("=== Trading Information ===")
    print(f"Price:  ${coin_price:.6f}")
    print(f"Paid:   ${investment_amount:.6f}")
    # print(f"Fee Percentage (Per Trade): {fee_percent}%")
    # print(f"Qty:    {quantity:.6f}")
    # print(f"Fee:    ${buy_fee:.6f}")
    # print(f"Total:  ${actual_total_cost:.6f}")
    # print(f"Actual: ${actual_price_per_unit:.6f}")
    print(f"Break:  ${break_even_price:.6f}\n")

    if current_coin_price:
        print(
            f"{percentage_profit_loss:.2f}%: ${current_coin_price:.6f} (${profit_at_current:.6f})"
        )
        # print(f"Sell Value:         ${total_sell_value_at_current:.6f}")
        # print(f"Net Profit/Loss:    ${profit_at_current:.6f}")
        # print(f"Percentage:         {percentage_profit_loss:.2f}%")

    for gain, price in target_prices.items():
        # print(f"\nFor {gain}% Gain")
        print(f"{gain}%: ${price:.6f} (${profits[gain]:.6f})")
        # print(f"Sell Value:   ${net_sell_values[gain]:.6f}")
        # print(f"Net Profit:   ${profits[gain]:.6f}")


def trade_summary(buy_price, quantity):
    investment_amount = buy_price * quantity
    trade_summary_with_fractional(buy_price, investment_amount)


def main():
    # Ask for input
    user_input = input("Enter input (price,paid,current): ")

    # Split the input and parse the numbers
    inputs = user_input.split(",")
    if len(inputs) < 1 or len(inputs) > 3:
        print("Error: Please enter 1 to 3 comma-separated numbers.")
        exit(1)  # Exit the program with an error status

    # Parse arguments
    try:
        coin_price = float(inputs[0])
        investment_amount = float(inputs[1]) if len(inputs) > 1 else 100
        current_coin_price = float(inputs[2]) if len(inputs) > 2 else None
    except ValueError:
        print("Error: All inputs must be valid numbers.")
        exit(1)

    trade_summary_with_fractional(
        coin_price=coin_price,
        investment_amount=investment_amount,
        current_coin_price=current_coin_price,
    )


if __name__ == "__main__":
    main()
