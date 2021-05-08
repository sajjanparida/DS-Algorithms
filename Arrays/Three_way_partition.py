# Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order. You are required to return the modified array


def three_way_partition(arr,n,a,b):

    l=0
    r=n-1
    i=0
    while i < r:

        if (arr[i] < a):
            arr[i],arr[l]= arr[l],arr[i]
            l += 1
            i += 1
            print("l: {} , i : {}".format(l,i))
        elif arr[i] > b:
            arr[i],arr[r] =arr[r],arr[i]
            r -= 1
            print("r: {} , i : {}".format(r,i))
        else: 
            i += 1
    return arr

arr=[76,8 ,75, 22, 59, 96, 30, 38, 36]
print("Output array is {}".format(three_way_partition(arr,9,44,62)))


