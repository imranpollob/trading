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
Price: $116.0000
Paid:  $100.0000
Fee:   Buy 0.25% Sell 0.25%
Break: $116.5815

0.50%: $117.1644 ($0.50)
1.00%: $117.7473 ($1.00)
2.00%: $118.9131 ($2.01)
3.00%: $120.0789 ($3.01)
4.00%: $121.2447 ($4.01)
5.00%: $122.4105 ($5.01)

-0.50%: $115.9985 (-$0.50)
-1.00%: $115.4156 (-$1.00)
-2.00%: $114.2498 (-$2.01)
-3.00%: $113.0840 (-$3.01)
-4.00%: $111.9182 (-$4.01)
-5.00%: $110.7524 (-$5.01)

# t 116 200
# t coin_price investment_amount
Price: $116.0000
Paid:  $200.0000
Fee:   Buy 0.25% Sell 0.25%
Break: $116.5815

0.50%: $117.1644 ($1.00)
1.00%: $117.7473 ($2.00)
2.00%: $118.9131 ($4.01)
3.00%: $120.0789 ($6.01)
4.00%: $121.2447 ($8.02)
5.00%: $122.4105 ($10.03)

-0.50%: $115.9985 (-$1.00)
-1.00%: $115.4156 (-$2.00)
-2.00%: $114.2498 (-$4.01)
-3.00%: $113.0840 (-$6.01)
-4.00%: $111.9182 (-$8.02)
-5.00%: $110.7524 (-$10.03)

# t 116 200 118
# t coin_price investment_amount current_coin_price
Price: $116.0000
Paid:  $200.0000
Fee:   Buy 0.25% Sell 0.25%
Break: $116.5815

1.22%: $118.0000 ($2.44)

0.50%: $117.1644 ($1.00)
1.00%: $117.7473 ($2.00)
2.00%: $118.9131 ($4.01)
3.00%: $120.0789 ($6.01)
4.00%: $121.2447 ($8.02)
5.00%: $122.4105 ($10.03)

-0.50%: $115.9985 (-$1.00)
-1.00%: $115.4156 (-$2.00)
-2.00%: $114.2498 (-$4.01)
-3.00%: $113.0840 (-$6.01)
-4.00%: $111.9182 (-$8.02)
-5.00%: $110.7524 (-$10.03)

# t 116 200 118 .20
# t coin_price investment_amount current_coin_price buy_fee_rate
Price: $116.0000
Paid:  $200.0000
Fee:   Buy 0.20% Sell 0.20%
Break: $116.4649

1.32%: $118.0000 ($2.64)

0.50%: $117.0473 ($1.00)
1.00%: $117.6296 ($2.00)
2.00%: $118.7942 ($4.01)
3.00%: $119.9589 ($6.01)
4.00%: $121.1235 ($8.02)
5.00%: $122.2882 ($10.02)

-0.50%: $115.8826 (-$1.00)
-1.00%: $115.3003 (-$2.00)
-2.00%: $114.1356 (-$4.01)
-3.00%: $112.9710 (-$6.01)
-4.00%: $111.8063 (-$8.02)
-5.00%: $110.6417 (-$10.02)

# 116 200 118 .20 .35
# t coin_price investment_amount current_coin_price buy_fee_rate sell_fee_rate
Price: $116.0000
Paid:  $200.0000
Fee:   Buy 0.20% Sell 0.35%
Break: $116.6402

1.17%: $118.0000 ($2.34)

0.50%: $117.2234 ($1.00)
1.00%: $117.8066 ($2.00)
2.00%: $118.9730 ($4.01)
3.00%: $120.1394 ($6.01)
4.00%: $121.3059 ($8.02)
5.00%: $122.4723 ($10.02)

-0.50%: $116.0570 (-$1.00)
-1.00%: $115.4738 (-$2.00)
-2.00%: $114.3074 (-$4.01)
-3.00%: $113.1410 (-$6.01)
-4.00%: $111.9746 (-$8.02)
-5.00%: $110.8082 (-$10.02)
```