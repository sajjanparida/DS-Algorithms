

def kthelement(arr1,arr2,n,m,k):

    kthelement=0
    i=0
    j=0
    l=0
    while l < k:
        if arr1[i]<arr2[j]:
            kthelement =arr1[i]
            i += 1
            l += 1     
        else:
            kthelement = arr2[j]
            j+=1
            l += 1
    if i==n:
        while l<k:
            kthelement = arr2[j]
            j+=1
            l += 1
    elif j==m:
        while l<k:
            kthelement =arr1[i]
            i += 1
            l += 1  

    return kthelement
    
arr1=[2,3,6,7,9]
arr2=[1,4,8,1]
kthelement(arr1,arr2,5,4,5)

