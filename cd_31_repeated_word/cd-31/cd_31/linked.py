
 
 

from multiprocessing import Value

class Node : 

    def __init__(self, value,next=None)  :
       
       self.value=value
       self._next=next
 
class LinkedList:

    def __init__(self,iterable=[]) :
        self.head=None
        self._size=0

    
    def append(self,value):
        if self.head is None:
            self.insert(value)
        
        else : 
            current=self.head
            while current:
                if current._next is None:
                    current._next=Node(value)
                    self._size+=1
                    break
            
                current=current._next

 

    def add(self,value):
        node=Node(value)
        if not self.head:
            self.head=node
        else:
            current=self.head
            while current.next:
                current=current.next
            
            current.next=node

    def insert(self,value):
        """
        add a value to the head of the linked list

        """
 
        self.head=Node(value,self.head)
        self._size+=1

    def includes(self,value):
        """
        return True if the value is in the LL 
        and return FALSE if the the value is not in the LL 
        """

        if self.head:
            current=self.head
            while current:
                if current.value[0]==value:
                    return True
                current=current.next
            return False
        else : 
            print ("this linked list is empty , so please insert a value firstly ")

    
    def get(self,value):
        """
        return the value of a key
        """

        if self.head:
            current=self.head
            while current:
                if current.value[0]==value:
                    return current.value
                current=current.next
        
        else:
            print ("the key is not found")


