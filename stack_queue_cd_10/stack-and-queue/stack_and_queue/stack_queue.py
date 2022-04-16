

 


class Node:

    """ 
    Node class : has properties for the value stored in the Node,
    and a pointer to the next node.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
    
    Stack class : has a top property. 
    It creates an empty Stack when instantiated.
    This object should be aware of a default empty value
     assigned to top when the stack is created.
    """

    def __init__(self,node=None):
        self.top = None

    def push(self, value):
        """
        push
        Arguments: value
        adds a new node with that value to the top of the stack 
        with an O(1) Time performance.
        """

        # IF the stack is empty 
        if self.top== None:
            self.top = Node(value)
        else:
            # create the node  to be the top 
            new_node = Node(value)

            new_node.next = self.top
            self.top = new_node

    def pop(self):
        """ 
        Arguments: none
       Returns: the value from node from the top of the stack
       Removes the node from the top of the stack
       Should raise exception when called on empty stack
       """

        if self.is_empty()==True:
            raise AttributeError("the stack is empty , so there is no nodes to remove ")

        else:
            #store the top in a temporary value (poped_node)
            poped_node = self.top
            self.top = self.top.next
            poped_node.next = None
            return poped_node.value

    def peek(self):
        """ 
        Arguments: none
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack
        """
        if self.is_empty()==True:
            raise AttributeError("the stack is empty ")

        else:
            return self.top.value

    def is_empty(self):
        """ 
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty.
        """
        #check the value of the top if it is none return true , that means the stack is empty 
        if self.top== None:
            return True
        else:
            return False

    def display_stack(self) :

        
         node =self.top
         result=""

     
         if self.is_empty()==True:
                return "the stack is empty "
           
         else:
            while(node!=None):
                    result+=f"{node.value} | "   
                    node=node.next
         
         return (result)
        
             
             
 

        
               
 

if __name__== "__main__":
    mystack=Stack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)

    # get the top of this stack :
    print(mystack.peek())

    # delete element from the stack :
    mystack.pop()
    print(mystack.peek())
    print(mystack.display_stack())

    
