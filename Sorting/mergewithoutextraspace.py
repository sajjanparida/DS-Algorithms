 

def merge(arr1,arr2,m,n):

    i=0
    j=0

    while i<m and j<n:

        if arr1[i] < arr2[j]:
            j += 1
            if arr2[j]<arr2[j-1]:
                arr2[j-1],arr2[j] = arr2[j],arr2[j-1]
                j -= 1
        elif arr2[j] < arr1[i]:
            arr2[j],arr1[i] = arr1[i],arr2[j]
            i += 1

    arr2.sort()

    for i in arr1:
        print(i,end=' ')
    for i in arr2:
        print(i,end=' ')

arr1=[1,3,5,7]
arr2=[0,2,6,8,9]
merge(arr1,arr2,4,5)
