# Give an array containing 0 and 1, partition the array into two parts


def partionalarray(arr):

    i=j=0
    k= len(arr)-1
    while i <= k:
        if arr[i] > 1:
            arr[i],arr[k]=arr[k],arr[i]
            k -= 1
        elif arr[i] > 0:
            i += 1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j += 1

arr=[0,1,1,2,1,0,1,2,0,1,0,2,0,1,2,1]

pindex=partionalarray(arr)
print( " Partition Index of array is {} ".format(pindex))
for i in arr:
    print(i , end=' ')
