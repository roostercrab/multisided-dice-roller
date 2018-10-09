from check_highest import CheckHighest
from check_dups import CheckDups
from check_count import CheckCount
from master_roll import Roll
import json

def Stage(roll_name,staged_dicelist,number_of_rolls):
 
    rolled_count_dictionary = {
    '1s':0,
    '2s':0,
    '3s':0,
    '4s':0,
    '5s':0,
    '6s':0,
    '7s':0,
    '8s':0,
    '9s':0,
    '10s':0,
    '11s':0,
    '12s':0,
    '13s':0,
    '14s':0,
    '15s':0,
    '16s':0,
    '17s':0,
    '18s':0,
    '19s':0,
    '20s':0}
    
    highest_results_dictionary = {  
    'd4_hits':0,
    'd6_hits':0,
    'd8_hits':0,
    'd10_hits':0,   
    'd12_hits':0,
    'd20_hits':0,  
    'double_hit':0,
    'triple_hit':0,
    'quad_hit':0,
    'quint_hit':0, 
    'hit_on_1s':0,
    'hit_on_2s':0,
    'hit_on_3s':0,
    'hit_on_4s':0,
    'hit_on_5s':0,
    'hit_on_6s':0,
    'hit_on_7s':0,
    'hit_on_8s':0,
    'hit_on_9s':0,
    'hit_on_10s':0,
    'hit_on_11s':0,
    'hit_on_12s':0,
    'hit_on_13s':0,
    'hit_on_14s':0,
    'hit_on_15s':0,
    'hit_on_16s':0,
    'hit_on_17s':0,
    'hit_on_18s':0,
    'hit_on_19s':0,
    'hit_on_20s':0}

    dups_results_dictionary = {
    'doubles':0,
    'triples':0,
    'quadruples':0,
    'quintuples':0,
    'sixtuples':0,
    'sentuples':0,
    'octuples':0,
    'doubles':0,
    'triples':0,
    'quadruples':0,
    'quintuples':0,
    'sixtuples':0,
    'sentuples':0,
    'octuples':0,
    'double_1s':0,
    'double_2s':0,
    'double_3s':0,
    'double_4s':0,
    'double_5s':0,
    'double_6s':0,
    'double_7s':0,
    'double_8s':0,
    'double_9s':0,
    'double_10s':0,
    'double_11s':0,
    'double_12s':0,
    'double_13s':0,
    'double_14s':0,
    'double_15s':0,
    'double_16s':0,
    'double_17s':0,
    'double_18s':0,
    'double_19s':0,
    'double_20s':0,
    'triple_1s':0,
    'triple_2s':0,
    'triple_3s':0,
    'triple_4s':0,
    'triple_5s':0,
    'triple_6s':0,
    'triple_7s':0,
    'triple_8s':0,
    'triple_9s':0,
    'triple_10s':0,
    'triple_11s':0,
    'triple_12s':0,
    'triple_13s':0,
    'triple_14s':0,
    'triple_15s':0,
    'triple_16s':0,
    'triple_17s':0,
    'triple_18s':0,
    'triple_19s':0,
    'triple_20s':0,
    'quadruple_1s':0,
    'quadruple_2s':0,
    'quadruple_3s':0,
    'quadruple_4s':0,
    'quadruple_5s':0,
    'quadruple_6s':0,
    'quadruple_7s':0,
    'quadruple_8s':0,
    'quadruple_9s':0,
    'quadruple_10s':0,
    'quadruple_11s':0,
    'quadruple_12s':0,
    'quadruple_13s':0,
    'quadruple_14s':0,
    'quadruple_15s':0,
    'quadruple_16s':0,
    'quadruple_17s':0,
    'quadruple_18s':0,
    'quadruple_19s':0,
    'quadruple_20s':0,
    'quintuple_1s':0,
    'quintuple_2s':0,
    'quintuple_3s':0,
    'quintuple_4s':0,
    'quintuple_5s':0,
    'quintuple_6s':0,
    'quintuple_7s':0,
    'quintuple_8s':0,
    'quintuple_9s':0,
    'quintuple_10s':0,
    'quintuple_11s':0,
    'quintuple_12s':0,
    'quintuple_13s':0,
    'quintuple_14s':0,
    'quintuple_15s':0,
    'quintuple_16s':0,
    'quintuple_17s':0,
    'quintuple_18s':0,
    'quintuple_19s':0,
    'quintuple_20s':0,
    'sixtuple_1s':0,
    'sixtuple_2s':0,
    'sixtuple_3s':0,
    'sixtuple_4s':0,
    'sixtuple_5s':0,
    'sixtuple_6s':0,
    'sixtuple_7s':0,
    'sixtuple_8s':0,
    'sixtuple_9s':0,
    'sixtuple_10s':0,
    'sixtuple_11s':0,
    'sixtuple_12s':0,
    'sixtuple_13s':0,
    'sixtuple_14s':0,
    'sixtuple_15s':0,
    'sixtuple_16s':0,
    'sixtuple_17s':0,
    'sixtuple_18s':0,
    'sixtuple_19s':0,
    'sixtuple_20s':0,
    'sentuple_1s':0,
    'sentuple_2s':0,
    'sentuple_3s':0,
    'sentuple_4s':0,
    'sentuple_5s':0,
    'sentuple_6s':0,
    'sentuple_7s':0,
    'sentuple_8s':0,
    'sentuple_9s':0,
    'sentuple_10s':0,
    'sentuple_11s':0,
    'sentuple_12s':0,
    'sentuple_13s':0,
    'sentuple_14s':0,
    'sentuple_15s':0,
    'sentuple_16s':0,
    'sentuple_17s':0,
    'sentuple_18s':0,
    'sentuple_19s':0,
    'sentuple_20s':0,
    'octuple_1s':0,
    'octuple_2s':0,
    'octuple_3s':0,
    'octuple_4s':0,
    'octuple_5s':0,
    'octuple_6s':0,
    'octuple_7s':0,
    'octuple_8s':0,
    'octuple_9s':0,
    'octuple_10s':0,
    'octuple_11s':0,
    'octuple_12s':0,
    'octuple_13s':0,
    'octuple_14s':0,
    'octuple_15s':0,
    'octuple_16s':0,
    'octuple_17s':0,
    'octuple_18s':0,
    'octuple_19s':0,
    'octuple_20s':0}

    for roll in range(number_of_rolls):
        d4s = []
        d6s = []
        d8s = []
        d10s = []
        d12s = []
        d20s = []
        
        d4s = Roll(staged_dicelist[0])
        d6s = Roll(staged_dicelist[1])       
        d8s = Roll(staged_dicelist[2])
        d10s = Roll(staged_dicelist[3])
        d12s = Roll(staged_dicelist[4])
        d20s = Roll(staged_dicelist[5])
        highest_results_list = CheckHighest(d4s,d6s,d8s,d10s,d12s,d20s)
        all_dice_rolls = d4s + d6s + d8s + d10s + d12s + d20s 
        multiples_return_list = CheckDups(all_dice_rolls)
        count_return_list = CheckCount(all_dice_rolls)

        # zip rolled numbers count list into rolled count dictionary
        list_counter = 0  
        for k, v in rolled_count_dictionary.items():
            if count_return_list[list_counter] != 0:
                increase = count_return_list[list_counter]
                rolled_count_dictionary[k] += increase
            list_counter += 1

        # zip highest list into highest dictionary
        list_counter = 0  
        for k, v in highest_results_dictionary.items():
            if highest_results_list[list_counter] != 0:
                highest_results_dictionary[k] += highest_results_list[list_counter]
            list_counter += 1

        # zip dups list into dups dictionary
        list_counter = 0  
        for k, v in dups_results_dictionary.items():
            if multiples_return_list[list_counter] != 0:
                dups_results_dictionary[k] += multiples_return_list[list_counter]
            list_counter += 1

    final_output = {}
    final_output.update(rolled_count_dictionary) 
    final_output.update(highest_results_dictionary)
    final_output.update(dups_results_dictionary)
    
    with open("results.txt", "a+") as file:
        file.write(roll_name + (json.dumps(final_output)) + '\n')
    
    return()

