class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# ===== 测试代码 =====
ll = LinkedList()
ll.add_first(30)
ll.add_first(20)
ll.add_first(10)
ll.print_all()