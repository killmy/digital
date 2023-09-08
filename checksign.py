from stack import MinStack
# 括号匹配 [] () {}
# 1.左括号等于右括号
# 2.必须左匹配右，不是右匹配左
# 3.last opened first closed
def check_sign(check_object):
    # sign = ['[','{','(']
    sign = {'[':']','{':'}','(':')'}
    check_stack = MinStack()
    for s in check_object:
        if s in sign:
            check_stack.push(s)
            # print(s)
    if check_stack.s_top == -1:
        return True
    return False
# while True:
#     input_str = input()
#     if input_str == 'q':
#         break
#     check_sign(input_str)
        
    