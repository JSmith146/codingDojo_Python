# Threes and Fives
# Create function ThreesFives() that adds each value 
# from 100 and 4000000 (inclusive) if that value
# is evenly divisible by 3 or 5 but not both . Display 
# the final sum in the console.

def ThreesFives():
    sum = 0 
    for i in range(100,4000001):
        if (i%3==0) and (i%5==0):
            continue
        elif (i%3==0) or (i%5==0):
            sum += i
    print(sum)

ThreesFives()

def BetterThreesFives(start,end):
    sum = 0
    for i in range(start, end+1):
        if (i%3==0) and (i%5==0):
            continue
        elif (i%3==0) or (i%5==0):
            sum += i
    print(sum)
BetterThreesFives(1,100)
