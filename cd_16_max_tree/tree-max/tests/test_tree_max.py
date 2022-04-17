from tree_max.max_tree import BinarySearchTree,BinaryTree,Node


 

def test_max_value():

     t=BinarySearchTree()
     t.add(10)
     t.add(20)
     t.add(30)
     assert t.max_value()==30


