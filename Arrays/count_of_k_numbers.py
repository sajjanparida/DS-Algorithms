#Given an array of size n and a number k, find all elements that appear more than n/k times

def count_of_arrays(arr,n,k):

    dictionary={}
    req_count= n//k
    for  i in arr:
        if dictionary.get(i)==None:
            dictionary[i]=1
        else:
            dictionary[i] = dictionary[i] + 1

    output_array=[]
    for  i in dictionary:
        if dictionary[i] > req_count:
            output_array.append(i)

    return output_array

array=[3, 1, 2, 2, 1, 2, 3, 3]
arr=count_of_arrays(array,len(array),4)

for i in arr:
        print(i,end=' ')