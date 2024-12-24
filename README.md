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
# for basic information
trade <coin_price> [<investment_amount>] [<current_coin_price>]

# for detailed information
traded <coin_price> [<investment_amount>] [<current_coin_price>]
```

Parameters:
- <coin_price>: The price of the cryptocurrency at the time of purchase (in USD). (Required)
- [<investment_amount>]: The total amount of money invested (in USD). (Optional, defaults to $100).
- [<current_coin_price>]: The current price of the cryptocurrency (in USD). (Optional, defaults to None).

## Sample basic output
```bash
# trade 116 200 118

Price:  $116.000000
Paid:   $200.000000
Break:  $116.581454

1.22%: $118.000000 ($2.439655)
1%: $117.747268 ($2.005000)
2%: $118.913083 ($4.010000)
3%: $120.078897 ($6.015000)
4%: $121.244712 ($8.020000)
5%: $122.410526 ($10.025000)
```


## Sample detailed output
```bash
# traded 116 200 118

=== Trading Information ===
Coin Price per Unit:   $116.000000
Investment Amount:     $200.000000
Quantity Purchased:    1.724138
Buying Fee:            $0.500000
Total Cost with Fee:   $200.500000
Actual Price per Unit: $116.290000
Break-even Sell Price: $116.581454

=== Current Price Analysis ===
Current Coin Price: $118.000000
Sell Value:         $202.939655
Net Profit/Loss:    $2.439655
Percentage:         1.22%

=== Target Prices and Profits ===
For 1% Gain
Target Price: $117.747268
Sell Value:   $202.505000
Net Profit:   $2.005000

For 2% Gain
Target Price: $118.913083
Sell Value:   $204.510000
Net Profit:   $4.010000

For 3% Gain
Target Price: $120.078897
Sell Value:   $206.515000
Net Profit:   $6.015000

For 4% Gain
Target Price: $121.244712
Sell Value:   $208.520000
Net Profit:   $8.020000

For 5% Gain
Target Price: $122.410526
Sell Value:   $210.525000
Net Profit:   $10.025000
```