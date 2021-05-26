# print the path of the stairs if you can take only 1,2,3 steps at each staircase.
#using memoization
# def printStairPath(n,output):
#     if n==0:
#         return 1
#     elif n<0:
#         return 0
    
#     if output[n]!=0:
#         return output[n]

#     n1=printStairPath(n-1,output)
#     n2=printStairPath(n-2,output)
#     n3=printStairPath(n-3,output)

#     npath=n1 + n2 + n3
#     output[n]=npath
#     return npath

# n=int(input())
# output = [0]*(n+1)
# totalpath=printStairPath(n,output)
# print("Total Path = {}".format(totalpath))



# Solving the same problem using Tabulation

def printStairPath(n):

    output=[0]*(n+1)

    output[0]=1
    output[1]=1
    output[2]=2

    for i in range(3,n+1):
        output[i]=output[i-1] + output[i-2] + output[i-3]

    return output[n]

n= int(input())
npath=printStairPath(n)
print("Total Path = {} ".format(npath))