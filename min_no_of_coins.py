def min_coins(coins , n):
    coins.sort()
    i = 0
    rem = n
    num = 0
    res = []
    if n in coins:
        return [n]
    while i < len(coins) and coins[i] < n :
        i += 1
    j = i-1
    while j >= 0 and rem != 0:
        num = coins[j]
        while num <= rem:
            res.append(coins[j])
            rem -= num
        j -= 1
    return res

coins = [1 , 2 , 5 , 10 , 20 , 50 , 100 , 200 , 500 , 2000]
n = 6
print(min_coins(coins , n))
