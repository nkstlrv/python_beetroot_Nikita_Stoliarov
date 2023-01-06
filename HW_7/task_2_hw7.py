# Task 2

# Input data:
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }

# Compute the total price of the stock
# where the total price is the sum of the price of an item
# multiplied by the quantity of this exact item.


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock_list = []
for s_val in stock.values():
    stock_list.append(float(s_val))
print("\n Our item's quantities list is -->", stock_list)

prices_list = []
for p_val in prices.values():
    prices_list.append(float(p_val))
print("\n Our item's prices list is -->", prices_list)

set_prices_list = []
for i in range(len(stock_list)):
    set_prices_list.append(stock_list[i] * prices_list[i])
print("\n Price of each set of items  -->", set_prices_list)

total_price = sum(set_prices_list)

print("\n Our stock total price is -->", total_price)