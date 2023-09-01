class MinStack(object):
    def __init__(self) -> None:
        self.stack = []
        self.s_top = -1
        self.min_stack = []
        self.min_top = -1
    def push(self, x: int) -> None:
        self.s_top += 1
        self.stack.insert(self.s_top,x)
        if self.min_top < 0 or self.min_stack[self.min_top] >= x:
            self.min_top += 1
            self.min_stack.insert(self.min_top,x)
        
    def pop(self) -> None:
        if self.s_top < 0:
            # return False
            return
        # return_val = self.stack[self.s_top]
        if self.stack[self.s_top] == self.min_stack[self.min_top]:
            self.min_top -= 1
        self.s_top -= 1
        # return return_val
    def top(self) -> int:
        return self.stack[self.s_top]
    def min(self) -> int:
        return self.min_stack[self.min_top]
    def __repr__(self) -> str:
        a = []
        for i in range(self.s_top+1):
            a.insert(0,self.stack[i])
        return " ".join(map(str,a))
    def min_val(self) -> str:
        a = []
        for i in range(self.min_top+1):
            a.insert(0,self.min_stack[i])
        return a
stack = MinStack()
# [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483646,2147483646,null,2147483646,2147483646,null,2147483646]
# stack.push(2147483646)
# stack.push(2147483646)
# stack.push(2147483647)
# # print(stack.min_top)
# print(stack)
# for i in range(stack.min_top+1):
#     print(stack.min_stack[i])
# stack.pop()
# stack.pop()
# stack.pop()
# print('2')
# print(stack)
# for i in range(stack.min_top+1):
#     print(stack.min_stack[i])
# stack.push(2147483647)
# print(stack)
# stack.push(2147483647)
