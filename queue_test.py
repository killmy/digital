# 队列至少插入2，数组实现队列的方式并不好还是链表比较好
class Array_Queue(object):
    def __init__(self,size) -> None:
        self.queue_list = [0]*size 
        self.front = -1
        self.rear = -1
        self.size = size
    def isEmpty(self):
            return self.rear == self.front
    def isFull(self):
        return (self.rear+1)%self.size == self.front
    def Enqueue(self,x):
        if self.isFull():
            return
        elif self.isEmpty():
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.size
            
        self.queue_list[self.rear] = x 
    def Dequeue(self):
        if self.isEmpty():
            return
        elif self.front == self.rear:
            self.rear = self.front = -1
        else:
            self.front = (self.front + 1) % self.size 
    def get_front(self):
        if self.isEmpty():
            return -1
        return self.queue_list[self.front]
    def get_rear(self):
        if self.isEmpty():
            return -1
        return self.queue_list[self.rear]
class Node(object):
    def __init__(self,x) -> None:
        self.val = x
        self.next = next
class List_Queue(object):
    def __init__(self) -> None:
        self.rear = None
        self.front = None
    def isEmpty(self):
        return self.front == self.front ==None
    def Enqueue(self,x):
        node = Node(x)
        if self.isEmpty():
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node
    def Dequeue(self,x):
        if self.isEmpty():
            return -1
        elif self.rear == self.front:
            self.rear = self.front = None
        else:
            self.front = self.front.next
    def get_front(self):
        if not self.front:
            return -1
        return self.front.val
    def get_rear(self):
        if not self.rear:
            return -1
        return self.rear.val