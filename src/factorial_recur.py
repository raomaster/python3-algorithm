def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recur(n-1)


z = 0
print(f"Factorial for value {z}! is: {factorial_recur(z)}")

z = 1
print(f"Factorial for value {z}! is: {factorial_recur(z)}")

z = 5
print(f"Factorial for value {z}! is: {factorial_recur(z)}")