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

        