from cd_33_left_join.hash import HashTable


def left_join(ht_1,ht_2):
     
     lst=[]

     for element in ht_1:
         if element:
             j=0
             current_element=element[j]
             while current_element:
                 key=current_element[0]
                 if ht_2.contains(key):
                     lst.append([key,current_element[1],ht_2.get(key)])

                 else:
                     
                    lst.append([key,current_element[1],None])

                 try:
                     if element[j+1]:
                         j+=1
                         current_element=element[j]

                     else:
                         current_element=None
                 except:
                        break
     return lst



