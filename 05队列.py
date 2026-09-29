# from collections import deque
#
# # ===== 直接用 deque 当队列 =====
# q = deque()
# q.append("顾客1")      # 入队：排到队尾（O(1)）
# q.append("顾客2")
# q.append("顾客3")
# print(q)              # deque(['顾客1', '顾客2', '顾客3'])
#
# first = q.popleft()   # 出队：队头离开（O(1)）
# print(first)          # 顾客1（先进先出！）
# print(q)              # deque(['顾客2', '顾客3'])
# print(q[0])           # 看队头：顾客2
#
# # ===== 包一个 Queue 类，更清晰 =====
# class Queue:
#     def __init__(self):
#         self.items = deque()
#
#     def enqueue(self, item):         # 入队 O(1)
#         self.items.append(item)
#
#     def dequeue(self):               # 出队 O(1)
#         if self.is_empty():
#             return None
#         return self.items.popleft()
#
#     def peek(self):                  # 看队头 O(1)
#         if self.is_empty():
#             return None
#         return self.items[0]
#
#     def is_empty(self):
#         return len(self.items) == 0



# from collections import deque
#
# class Queue:
#     def __init__(self):
#         self.queue = deque()
#
#     def ping(self, item):
#         self.queue.append(item)
#
#         while self.queue[0] < item - 3000:
#             self.queue.popleft()
#             print(self.queue)
#
#         return len(self.queue)
#
#
# counter = Queue()
# print(counter.ping(1))
# print(counter.ping(100))
# print(counter.ping(3001))
# print(counter.ping(3002))
# print(counter.ping(4000))



'''优化'''
from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = deque()  # 用队列存储所有 ping 的时间戳

    def ping(self, t):
        # 1. 当前 ping 入队
        self.queue.append(t)

        # 2. 淘汰超过 3000ms 的旧 ping
        while self.queue[0] < t - 3000:
            self.queue.popleft()

        # 3. 返回过去 3000ms 内的 ping 次数
        return len(self.queue)


# ===== 测试代码 =====
if __name__ == "__main__":
    counter = RecentCounter()

    print(counter.ping(1))  # 1
    print(counter.ping(100))  # 2
    print(counter.ping(3001))  # 3
    print(counter.ping(3002))  # 3（100 还在窗口内）
    print(counter.ping(4000))  # 3（3001, 3002, 4000）