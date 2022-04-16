from inspect import stack
from logging import exception
from re import S
import pytest
from stack_and_queue import __version__
from stack_and_queue.stack_queue import *

def test_version():
    assert __version__ == '0.1.0'

#Can successfully push onto a stack
def test_push_1_onto_stack():
    stak=Stack()
    stak.push(1)
    assert stak.top.value==1

#Can successfully push multiple values onto a stack
def test_push_multiple_onto_stack():
    stak=Stack()
    stak.push(1)
    stak.push(2)
    stak.push(3)
    assert stak.top.value==3

#Can successfully pop off the stack
def test_pop_off_stack():
    stak=Stack()
    stak.push(10)
    stak.push(20)
    stak.pop()
    assert stak.top.value==10
#Can successfully empty a stack after multiple pops
def test_empty_stack():
    stak=Stack()
    stak.push(10)
    stak.push(20)
    stak.pop()
    stak.pop()
    assert stak.is_empty()==True
    
 #Can successfully peek the next item on the stack
def test_PEEK_stack():
    stak=Stack()
    stak.push(10)
    stak.push(20)
  
    assert stak.peek()==20

#Can successfully instantiate an empty stack
def test_instantiate_stack():
    stak=Stack()
    assert stak.top==None

#Calling pop or peek on empty stack raises exception
def test_empty_stack_raises_exception_stack():
    stak=Stack()
    with pytest.raises(Exception):
        assert stak.peek()
    with pytest.raises(Exception):
        assert stak.pop()

 ###########################  queue  #####################3
#Can successfully enqueue into a queue
def test_enqueue_1():
    q=Queue()
    q.enqueue("eman")
    assert q.rear.value=="eman"


#Can successfully enqueue multiple values into a queue
def test_enqueue_multiple():
    q=Queue()
    q.enqueue(10)
    q.enqueue(20)
    assert q.rear.value==20
#Can successfully dequeue out of a queue the expected value
def test_enqueue_multiple():
    q=Queue()
    q.enqueue(10)
    q.dequeue()
    q.enqueue(20)
    assert q.front.value==20
#Can successfully peek into a queue, seeing the expected value
def test_peek_queue():
    q=Queue()
    q.enqueue(10)
   
    q.enqueue(20)
    assert q.peek()==10
#Can successfully empty a queue after multiple dequeues
def test_empty_queue():
    q=Queue()
    q.enqueue(10)
   
    q.enqueue(20)
    q.dequeue()
    q.dequeue()
    assert q.q_is_empty()==True
#Can successfully instantiate an empty queue
def test_instantiate_queue():
    q=Queue()
     
    assert q.front==None
    assert q.rear==None
#Calling dequeue or peek on empty queue raises exception
def test_empty_queu_raises_exception_stack():
    q=Queue()
    with pytest.raises(Exception):
        assert q.peek()
    with pytest.raises(Exception):
        assert q.dequeue()