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
t <coin_price> [<investment_amount>] [<current_coin_price>]
```

Parameters:
- <coin_price>: The price of the cryptocurrency at the time of purchase (in USD). (Required)
- [<investment_amount>]: The total amount of money invested (in USD). (Optional, defaults to $100).
- [<current_coin_price>]: The current price of the cryptocurrency (in USD). (Optional, defaults to None).

## Sample output
```bash
# t 116 200 118

Price: $116.000000
Paid:  $200.000000
Break: $116.581454
1.22%: $118.000000 ($2.44)
1.00%: $117.747268 ($2.00)
2.00%: $118.913083 ($4.01)
3.00%: $120.078897 ($6.01)
4.00%: $121.244712 ($8.02)
5.00%: $122.410526 ($10.03)
```