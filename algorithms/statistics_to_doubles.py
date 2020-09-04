import random
# Statistics to Doubles
# Implement a ‘die’ that randomly returns an
# integer between 1 and 6 inclusive. Roll a pair of
# these dice, tracking the statistics until doubles
# are rolled. Display the number of rolls , min , max ,
# and average .

def dice_roll():
    return random.randint(1,6)

# double = False
dice_stats = {'max':0, 'min':12, 'count':0, 'roll_total':0,'average':0}
while True:
    dice1, dice2 = dice_roll(), dice_roll()
    if dice1==dice2:
        print("Both dice rolled:",dice1)
        print("Finished")
        print(dice_stat)
        break
    sum = dice1 + dice2
    if sum > dice_stats['max']:
        dice_stats['max'] = sum
    if sum < dice_stats['min']:
        dice_stats['min'] = sum
    dice_stats['count'] += 1
    dice_stats['roll_total'] += sum
    dice_stats['average'] = dice_stats['roll_total']/dice_stats[]
    print(dice_stats)
