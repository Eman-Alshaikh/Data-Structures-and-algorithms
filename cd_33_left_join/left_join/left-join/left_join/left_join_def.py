 
from left_join.hash import Hashtable


def left_join_fun(left,right):
      
      result=[]


      for bucket in left._buckets :
          if bucket: 
               current=bucket.head
               while current:
                    left_column=[current.data[0],current.data[1]]
                    right_value=right.get(current.data[0])
                    left_column.append(right_value)
                    current=current.next
               result.append(left_column)
      return result
              

 