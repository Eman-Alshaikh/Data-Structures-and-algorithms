 


from queue import Queue
from typing_extensions import Self


class Node : 
    """
     Node class that has properties for the value stored in the node,
     the left child node, 
    and the right child node.
    
    """
    def __init__(self,value=None,left=None,right=None) :
        self.value=value
        self.left=left
        self.right=right


class  BinaryTree:
    """
    Create a Binary Tree class
    Define a method for each of the depth first traversals:
    pre order
    in order
    post order which returns an array of the values, ordered appropriately.
    """
    def __init__(self,root=None) :
        self.root=root

    def pre_order(self):

        values=[]

        def walk(root):
            if root is None:
                return
            if root : 
                values.append(root.value)
                walk(root.left)
                walk(root.right)

        walk(self.root)
        return values

    def in_order(self):

        values=[]
        if self.root==None:
                return

        def walk(node):
            
            if node :                
                walk(node.left)

                values.append(node.value)
                walk(node.right)

        walk(self.root)
        return values

    def post_order(self):

        values=[]
        if self.root==None:
                return

        def walk(node):
            
            if node :                
                walk(node.left)
                walk(node.right)
                values.append(node.value)
                

        walk(self.root)
        return values

############################# 17 ###################### 

    def breadth_first(self,tree): 
         
        q_list=[]
        values=[]

        if tree.root:
            q_list.insert(0,tree.root)

        while(q_list):
            node=q_list.pop()
            values.append(node.value)

            if node.left:
                q_list.insert(0,node.left)
            
            
            if node.right:
                q_list.insert(0,node.right)
        return values


 

             


            



            


class BinarySearchTree(BinaryTree):
    """
    Create a Binary Search Tree class
    This class should be a sub-class (or your languages equivalent)
    of the Binary Tree Class, with the following additional methods:
    """

    def add(self,value):
        """
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location
         in the binary search tree.


        """
        def walk(root):
            if value<root.value:
                if root.left is None:
                    root.left=Node(value)
                else : 
                    walk(root.left)
            else : 
                if root.right is None:
                    root.right=Node(value)
                else:
                    walk(root.right)
        walk(self.root)


    def contains(self,value):
        """
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        """
        def walk(root):
            if root is None :
                return False
            elif root.value==value:
                return True
            elif value<root.value:
                return walk(root.left)
            else : 
                return walk(root.right)
             
        return walk(self.root)


 