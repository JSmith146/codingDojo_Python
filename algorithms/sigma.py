# Sigma
# Implement a function sigma(num) that, given a
# number, returns the sum of all positive integers
# from 1 up to number (inclusive). Ex.: sigma(3)
# = 6 (or 1+2+3); sigma(5) = 15 (or 1+2+3+4+5).

def sigma(n):
    sum = 0
    for i in range(n+1):
        sum += i
    print(sum)

sigma(3)
sigma(5)

