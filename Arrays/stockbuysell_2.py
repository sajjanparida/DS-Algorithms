
def infiniteTransactionStock(prices):

    buy_point=0
    selling_point=0
    profit=0
    for  i in range(1, len(prices)):
        if prices[i]>prices[i-1]:
            selling_point += 1
        else:
            profit += prices[selling_point] - prices[buy_point]
            buy_point=i
            selling_point = i
            
    profit += prices[selling_point] - prices[buy_point]


    return profit

prices= [int(x) for x in input().split(' ')]
print("Maximum Value: {}".format(infiniteTransactionStock(prices)))