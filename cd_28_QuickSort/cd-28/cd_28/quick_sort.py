

 
 

def quick_sort_fun(arr,left,right):
    if left<right:
        # partition the array by setting the position of the pivot value 
        position=partition(arr,left,right)

        #sort the left 
        quick_sort_fun(arr,left,position-1)


        #sort the right 
        quick_sort_fun(arr,position+1,right )

    return arr


def partition(arr,left,right):

    #set a pivot value as a point of reference
    pivot=arr[right]
    #create a variable to track the largest index of numbers lower than the defined pivot 
    low=left-1
    for i in range(left,right):
        print(arr,i,pivot)
        if arr[i]<=pivot:
            low+=1
            arr[i],arr[low]=arr[low],arr[i]
    
    #place the value of the pivot location in the middle 
    #all numbers smaller than the pivot are on the left , larger on the right
    arr[low+1],arr[right]=arr[right],arr[low+1]
    #return the pivot index point
    return low+1



