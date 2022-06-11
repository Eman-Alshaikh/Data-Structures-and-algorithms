

class Node : 


    def __init__(self,data=None,next=None)  :
       
       self.data=data
       self.next=next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


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

    def insert(self,value=None):
        """
        add a value to the head of the linked list

        """

        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

    def includes(self,value):
        """
        return True if the value is in the LL 
        and return FALSE if the the value is not in the LL 
        """
        current=self.head
        
        while current!=None:
                if current.getData()==value:
                    return True
                 
                else : 
                    current=current.getNext()
        return False


    def append(self,value):
        node=Node(value)
        current=self.head
        if current==None:
            self.head=node
        else:
            while current.next != None:
                current=current.next
            current.next=node

    
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