def DupsCheck():
    all_dice_rolls = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,7,8]
    doubles = 0
    triples = 0
    quadruples = 0
    quintuples = 0
    sixtuples = 0
    sentuples = 0
    octuples = 0

    doubles_per_number = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    triples_per_number = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    quadruples_per_number = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    quintuples_per_number = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sixtuples_per_number = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    sentuples_per_number = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    octuples_per_number = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    number_to_check = 1
    list_position = 0
    for check in range(1,21):
        if number_to_check in all_dice_rolls:
            how_many = all_dice_rolls.count(number_to_check)
        
        if how_many == 2:
            doubles_per_number[list_position] += 1
            doubles += 1
        elif how_many == 3:
            triples_per_number[list_position] += 1
            triples += 1
        elif how_many == 4:
            quadruples_per_number[list_position] += 1
            quadruples += 1
        elif how_many == 5:
            quintuples_per_number[list_position] += 1
            quintuples += 1
        elif how_many == 6:
            sixtuples_per_number[list_position] += 1
            sixtuples += 1
        elif how_many == 7:
            sentuples_per_number[list_position] += 1
            sentuples += 1
        elif how_many == 8:
            octuples_per_number[list_position] += 1
            octuples += 1

        number_to_check += 1
        list_position += 1


