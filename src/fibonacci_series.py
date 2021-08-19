def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)


z = 0
print(f"The {z}! number in the fibonacci sequence is: {fib_recur(z)}")

z = 1
print(f"The {z}! number in the fibonacci sequence is: {fib_recur(z)}")

z = 10
print(f"The {z}! number in the fibonacci sequence is: {fib_recur(z)}")