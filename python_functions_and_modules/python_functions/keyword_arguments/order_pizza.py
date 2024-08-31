
# Write a function `order_pizza` that takes `size`, `topping1`, and `topping2` as keyword arguments. 
# Set default values for `size`, `topping1` and `topping2`.

def order_pizza(size="medium", topping1="pineapple", topping2="bacon"):
    return f"Order: {size} pizza with {topping1} and {topping2}."

print(order_pizza())  # Output: Order: medium pizza with pineapple and bacon.
print(order_pizza(size="large", topping1="pepperoni"))  # Output: Order: large pizza with pepperoni and bacon.