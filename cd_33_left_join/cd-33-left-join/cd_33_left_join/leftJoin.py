from array import array
from cd_33_left_join.hash import HashTable


def left_join(ht_1,ht_2):
      
      result=[]


      for item in ht_1.map :
          if item: 
              for i in item.display():
                  result.append(list(i.keys())[0])
                  result[-1]=[result[-1],ht_1.get(result[-1]),ht_2.get(result[-1])]

      return result 