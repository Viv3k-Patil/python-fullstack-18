

try:
    # a = 1 / 0
    a = int("abc")
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")