# TAKE t NUMBER OF TEST cases
# create a dictionary for the frequencies of remainders
# multiply the frequencies with complement frequencies or do nc2
# finally print the sum
t=int(input())
for _ in range(t):
    #arr = list(map(int, input().split()))
    #arr = arr[1:]
    #m = int(input())   # the number from which the sum of pair is divided
    arr = [10,9,4,5,7,2,8,20,21]
    m=15
    remainders = {}

    for num in arr:
        curr_rem = num%m
        if curr_rem in remainders:
            remainders[curr_rem]+=1   #* curr_rem = key and remainders[curr_rem] = values
        else:
            remainders[curr_rem]=1

    num_pairs = 0
    for rem in remainders:
        complement = m - rem
        pairs = 0
        if (complement==m) or (complement*2==m):
            pairs  = (remainders[rem]*(remainders[rem]-1))//2
        elif complement in remainders:
            pairs = remainders[rem]*remainders[complement]
            remainders[rem]=0
        num_pairs = num_pairs + pairs

print(num_pairs)    
       
        
        
    
    
