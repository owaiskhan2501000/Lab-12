def check_range(value, min_value, max_value):
    assert min_value <= value <= max_value, f"Value {value} is not within the specified range [{min_value}, {max_value}]"
try:
    check_range(5, 1, 10)
    print("Value is within the specified range.")
except AssertionError as e:
    print(f"AssertionError: {e}")
