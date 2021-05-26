#program to find the maximum profit when only 1 transactions is allowed.


def oneTransactionStock(prices,n):
    profit=0
    left_so_far=float('INF')
    
    for i in range(0,n):
        
        if prices[i]<left_so_far:
            left_so_far = prices[i]
        
        if prices[i]-left_so_far > profit:
            profit=prices[i]-left_so_far
    
    return profit


n=int(input())
prices=[int(x) for x in input().split(' ')]

print("The value is {} ".format(oneTransactionStock(prices,n)));