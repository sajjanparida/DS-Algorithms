write a program to merge two sorted arrays

def merge_sorted_arrays(arr,aux,lo,mid,hi):
    i=lo
    j=mid+1
    k=lo
    while i<=mid and j<= hi:

        if arr[i] <= arr[j] :
            aux[k] = arr[i]
            k += 1
            i += 1
        else:
            aux[k]=arr[j]
            k += 1
            j +=1

    while i <= mid :
        aux[k] = arr[i]
        k += 1
        i += 1

    for i in range(lo,hi+1):
        arr[i] = aux[i]


def merge_sort(arr,aux,lo,hi):
    
    if lo==hi:
        return

    mid= (lo + hi )//2

    merge_sort(arr,aux,lo,mid)
    merge_sort(arr,aux,mid+1,hi)
    merge_sorted_arrays(arr,aux,lo,mid,hi)


arr=[2,4,6,8,10,12,14,1,3,5,7,9]
aux=arr.copy()

merge_sort(arr,aux,0,len(arr)-1)

for i in arr:
    print(i ,end=' ')