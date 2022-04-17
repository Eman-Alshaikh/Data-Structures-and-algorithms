class Node : 
    """
     Node class that has properties for the value stored in the node,
     the left child node, 
    and the right child node.
    
    """
    def __init__(self,value) :
        self.value=value
        self.left=None
        self.right=None


class  BinaryTree:
    """
    Create a Binary Tree class
    Define a method for each of the depth first traversals:
    pre order
    in order
    post order which returns an array of the values, ordered appropriately.
    """
    def __init__(self) :
        self.root=None

    def pre_order(self):
        try:
            if not self.root:
                return"the tree is empty "
            else :


                values=[]

                def order_tree(node):
                  nonlocal values
                  values+=[node.value]
                  if node.left:
                      order_tree(node.left)
                  if node.right:
                      order_tree(node.right)
                  return values
                return order_tree(self.root)
        except :
            print("there is something wrong ")


    def in_order(self):

        try:
            if not self.root:
                return"the tree is empty "
            else :


                values=[]

                def order_tree(node):
                  
                  if node.left:
                      order_tree(node.left)
                
                  nonlocal values
                  values+=[node.value]
                  if node.right:
                      order_tree(node.right)
                  return values
                return order_tree(self.root)
        except :
            print("there is something wrong ")


    def post_order(self):

        try:
            if not self.root:
                return"the tree is empty "
            else :


                values=[]

                def order_tree(node):
                  
                  if node.left:
                      order_tree(node.left)
                
                 
                  if node.right:
                      order_tree(node.right) 
                  nonlocal values
                  values+=[node.value]
                  return values
                final_output= order_tree(self.root)
                return final_output

        except :
            print("there is something wrong ")

    ################################# cd 16 ##############################


    def max_value(self) :

        if not self.root:
            return"the tree is empty "
        _max=self.root.value

        def _max_value(node):

            nonlocal _max
            if   node.value > _max :
                _max=node.value
            else :
                _max

            if node.left:
               _max_value(node.left)   
            if node.right:         
              _max_value(node.right)

        _max_value(self.root)
        return  _max






class BinarySearchTree(BinaryTree):
    """
    Create a Binary Search Tree class
    This class should be a sub-class (or your languages equivalent)
    of the Binary Tree Class, with the following additional methods:
    """
    def __init__(self):
        super().__init__()

    def add(self,value):
        """
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location
         in the binary search tree.


        """
        try : 
            if not self.root : 
                self.root=Node(value)
            else: 
                node=self.root
                while node:
                    if node.value>value:
                        if not node.left:
                            node.left=Node(value)
                            break
                        node=node.left
                    else : 
                        if not node.right:
                            node.right=Node(value)
                            break
                        node=node.right
        except :
            print("there is something wrong ")

    def contains(self,value):
        """
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        """
        try : 
            if not self.root : 
                return "the tree is empty "
            else: 
                node=self.root
                while node:
                    if node.value==value:
                        return True
                    if node.value>value:
                        if not node.left:
                            return "the value is not in the tree"
                        node=node.left
                    else : 
                        if  node.right==None:
                            return "the value is not in the tree"

                        node=node.right
        except :
            print("there is something wrong ")