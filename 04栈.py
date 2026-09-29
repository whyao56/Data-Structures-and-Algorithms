# # ===== 方式1：直接用 list 当栈 =====
# stack = []
# stack.append("A")    # 压栈：放入 A
# stack.append("B")    # 压栈：放入 B
# stack.append("C")    # 压栈：放入 C
# print(stack)         # ['A', 'B', 'C']  （列表末尾 = 栈顶）
#
# top = stack.pop()    # 弹栈：拿走最上面的 C
# print(top)           # C
# print(stack)         # ['A', 'B']
# print(stack[-1])     # 看栈顶：B（但没拿走它）
#
# # ===== 方式2：包一个 Stack 类，更清晰的语义 =====
# class Stack:
#     def __init__(self):
#         self.items = []              # 内部用一个列表存数据
#
#     def push(self, item):            # 压栈（O(1)）
#         self.items.append(item)
#
#     def pop(self):                   # 弹栈（O(1)）
#         if self.is_empty():          # 空栈保护
#             return None
#         return self.items.pop()
#
#     def peek(self):                  # 看栈顶（O(1)）
#         if self.is_empty():
#             return None
#         return self.items[-1]
#
#     def is_empty(self):              # 判断是否为空
#         return len(self.items) == 0
#
# # 测试
# s = Stack()
# print(s.is_empty())
# s.push("页面1")
# s.push("页面2")
# s.push("页面3")
# print(s.is_empty())
# print(s.peek())      # 页面3
# print(s.pop())       # 页面3（后进先出！）
# print(s.pop())       # 页面2
# print(s.pop())       # 页面1
# print(s.pop())       # None（空了，安全返回）
from requests.utils import is_valid_cidr


'''回答'''
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def is_valid(self, item):
#         stack = []
#         mapping = {")": "(",
#                    "]": "[",
#                    "}": "{"
#         }
#
#         for i in item:
#             if i in "([{":
#                 stack.append(i)
#
#             else:
#                 if not stack:
#                     return False
#                 top = stack.pop()
#
#                 if mapping[i] != top:
#                     return False
#
#         return len(stack) == 0
#
#
# s = Stack()
# print(s.is_valid("()[]{}"))
# print(s.is_valid("([)]"))
# print(s.is_valid("{[]}"))
# print(s.is_valid("([])[]"))




'''优化'''


class Stack:
    def __init__(self):
        self.items = []


def is_valid(s):  # 独立函数，不依赖任何类
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if mapping[char] != top:
                return False

    return len(stack) == 0


# ===== 测试 =====
print(is_valid("()[]{}"))  # True
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True
print(is_valid("([])[]"))  # True
print(is_valid("("))  # False
print(is_valid(")"))  # False
print(is_valid(""))  # True
