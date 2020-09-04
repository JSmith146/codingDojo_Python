# Generate Coin Change
# Implement generateCoinChange(cents) that accepts a parameter 
# for the number of cents, and
# computes how to represent that amount with the smallest 
# number of coins. Console.log the result.

def generateCoinChange(cents):
    quarters, dimes, nickles, pennies  = 0,0,0,0
    while cents >0:
        if (cents - .25) > 0:
            quarters += 1
            cents -= .25
            print("remaining change:",cents)
            continue
        # elif cents%.10==0:
        #     dimes += 1
        #     cents -= .10
        #     print("remaining change:",cents)
        #     continue
    print(quarters,dimes,nickles,pennies)

generateCoinChange(.50)