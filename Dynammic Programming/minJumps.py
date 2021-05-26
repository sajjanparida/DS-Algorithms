# # given an array of integers, write a  program to reach end
def minJumps(n,arr):

    output=[None]*(n+1)

    output[n]=0

    for i in range(n-1,-1,-1):
        if arr[i]>0:
            minjump = float('INF')

        for k in range(1,arr[i]+1):
            if i+k < len(output) and output[i+k]!=None:
                minjump= 1+ min(minjump,output[i+k])
        output[i] = minjump
    
    print("Output array is {}".format(output))
    return output[0]

n=int(input())
arr=[int(x) for x in input().split(' ')]
print("Minimum Jumps : {} ".format(minJumps(n,arr)))
