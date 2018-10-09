def CheckCount(all_dice_rolls):

    rolled_numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    number_to_check = 1
    list_position = 0
    for check in range(1,21):
        how_many = all_dice_rolls.count(number_to_check)
        rolled_numbers[list_position] += how_many
        number_to_check += 1
        list_position += 1

    return(rolled_numbers)