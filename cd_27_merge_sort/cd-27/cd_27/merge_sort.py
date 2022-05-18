 

def merge_sort(array):
    n=len(array)

    def merge(left,right,array):
        i=0
        j=0
        k=0

        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                array[k]=left[i]
                i+=1

            else : 
                array[k]=right[j]
                j+=1

            k+=1

        if i==len(left):
            for i in right[j:]:
                array[k]=i
                k+=1

        else:
            for i in left[i:]:
                array[k]=i
                k+=1
    if n>1:
        mid=n//2
        left=array[0:mid]
        right=array[mid:n]
        merge_sort(left)
        merge_sort(right)
        merge(left,right,array)
    
    return array
    

