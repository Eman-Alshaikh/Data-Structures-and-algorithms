 
from tree_breadth_first.t_b_f import BinaryTree,Node

 

def test_b_f():
    tree=BinaryTree()
    tree.root=Node(2)
    tree.root.left=Node(7) 
    tree.root.left.left=Node(2)
    tree.root.left.right=Node(6)
 
     
    tree.root.left.right.left=Node(5)
    tree.root.left.right.right=Node(11)
    tree.root.right=Node(5)
    tree.root.right.right=Node(9)
    tree.root.right.right.left=Node(4)
    

    assert tree.breadth_first() ==[2,7,5,2,6,9,5,11,4]




