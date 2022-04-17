

class PetAnimal:
     """
     this class creates the animal instance node with the given value 
     """

     def __init__(self,pet_name)  :
         self.value=pet_name
         self.next=None
    

class Cat:
    """
    1- this class inherets the properties from animal class 
    2- create cat node 
    """
    pet_type="Cat"

class Dog:
    """
    1- this class inherets the properties from animal class 
    2- create Dog node 
    """
    pet_type="Dog"

class AnimalShelter :


   def __init__(self) :

    """
     holds only dogs and cats.
    The shelter operates using a first-in, first-out approach.
    """
    # (class) Queue() Create a Queue class that has a front property.
    #  It creates an empty Queue when instantiated. 
    # This object should be aware of a default empty value assigned to front 
    # when the queue is created.
    self.frontcat=None
    self.rearcat=None
    self.frontdog=None
    self.reardog=None



    

   def enqueue( self , animal):
       """
       Arguments: animal
       animal can be either a dog or a cat object.
       """

       #Return whether an object is an instance of a class or of a subclass thereof.
       if  animal.type=="cat" :
           if self.frontcat==None :
               self.frontcat=animal
               self.rearcat=animal
           else:
               self.rearcat.next=animal
               self.rearcat=animal

       if  animal.type=="dog" :
           if self.frontdog==None :
               self.frontdog=animal
               self.reardog=animal
           else:
               self.reardog.next=animal
               self.reardog=animal

            
               
            
   def  dequeue(self, pref):
         """Arguments: pref
            pref can be either "dog" or "cat"
            Return: either a dog or a cat, based on preference.
            If pref is not "dog" or "cat" then return null.
         """

         if pref=="cat" and self.frontcat !=None:
             temp=self.frontcat
             self.frontcat=temp.next
             temp.next=None
             return temp.name
        
         elif pref=="dog" and self.frontdog!=None:
             temp=self.frontdog
             self.frontdog=temp.next
             temp.next=None
             return temp.name
         else:
             return 'null'

class Cat():
    def __init__(self,name) :
        self.name,self.type,self.next=name, 'cat',None
      
         
class Dog():
    def __init__(self,name) :
        self.name,self.type,self.next=name, 'dog',None
      
 

        


###################################################################################
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
        
             
             
 


###########################  queue  #####################3
class Queue:

    """ 
    Create a Queue class that has a front property. 
    It creates an empty Queue when instantiated.
    This object should be aware of a default empty value assigned to front when the queue is created.
    """
    def __init__(self) :
        self.front=None
        self.rear=None

    def  enqueue (self,value):
        """
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance.
        """
        new_node=Node(value)

        # rear node will point to the new node + the rear will be thw new node 
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        
        #else the new node will be both front and rear
        else :
            self.rear=self.front=new_node

    def dequeue(self):
        """
        Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        """
        if self.front==None:
             raise AttributeError("the queue is empty , so there is no nodes to remove ")
 
        else : 
            deq_node=self.front.next
            #the new front will be the next node 
            self.front=self.front.next
            #if the new front is None then the rear should be none too
            if self.front==None:
                self.rear=None
            return deq_node


    def peek(self):
        """
        Arguments: none
        Returns: Value of the node located at the front of the queue
        Should raise exception when called on empty stack
        """
        
        # firstly i will check the front that its not empty , 
        # because the peek is from front
        if self.front==None:
            raise AttributeError("the queue is empty   ")

        # give the value of the front of queue
        return self.front.value

    def q_is_empty(self):

        """
        is empty
        Arguments: none
        Returns: Boolean indicating whether or not the queue is empty
        """
        if self.rear==None:
            return True
        return False

    def q_display(self):

        qnode =self.front
        result=""

        
        if self.q_is_empty()==True:
            return "the stack is empty "
            
        else:
            while(qnode!=None):
                        result+=f"{qnode.value} <= "   
                        qnode=qnode.next
            
        return (result)

 