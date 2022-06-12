from cd_32.tree_inter import  *

 
def test_trees():
    tree1=BinaryTree()
    tree2=BinaryTree()

    tree1.add(1)
    tree1.add(2)
    tree1.add(3)
    tree1.add(4)



     
    tree2.add(20)
    tree2.add(2)
    tree2.add(1)
    tree2.add(40)


     
    assert tree1.root.value==1
    assert tree2.root.value==20
    assert tree1.root.left.value==2

def test_intersection_trees():
    tree1=BinaryTree()
    tree2=BinaryTree()

    tree1.add(1)
    tree1.add(2)
    tree1.add(3)
    tree1.add(4)



     
    tree2.add(20)
    tree2.add(2)
    tree2.add(1)
    tree2.add(40)

     
    actual=tree_intersection(tree1,tree2)
    expected=[2,1]
    assert actual==expected

def test_empty_trees():
    tree1=BinaryTree()
    tree2=BinaryTree()

     
    tree1.add(1)
    tree1.add(2)
    tree1.add(3)
    tree1.add(4)

    actual=tree_intersection(tree1,tree2)
    expected=[ ]
    assert actual==expected

def test_allmatch_trees():
    tree1=BinaryTree()
    tree2=BinaryTree()

    tree1.add(1)
    tree1.add(2)
    tree1.add(3)
    tree1.add(4)
    tree2.add(1)
    tree2.add(2)
    tree2.add(3)
    tree2.add(4)
 
     
   
     
    actual=tree_intersection(tree1,tree2)
    expected=[4,2,3,1]
    assert actual==expected