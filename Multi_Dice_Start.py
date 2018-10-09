from stage import Stage
from count_and_slice_functions import Count
from count_and_slice_functions import Slice

class Dice():
    """these are the dice to roll"""
    def __init__(d, qty, sides):
        d.qty = qty
        d.sides = sides
        d.name = ("%sd%s" % (qty, sides))


#these are the dice objects that will be rolled
blank = Dice(0, 0)    
q1d4 = Dice(1, 4)
q2d4 = Dice(2, 4)
q3d4 = Dice(3, 4)
q4d4 = Dice(4, 4)
q5d4 = Dice(5, 4)
q6d4 = Dice(6, 4)
q1d6 = Dice(1, 6)
q2d6 = Dice(2, 6)
q3d6 = Dice(3, 6)
q4d6 = Dice(4, 6)
q5d6 = Dice(5, 6)
q6d6 = Dice(6, 6)
q1d8 = Dice(1, 8)
q2d8 = Dice(2, 8)
q3d8 = Dice(3, 8)
q4d8 = Dice(4, 8)
q5d8 = Dice(5, 8)
q6d8 = Dice(6, 8)
q1d10 = Dice(1, 10)
q2d10 = Dice(2, 10)
q3d10 = Dice(3, 10)
q4d10 = Dice(4, 10)
q5d10 = Dice(5, 10)
q6d10 = Dice(6, 10)
q1d12 = Dice(1, 12)
q2d12 = Dice(2, 12)
q3d12 = Dice(3, 12)
q4d12 = Dice(4, 12)
q5d12 = Dice(5, 12)
q6d12 = Dice(6, 12)
q1d20 = Dice(1, 20)
q2d20 = Dice(2, 20)
q3d20 = Dice(3, 20)
q4d20 = Dice(4, 20)
q5d20 = Dice(5, 20)
q6d20 = Dice(6, 20)

dicelist = [blank, q1d4, q2d4, q3d4, q4d4, q5d4, q6d4, q1d6, q2d6, q3d6, q4d6, q5d6, q6d6, q1d8, q2d8, q3d8, q4d8, q5d8, q6d8, q1d10, q2d10, q3d10, q4d10, q5d10, q6d10, q1d12, q2d12, q3d12, q4d12, q5d12, q6d12, q1d20, q2d20, q3d20, q4d20, q5d20, q6d20]
#blank was orignally in here to prevent the list from counting from 0 but now it's also to roll nothings when needed in the count

def StartRolls(number_of_rolls):
    
    #initialize the count
    d4_count = 0
    d6_count = 0
    d8_count = 0
    d10_count = 0
    d12_count = 0
    d20_count = 0
    
    
    #this is the number of variations of 6 types of dice and 7 levels of qty (including blanks) 6^7 = 279936
    dice_combo_variations = 279936
    for variations in range(dice_combo_variations):
        
        staged_dicelist = []
        nameslist = []
        
        #gives the Count function the current dice count to return an increase of one step (dice type)
        countlist_result = Count(d4_count, d6_count, d8_count, d10_count, d12_count, d20_count)
        #print('this is the list that will be given to slice: %s' % countlist_result)
        
        #this updates the count variables so that it will increase the next time through the Count function
        d4_count, d6_count, d8_count, d10_count, d12_count, d20_count = countlist_result
        #print('d4: %s, d6: %s, d8: %s, d10: %s, d12: %s, d20: %s' % (d4_count, d6_count, d8_count, d10_count, d12_count, d20_count))
        
        #this gives the Slice function the modified count and adds positionally relevant numbers so that it can take dice from the correct position in the dicelist to roll
        slicelist_result = Slice(d4_count, d6_count, d8_count, d10_count, d12_count, d20_count)
        #print('this is the list that is coming from slice: %s' % slicelist_result)

        d4_to_roll = 0
        d6_to_roll = 0
        d8_to_roll = 0
        d10_to_roll = 0
        d12_to_roll = 0
        d20_to_roll = 0
      
        #populates the d*_to_roll variables from the slicelist that will determine which Dice objects to roll from dicelist
        d4_to_roll, d6_to_roll, d8_to_roll, d10_to_roll, d12_to_roll, d20_to_roll = slicelist_result
        
        #puts actual dice objects into staged dicelist, blank could be inserted if the count is 0 but the roll function is done off positional numbers at the moment so can't just yet...
        if d4_to_roll != 0:
            staged_dicelist.append(dicelist[d4_to_roll])
        else:
            staged_dicelist.append(dicelist[0])
            
        if d6_to_roll != 0:
            staged_dicelist.append(dicelist[d6_to_roll]) 
        else:
            staged_dicelist.append(dicelist[0])
        
        if d8_to_roll != 0:
            staged_dicelist.append(dicelist[d8_to_roll])
        else:
            staged_dicelist.append(dicelist[0])
            
        if d10_to_roll != 0:
            staged_dicelist.append(dicelist[d10_to_roll]) 
        else:
            staged_dicelist.append(dicelist[0])
            
        if d12_to_roll != 0:
            staged_dicelist.append(dicelist[d12_to_roll]) 
        else:
            staged_dicelist.append(dicelist[0])
            
        if d20_to_roll != 0:
            staged_dicelist.append(dicelist[d20_to_roll]) 
        else:
            staged_dicelist.append(dicelist[0])

        #this will collect a string of the names of the dice being rolled
        for each in staged_dicelist:
            nameslist.append(each.name)
            roll_name = ' '.join(nameslist)
            
        #print('this is the staged dicelist: %s' % staged_dicelist)       
        Stage(roll_name, staged_dicelist, number_of_rolls)    
        #print(roll_name, final_result)

if __name__ == "__main__":
    number_of_rolls = int(input('How many rolls? '))
    StartRolls(number_of_rolls)    