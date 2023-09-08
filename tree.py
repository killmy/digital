class TreeNode():
    def __init__(self,x) -> None:
        self.val = x 
        self.left = None 
        self.right = None
class Tree(object):
    def __init__(self) -> None:
        self.root = None
    def Insert(self,value):
        self.root = self.Insert_back(self.root,value)
    def Insert_back(self,node,value):
        if not node:
            node = TreeNode(value)
        elif value <= node.val:
            node.left = self.Insert_back(node.left,value)
        else:
            node.right = self.Insert_back(node.right,value)
        return node
    def Search(self,value):
        return self.Search_back(self.root,value)
    def Search_back(self,node,value):
        if not node:
            return False
        elif node.val == value:
            return True
        elif value < node.val:
            return self.Search_back(node.left,value)
        else:
            return self.Search_back(node.right,value)
    def FindMin(self):
        if not self.root:
            return -1
        # p = self.root
        # while p.left:
        #     p = p.left
        # return p.val
        return self.FindMin_back(self.root)
    def FindMin_back(self,node):
        if not node.left:
            return node.val
        return self.FindMin_back(node.left)
    def FindMax(self):
        if not self.root:
            return -1
        # p = self.root
        # while p.right:
        #     p = p.right
        # return p.val
        return self.FindMax_back(self.root)
    def FindMax_back(self,node):
        if not node.right:
            return node.val
        return self.FindMax_back(node.right)
    def FindHeight_back(self,node):
        if not node:
            return -1
        return max(self.FindHeight_back(node.left),self.FindHeight_back(node.right))+1
    def FindHeight_root(self):
        return self.FindHeight_back(self.root)
    def LevelOrder(self,Node):
        a = []
        if not Node:
            return a
        Q = ListQueue()
        Q.push(Node)
        while not Q.isEmpty():
            current = Q.get_front()
            a.append(current.val)
            if current.left:
                Q.push(current.left)
            if current.right:
                Q.push(current.right)
            Q.pop()
        return a
    def LevelOrder_root(self):
        return self.LevelOrder(self.root)
    def Preorder_root(self):
        a = []
        return self.Preorder(self.root,a)
    def Preorder(self,Node,a):
        if Node==None:
            return
        a.append(Node.val)
        self.Preorder(Node.left,a)
        self.Preorder(Node.right,a)
        return a
    def Inorder_root(self):
        a = []
        return self.Inorder(self.root,a)
    def Inorder(self,Node,a):
        if Node==None:
            return
        self.Inorder(Node.left,a)
        a.append(Node.val)
        self.Inorder(Node.right,a)
        return a
    def Posorder_root(self):
        a = []
        return self.Posorder(self.root,a)
    def Posorder(self,Node,a):
        if Node==None:
            return
        self.Posorder(Node.left,a)
        self.Posorder(Node.right,a)
        a.append(Node.val)
        return a
class QueueNode(object):
    def __init__(self,treenode) -> None:
        self.val = treenode
        self.next = None
class ListQueue(object):
    def __init__(self) -> None:
        self.front = None
        self.rear = None
    def isEmpty(self):
        if self.front == self.rear == None:
            return True
        return False
    def push(self,value):
        if self.isEmpty():
            self.front = self.rear = QueueNode(value)
            return
        self.rear.next = QueueNode(value)
        self.rear = self.rear.next
    def pop(self):
        if self.isEmpty():
            return
        elif self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
    def get_front(self):
        if self.isEmpty():
            return -1
        return self.front.val
    def get_rear(self):
        if self.isEmpty():
            return -1
        return self.rear.val
    def print_all(self):
        p = self.front
        while p:
            print(p.val)
            p = p.next
tree = Tree()
tree.Insert(10)
tree.Insert(8)
tree.Insert(15)
tree.Insert(1)
tree.Insert(4)
tree.Insert(12)
# print(tree.Search(8))
# print(tree.Search(10))
# print(tree.Search(15))
# print(tree.Search(1))
# print(tree.FindMax())
# print(tree.FindMin())
# print(tree.FindHeight_root())
print(tree.LevelOrder_root())
print(tree.Preorder_root())
print(tree.Inorder_root())
print(tree.Posorder_root())
# queue = ListQueue()
# A1 = TreeNode(10)
# queue.push(A1)
# queue.print_all()
# A2 = TreeNode(11)
# queue.push(A2)
# queue.print_all()
# A3 = TreeNode(9)
# queue.push(A3)
# print('all:')
# queue.print_all()
# queue.pop()
# print('delet:')
# queue.print_all()
# queue.pop()
# print('delet:')
# queue.print_all()
# queue.pop()
# print('delet:')
# queue.print_all()