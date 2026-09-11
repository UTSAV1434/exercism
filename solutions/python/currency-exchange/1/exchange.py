def exchange_money(budget, exchange_rate):
    return budget / exchange_rate
def get_change(budget,exchanging_value):
    return budget - exchanging_value
def get_value_of_bills(denomination, number_of_bills):
    total_amount = denomination * number_of_bills
    full_bills = total_amount // denomination
    payout = full_bills * denomination
    return payout
def get_number_of_bills(amount, denomination):
    return int(amount // denomination)
def get_leftover_of_bills(amount, denomination):
    return amount % denomination
def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_decimal = spread / 100
    adjusted_rate = exchange_rate * (1 + spread_decimal)
    exchanged_amount = budget / adjusted_rate
    max_value = (exchanged_amount // denomination) * denomination
    return int(max_value)
