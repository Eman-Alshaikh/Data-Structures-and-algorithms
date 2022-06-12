from cd_33_left_join.linkedlist  import LinkedList



class HashTable(object):


    def __init__(self,size=1024):
        #size=1024
        self.size=size
        # map=[]

        self.map=[None]*size
         
      


    def set(self,key,value):
        """
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        Should a given key already exist, replace its value from the value argument given to this method.
        """

        hashed_key=self.hash(key)

        if not self.map[hashed_key]:
            self.map[hashed_key]=LinkedList()
        self.map[hashed_key].add((key,value))





 

    
    def get (self,key):
        """

        Arguments: key
        Returns: Value associated
         with that key in the table
        """

        hashed_key=self.hash(key)
        if self.map[hashed_key]:
            return self.map[hashed_key].get(key)[1]
        return "NULL"
 


    def contains (self,key):
        """
        Arguments: key
        Returns: Boolean, indicating if the key
        exists in the table already.
        """

        hashed_key=self.hash(key)
        if self.map[hashed_key]:
            return self.map[hashed_key].includes(key)

        return False


    def keys(self):
        """
        Returns: Collection of keys

        """
        
    def hash(self,key):
        """
        Arguments: key
        Returns: Index in the collection for that key
      

        """

        sum_of_ascci=0
        for char in key:
            asci_of_char=ord(char)
            sum_of_ascci+=asci_of_char

        temp=sum_of_ascci*17
        hashed_key=temp%self.size
        return hashed_key

  




if __name__ == '__main__':
    hash=HashTable()
    hash.set('eman',26)
    hash.set('nuha',10)
    hash.set('elyas',30)
    hash.set('mohammad',40)
    hash.set('rema','friend')
    dict={
        "key":"value"
    }
    dict["key2"]="val2"
    print(hash["eman"])
    print(dict["key"])
    print(dict["key2"])

    
    
