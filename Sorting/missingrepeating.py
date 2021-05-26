def findTwoElement(arr, n): 
        # code here
        
        result=[-1,-1]
        arrsum=0
        expectedsum=0
        for i in range(0,n):
            expectedsum += i+1
            arrsum=arr[i]        
    
        return result
arr=[13,33,43,16,25,19,23,31,29 ,35 ,10 ,2 ,32 ,11 ,47 ,15 ,34 ,46 ,30 ,26 ,41 ,18 ,5 ,17 ,37 ,39 ,6 ,4 ,20 ,27 ,9 ,3 ,8 ,40 ,24 ,44 ,14 ,36 ,7 ,38 ,12 ,1 ,42 ,12 ,28 ,22 ,45]
print(findTwoElement(arr,47))