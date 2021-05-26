# given a matrix containing values in rows and colums, find the maximum cost
# from top left corner to bottom ight corner


def fmincost(arr,m,n,i,j,output):
    mincost=0
    if i==m-1 and j==n-1:
        return arr[i][j]
    elif i==m-1:
        return arr[i][j] + fmincost(arr,m,n,i,j+1,output)
    elif j==n-1:
        return arr[i][j] + fmincost(arr,m,n,i+1,j,output)

    if output[i][j] != None:
        return output[i][j]

    mincost = arr[i][j] +  min(fmincost(arr,m,n,i+1,j,output),fmincost(arr,m,n,i,j+1,output))

    output[i][j] = mincost

    return mincost

m=int(input())
n=int(input())
arr=[]

for i in range(0,m):
    temparr=[]
    for j in range(0,n):
        #print("Enter the value at {} : {}".format(i,j))
        temparr.append(int(input()))
    arr.append(temparr)

output = [[None]*m]*n
output_value=fmincost(arr,m,n,0,0,output)
print("Minimum Value is : {}".format(output[m-1][n-1]))
        