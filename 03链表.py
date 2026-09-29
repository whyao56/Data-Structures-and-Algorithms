# # ===== 1. 定义节点类：一个"线索纸条" =====
# class Node:
#     def __init__(self, value):
#         self.value = value   # 这张纸条上写的数据
#         self.next = None     # 这张纸条指向的"下一张纸条"（初始为None，表示没有下一张）
#
# # ===== 2. 定义链表类：管理一叠纸条 =====
# class LinkedList:
#     def __init__(self):
#         self.head = None     # 链表头：我们手上拿的第一张纸条
#
#     # ===== 3. 在头部插入新节点（O(1)）=====
#     def add_first(self, value):
#         new_node = Node(value)      # 造一张新纸条
#         new_node.next = self.head   # 新纸条指向原来的第一张
#         self.head = new_node        # 新纸条成为新的第一张
#
#     # ===== 4. 打印全部节点（O(n)）=====
#     def print_all(self):
#         current = self.head         # 从第一张开始
#         while current is not None:  # 只要还有纸条
#             print(current.value, end=" -> ")
#             current = current.next  # 顺着线索走到下一张
#         print("None")               # 走到头了
#
#     # ===== 5. 查找值（O(n)）=====
#     def find(self, value):
#         current = self.head
#         index = 0
#         while current is not None:
#             if current.value == value:
#                 return index        # 找到了，返回位置
#             current = current.next
#             index += 1
#         return -1                   # 走完全程没找到
#
# # ===== 测试 =====
# ll = LinkedList()
# ll.add_first(30)    # [30]
# ll.add_first(20)    # [20] -> [30]
# ll.add_first(10)    # [10] -> [20] -> [30]
# ll.print_all()      # 输出: 10 -> 20 -> 30 -> None
# print(ll.find(20))  # 输出: 1
# print(ll.find(99))  # 输出: -1



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self,data):  # 头部插入（队首插入）
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next
        print("None")

    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev


llist = LinkedList()
llist.add_first(1)
llist.add_first(2)
llist.add_first(3)
llist.printList()
llist.reverse()
llist.printList()


empty = LinkedList()
empty.reverse()          # 空链表反转会报错吗？

single = LinkedList()
single.add_first(5)         # 单节点链表
single.reverse()         # 会怎样？
single.printList()       # 输出应该是什么？

