def Count(d4_count, d6_count, d8_count, d10_count, d12_count, d20_count): 

    #creating every possible combination of dice by counting upwards by 6s, stored in sliced_dicelist, then used to CallRoll on each item
    #test_i = 0
    complete = 0
    while complete != 1:
    #while test_i < 100:   
        #print("Count: d4s: %s  d6s: %s  d8s: %s d10s: %s  d12s: %s d20s: %s" % (d4_count, d6_count, d8_count, d10_count, d12_count, d20_count))
        if d4_count < 6:
            d4_count += 1
        else:
            d4_count = 0
            if d6_count < 6:
                d6_count += 1
            else:
                d6_count = 0
                if d8_count < 6:
                    d8_count += 1
                else:
                    d8_count = 0
                    if d10_count < 6:
                        d10_count += 1
                    else:
                        d10_count = 0
                        if d12_count < 6:
                            d12_count += 1
                        else:
                            d12_count = 0
                            if d20_count < 6:
                                d20_count += 1
                            else:
                                complete = 1
                                print("complete")
                                
        countlist = [d4_count, d6_count, d8_count, d10_count, d12_count, d20_count]
        #print(countlist)
        
    #test_i += 1
        
        return(countlist)
        
        
        

def Slice(d4_count, d6_count, d8_count, d10_count, d12_count, d20_count):       
    
    
    #these will use the incrementing numbers from the countlist and increase each by the position that they should be in to pull from the correct position in the dicelist
    d4_slice = d4_count
    d6_slice = d6_count
    d8_slice = d8_count
    d10_slice = d10_count
    d12_slice = d12_count
    d20_slice = d20_count
    
    if d4_slice !=0:
        d4_slice 
    
    if d6_slice !=0:
        d6_slice += 6

    if d8_slice !=0:
        d8_slice += 12

    if d10_slice !=0:
        d10_slice += 18

    if d12_slice !=0:
        d12_slice += 24

    if d20_slice !=0:
        d20_slice += 30

    slicelist = [d4_slice, d6_slice, d8_slice, d10_slice, d12_slice, d20_slice]
    #print("Slice: d4s: %s  d6s: %s  d8s: %s d10s: %s  d12s: %s d20s: %s" % (d4_slice, d6_slice, d8_slice, d10_slice, d12_slice, d20_slice))
        
    return(slicelist)
