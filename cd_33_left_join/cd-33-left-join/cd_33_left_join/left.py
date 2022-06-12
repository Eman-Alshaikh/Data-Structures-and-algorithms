 
from cd_33_left_join.hash import Hashtable


def left_join(ht_1,ht_2):
      
      result=[]


      for element in ht_1 :
          if element: 
               j=0
               current=element[j]

               while current:
                    key=current[0]
                    if ht_2.contains(key):
                         result.append([key,current[1],ht_2.get(key)])

                    else : 
                         result.append([key,current[1],None])

                    try:
                         if element[j+1]:
                              j+=1
                              current=element[j]
                         else:
                              current=None
                    except:
                         break
      return result

                    