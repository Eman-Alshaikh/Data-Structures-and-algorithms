from cd_32.tree_inter import tree_intersection

from cd_32.tree_inter import BinarySearchTree

def test_1():
    tree1=BinarySearchTree()
    tree1.add(1)
    tree1.add(3)
    tree1.add(5)
    tree1.add(7)
    tree1.add(9)
    tree1.add(11)

    tree2=BinarySearchTree()
    tree1.add(100)
    tree1.add(3)
    tree1.add(50)
    tree1.add(7)
    tree1.add(90)
    tree1.add(110)

    assert tree_intersection(tree1,tree2)==[3,7]