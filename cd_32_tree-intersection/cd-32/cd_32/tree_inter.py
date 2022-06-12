
from cd_32.linked import LinkedList as LL

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

    def contains (self,key):
        """
        Arguments: key
        Returns: Boolean, indicating if the key
        exists in the table already.
        """

        hashed_key=self.hash(key)
        if self.bucket[hashed_key]:
            return self.bucket[hashed_key].includes(key)

        return False


def tree_intersection(bt1,bt2):
    ht=HashTable()
    match_array=[]

    def _tree(current):
        ht.set(current.data,current.data)

        if current.left:
            _tree(current.left)

        if current.right:
            _tree(current.right)

    def _tree_check(current):
        if current:
            if ht.contains(current.data):
                match_array.append(current.data)
            if current.left:
                _tree_check(current.left)
            
            if current.right:
                _tree_check(current.right)

    _tree(bt1.root)
    _tree_check(bt2.root)
    return match_array


 