from stack_queue_pseudo.qu_using_2_stacks import PseudoQueue
 
def test_is_PseudoQueu():
    PsQue=PseudoQueue()
    assert PsQue

def test_enq_deq_multiple_values():
    psqu=PseudoQueue()
    psqu.enque_mystack("1")
    psqu.enque_mystack("2")
    psqu.enque_mystack("3")

    psqu.deque_mystack()
    psqu.deque_mystack()

    actual=psqu.deque_mystack()
    expected="3"
    assert actual==expected

 
  


