def assign_cookies()->int:
    g = [ 1 , 2 , 4 , 8 , 6] 
    s =[ 1 , 2 , 3 , 2 , 4 , 7]
    g.sort()
    s.sort()
    n = len(g)
    m = len(s)
    left = 0 
    right = 0
    count = 0
    while left < n and right < m :
        if g[left] <= s[right]:
            count += 1
            left += 1
        right += 1
    return count
print(assign_cookies())