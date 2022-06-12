
 
 

class Node : 

    def __init__(self, value)  :
       
       self.value=value
       self.next=None

class LinkedList:

    def __init__(self) :
        self.head=None

    
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

        new_node=Node(value)
        if not self.head:
            self.head=new_node
        else:
            print("this LL has  a head")

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
        return the value of a key ...
        """

        if self.head:
            current=self.head
            while current:
                if current.value[0]==value:
                    return current.value
                current=current.next
        
        else:
            print ("the key is not found")

