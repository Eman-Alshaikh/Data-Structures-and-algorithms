 

from tree import __version__
from tree.tree import BinarySearchTree,BinaryTree,Node
import pytest


def test_version():
    assert __version__ == '0.1.0'

def test_emptry_tree():
    t=BinaryTree()
    actual=t.root
    expected=None
    assert actual==expected


def test_add_left():
    a=Node('a')
    b=Node('b')
    c=Node('c')
    t=BinaryTree(a)
    a.left=b
    a.right=c

    assert a.left==t.root.left
    assert a.right==t.root.right


def test_pre_order():

    a=Node('a')
    b=Node('b')
    c=Node('c')
    t=BinaryTree(a)
    a.left=b
    a.right=c

    assert a.left==t.root.left
    assert a.right==c




    order=t.pre_order()
    assert order==['a','b','c']


def test_in_order():

    a=Node('a')
    b=Node('b')
    c=Node('c')
    t=BinaryTree(b)
    b.left=c
    b.right=a

    assert b.left==c
    assert b.right==a

    assert b.left==t.root.left
    assert b.right==a




    order=t.in_order()
    assert order==['c','b','a']


def test_post_order():

    a=Node('a')
    b=Node('b')
    c=Node('c')
    t=BinaryTree(b)
    b.left=c
    b.right=a

    assert b.left==c
    assert b.right==a

    assert b.left==t.root.left
    assert b.right==a




    order=t.post_order()
    assert order==['c','a','b']

 
def test_serach_contains_tree_true():

     root=Node('c')
     t=BinarySearchTree(root)
     t.add('a')
     t.add('b')
     t.add('d')
     actual=t.contains('b')
     expected=True
     assert actual==expected


def test_serach_contains_tree_false():

     root=Node('c')
     t=BinarySearchTree(root)
     t.add('a')
     t.add('b')
     t.add('c')
     actual=t.contains('eman')
     expected=False
     assert actual==expected

def test_serach_contains_tree_empty():

  
     t=BinarySearchTree()
    
     actual=t.contains('eman')
     expected=False
     assert actual==expected

