#find the majority element from the array

def majority_element(arr,n):

    majority=arr[0]
    count=1


    for  i in range(1,n):

        if(arr[i]==majority):
            print(f'Current element is {arr[i]} and majority is {majority}')
            count += 1
        else:
            count -=1
            print(f'Current element is {arr[i]} and majority is {majority}',end=' ')
            print("Count is {}".format(count))
            if count == 0:
                majority =arr[i]
                count += 1
    count = 0
    for i in arr:
        if i==majority:
            count += 1
    if count <=  n/2:
        majority=-1
                
    print("The majority element is {}".format(majority))

arr=[1 ,2 ,1 ,2 ,1 ,2 ,1 ,2 ,1 ,2 ,1 ,1 ,2 ,2 ,2 ,2 ,2 ,1 ,1 ,2 ,2 ,1 ,1 ,1 ,2 ,2 ,2 ,1 ,2 ,1 ,2 ,1 ,1 ,2 ,2 ,1 ,2 ,2 ,2 ,1 ,2 ,1 ,1 ,1 ,2 ,2 ,1 ,1 ,1 ,1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1 ,2, 1, 1, 2, 2, 2, 1]

majority_element(arr,101)

        