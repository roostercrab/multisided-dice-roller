def CheckHighest(d4s, d6s, d8s, d10s, d12s, d20s):

    # this will be the highest dice of the roll
    max_highest = 0
    
    # we want to know which dice had the highest roll (the 'hit')
    d4_hits = 0
    d6_hits = 0
    d8_hits = 0
    d10_hits = 0   
    d12_hits = 0
    d20_hits = 0

    # records if the rolled hit number was hit by more than one dice    
    double_hit = 0
    triple_hit = 0
    quad_hit = 0
    quint_hit = 0 
    
    # print(d4s, d6s, d8s, d10s, d12s, d20s)
    # prepares the highest rolls from each rolled list to compare against each other
    d4s_highest = max(d4s, default=0)
    d6s_highest = max(d6s, default=0)
    d8s_highest = max(d8s, default=0)
    d10s_highest = max(d10s, default=0)
    d12s_highest = max(d12s, default=0)
    d20s_highest = max(d20s, default=0)
    
    # highest_rolls is a list of all the highest rolls combined
    highest_rolls = [d4s_highest, d6s_highest, d8s_highest, d10s_highest, d12s_highest, d20s_highest]

    # max_highest is the highest dice number
    max_highest = max(highest_rolls)

    # record what number the highest roll was 
    which_number_hit = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    list_counter = 0
    for number in range(1,21):
        if max_highest == number:
            which_number_hit[list_counter] += 1
            break
        else:
            list_counter +=1    
    
    # compare the rolls and record which multisided dice had the highest roll ('hit')       
    if d20s_highest == max_highest:
        d20_hits += 1
    else:
        if d12s_highest == max_highest:
            d12_hits += 1
        else:
            if d10s_highest == max_highest:
                d10_hits += 1
            else:
                if d8s_highest == max_highest:
                    d8_hits += 1                    
                else:
                    if d6s_highest == max_highest:
                        d6_hits += 1
                    else:
                        if d4s_highest == max_highest:
                            d4_hits += 1

    # checks to see if the rolled hit number was hit by more than one dice, doesn't record which other dice hit though    
    if highest_rolls.count(max_highest) == 5:
        quint_hit += 1  
    if highest_rolls.count(max_highest) == 4:
        quad_hit += 1
    if highest_rolls.count(max_highest) == 3:
        triple_hit += 1
    if highest_rolls.count(max_highest) == 2:
        double_hit += 1

    # put all the results into a list to be put into the dictionary
    highest_results_list = [
    d4_hits,
    d6_hits,
    d8_hits,
    d10_hits,   
    d12_hits,
    d20_hits, 
    double_hit,
    triple_hit,
    quad_hit,
    quint_hit] + which_number_hit  

    #print(highest_results_list)
    return(highest_results_list)