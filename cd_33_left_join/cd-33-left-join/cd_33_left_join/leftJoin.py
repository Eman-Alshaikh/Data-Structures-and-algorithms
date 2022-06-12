from array import array

from more_itertools import bucket
from cd_33_left_join.hash import HashTable


def left_join(left,right):
      
      result=[]


      for item in left._buckets :
          if item: 
               current=bucket.head
               while current:
                    left_column=[current.data[0],current.data[1]]
                    right_value=right.get(current.data[0])
                    left_column.append(right_value)
                    current=current.next
               result.append(left_column)
      return result
              

 