def fractional_knapsack(sack  , weight):
    profit = 0
    sack.sort(key = lambda item: item[0]/item[1] , reverse = True)
    for p , w in sack:
        if w <= weight:
            profit += p
            weight -= w
        else :
            profit += (p/w) * weight
            break
    return profit

sack = [(100 , 20) , (60 , 10) , (100 , 50) , (200 , 50)]
weight = 90
print(fractional_knapsack(sack,weight))

            
        
        
        



