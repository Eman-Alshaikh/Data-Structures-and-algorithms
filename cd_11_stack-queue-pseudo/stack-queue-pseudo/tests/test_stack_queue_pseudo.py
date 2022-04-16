from stack_queue_pseudo.qu_using_2_stacks import PseudoQueue,Stack
 
def test_is_PseudoQueu():
    PsQue=PseudoQueue()
    assert PsQue

def test_enq_1_value():
    psqu=PseudoQueue()
    psqu.enqueue(1)
    assert 1 ==psqu.rear


def test_enq_multiple_values():
    psqu=PseudoQueue()
    psqu.enqueue(1)
    psqu.enqueue(2)
    psqu.enqueue(3)

    assert 3==psqu.rear
 
  

def test_dequeue():
    psqu=PseudoQueue()
    psqu.enqueue(1)
    psqu.enqueue(2)
    psqu.enqueue(3)
    psqu.dequeue()
    psqu.dequeue()


    assert 3==psqu.dequeue()
 

def test_dequeue_empty():
    psqu=PseudoQueue()
    


    assert None==psqu.dequeue()
 



