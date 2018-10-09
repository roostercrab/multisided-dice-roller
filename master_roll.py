import random

def Roll(dice):
    qty = dice.qty
    sides = dice.sides
    roll_list = []
        
    #rolls a single type of dice "qty" times and appends the result to roll_list
    for q in range(qty):
        
        #print('Rolling %s' % dice.name)
        rand = random.randint(1, sides)
        roll_list.append(rand)
        #print('this is the roll list: %s' % roll_list)
       
    return roll_list
