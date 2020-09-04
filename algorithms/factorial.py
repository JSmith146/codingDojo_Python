# Factorial
# Write a function factorial(num) that, given a
# number, returns the product (multiplication) of all
# positive integers from 1 up to number (inclusive).
# For example, factorial(3) = 6 (or 1 * 2 * 3);
# factorial(5) = 120 (or 1 * 2 * 3 * 4 * 5).

def factorial(n):
    if n==0:
        print(0)
    res = 1
    for i in range(1,n+1):
        res *= i
    print(res)

factorial(3)
factorial(5)
