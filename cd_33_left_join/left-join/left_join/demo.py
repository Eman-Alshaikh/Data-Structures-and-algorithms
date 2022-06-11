
from left_join.linked import LinkedList as LL

class HashTable:
 
    def __init__(self,max_size=1024):

          self.max_size=max_size
          self.buckets=[LL() for _ in range(self.max_size)]
          if type(max_size) is not int :
              raise TypeError('max size must be integer')
          if max_size<1:
              raise ValueError('max size must be positive integer')

        

    def _has_key(self,key):
        if type(key) is not str : 
            raise TypeError('KEY must be string')

        sum =0
        for char in key:
            sum+= ord(char)
        return sum % len(self.buckets)


    def set (self,key,val):
        self.buckets[self._has_key(key)].append({key:val})

    def get (self ,key ):
        current=self.buckets[self._has_key(key)].head
        while current:
            if key in current.val.keys():
                return current.val[key]
            current=current._next
        return 'NULL'


         

        def left_join(hash1,hash2):
                result=[]
                for each in hash1.buckets:
                    if each:
                        for node in each.display():
                            result.append(list(node.keys())[0])
                            result[-1]=[result[-1], hash1.get(result[-1]), hash2.get(result[-1])]
                return result
 
 

 

