

from tkinter.messagebox import NO


class Node : 
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
    
    def getValue(self):
        return self.value
    
    def getNext(self):
        return self.next


class Queue:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear

    def enqueue(self,value):
        node=Node(value)
        if self.front is None:
            self.front=node
            self.rear=node

        else:
            self.rear.next=node
            self.rear=node


    def dequeue(self):
        if self.is_empty():
            print('the queue is empty')
        node=self.front
        self.front=self.front.next
        return node.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
    


