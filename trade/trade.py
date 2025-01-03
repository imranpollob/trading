def trade_summary(
    coin_price,
    investment_amount=100,
    current_coin_price=None,
    buy_fee_rate=0.0025,
    sell_fee_rate=0.0025,
):
    default_format = "{:.4f}"
    # if lenght of the coin_price after precision is more than 4, use the length of the input's precision
    input_format = len(str(coin_price).split(".")[1])

    if input_format > 4:
        default_format = f"{{:.{input_format}f}}"

    # Calculate the number of coins bought
    num_coins = investment_amount / coin_price

    # Total cost including buy fee
    total_cost = investment_amount + (investment_amount * buy_fee_rate)

    # Break-even price
    break_even_price = (total_cost / num_coins) / (1 - sell_fee_rate)

    # Output initial details
    print(f"Price: ${default_format.format(coin_price)}")
    print(f"Paid:  ${default_format.format(investment_amount)}")
    print(f"Fee:   Buy {buy_fee_rate*100:.2f}% Sell {sell_fee_rate*100:.2f}%")
    print(f"Break: ${default_format.format(break_even_price)}\n")

    # If current coin price is provided, calculate profit/loss
    if current_coin_price is not None:
        sell_revenue = num_coins * current_coin_price * (1 - sell_fee_rate)
        net_profit_loss = sell_revenue - total_cost
        profit_loss_percentage = (net_profit_loss / total_cost) * 100
        print(
            f"{profit_loss_percentage:.2f}%: ${default_format.format(current_coin_price)} (${net_profit_loss:.2f})"
        )

    # Target prices and profit amounts for 1% to 5% profit
    for i, profit in enumerate([0.01, 0.02, 0.03, 0.04, 0.05], 1):
        price = break_even_price * (1 + profit)
        profit_amount = (price - break_even_price) * num_coins * (1 - sell_fee_rate)
        print(
            f"{profit * 100:.2f}%: ${default_format.format(price)} (${profit_amount:.2f})"
        )


def main():
    # Ask for input
    user_input = input("Enter input (price,[paid,current,buy_fee,sell_fee]): ")

    # Split the input and parse the numbers
    inputs = user_input.split(",")
    if len(inputs) < 1:
        print("Error: Please enter comma-separated numbers.")
        exit(1)  # Exit the program with an error status

    buy_fee_rate = 0.25
    sell_fee_rate = 0.25

    # Parse arguments
    try:
        coin_price = float(inputs[0])
        investment_amount = float(inputs[1]) if len(inputs) > 1 else 100
        current_coin_price = float(inputs[2]) if len(inputs) > 2 else None
        if len(inputs) > 4:
            buy_fee_rate = float(inputs[3])
            sell_fee_rate = float(inputs[4])
        elif len(inputs) > 3:
            buy_fee_rate = float(inputs[3])
            sell_fee_rate = float(inputs[3])

    except ValueError:
        print("Error: All inputs must be valid numbers.")
        exit(1)

    trade_summary(
        coin_price=coin_price,
        investment_amount=investment_amount,
        current_coin_price=current_coin_price,
        buy_fee_rate=buy_fee_rate / 100,
        sell_fee_rate=sell_fee_rate / 100,
    )


if __name__ == "__main__":
    main()
