# Crypto Trading Profit Calculator

A command-line tool to calculate the profitable selling price of a cryptocurrency based on the investment amount, coin price, and the current price.

For crypto exchange like `kraken` impose 0.25% fee for any limit buy and sell. This tool can be helpful to analyze the selling price. 

You can change the `fee_percent=0.25` to adapt it for other exchanges fee rate.

## Usage
```bash
git clone https://github.com/your-repo/trade.git
cd trade
pip install -e .
```

## Available commands
```bash
t <coin_price> [<investment_amount>] [<current_coin_price>] [<buy_fee_rate>] [<sell_fee_rate>]
```

Parameters:
- <coin_price>: The price of the cryptocurrency at the time of purchase (in USD). (Required)
- [<investment_amount>]: The total amount of money invested (in USD). (Optional, defaults to $100).
- [<current_coin_price>]: The current price of the cryptocurrency (in USD). (Optional, defaults to None).
- [<buy_fee_rate>]: The current fee to buy. (Optional, defaults to 0.25).
- [<sell_fee_rate>]: The current fee to sell. (Optional, defaults to 0.25).

**Note:** If one fee is given it will be used for both buy and sell.

#### Storing custom fees
If you want to store a new fee structure for the default buy and sell fee then you can use the following command.

```bash
t --set-fee

# it will ask for input
Enter the buy fee rate (%): <buy_fee_rate>
Enter the sell fee rate (%): <sell_fee_rate>
```

## Sample output
```bash
# t 116
# t coin_price
Price: $116.000000
Paid:  $100.000000
Fee:   Buy 0.25% Sell 0.25%
Break: $116.581454

1.00%: $117.747268 ($1.00)
2.00%: $118.913083 ($2.01)
3.00%: $120.078897 ($3.01)
4.00%: $121.244712 ($4.01)
5.00%: $122.410526 ($5.01)

# t 116 200
# t coin_price investment_amount
Price: $116.000000
Paid:  $200.000000
Fee:   Buy 0.25% Sell 0.25%
Break: $116.581454

1.00%: $117.747268 ($2.00)
2.00%: $118.913083 ($4.01)
3.00%: $120.078897 ($6.01)
4.00%: $121.244712 ($8.02)
5.00%: $122.410526 ($10.03)

# t 116 200 118
# t coin_price investment_amount current_coin_price
Price: $116.000000
Paid:  $200.000000
Fee:   Buy 0.25% Sell 0.25%
Break: $116.581454

1.22%: $118.000000 ($2.44)
1.00%: $117.747268 ($2.00)
2.00%: $118.913083 ($4.01)
3.00%: $120.078897 ($6.01)
4.00%: $121.244712 ($8.02)
5.00%: $122.410526 ($10.03)

# t 116 200 118 .20
# t coin_price investment_amount current_coin_price buy_fee_rate
Price: $116.000000
Paid:  $200.000000
Fee:   Buy 0.20% Sell 0.20%
Break: $116.464930

1.32%: $118.000000 ($2.64)
1.00%: $117.629579 ($2.00)
2.00%: $118.794228 ($4.01)
3.00%: $119.958878 ($6.01)
4.00%: $121.123527 ($8.02)
5.00%: $122.288176 ($10.02)

# 116 200 118 .20 .35
# t coin_price investment_amount current_coin_price buy_fee_rate sell_fee_rate
Price: $116.000000
Paid:  $200.000000
Fee:   Buy 0.20% Sell 0.35%
Break: $116.640241

1.17%: $118.000000 ($2.34)
1.00%: $117.806643 ($2.00)
2.00%: $118.973046 ($4.01)
3.00%: $120.139448 ($6.01)
4.00%: $121.305850 ($8.02)
5.00%: $122.472253 ($10.02)
```