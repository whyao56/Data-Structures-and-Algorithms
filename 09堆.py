# import heapq
#
# # ===== 创建一个空堆 =====
# heap = []
#
# # ===== 插入元素（O(log n)）=====
# heapq.heappush(heap, 3)   # 插入 3
# heapq.heappush(heap, 1)   # 插入 1，会自动上浮
# heapq.heappush(heap, 2)
# print(heap)               # [1, 3, 2]（堆的内部数组，根最小）
#
# # ===== 查看堆顶最小元素（O(1)）=====
# print(heap[0])            # 1
#
# # ===== 弹出堆顶最小元素（O(log n)）=====
# smallest = heapq.heappop(heap)
# print(smallest)           # 1
# print(heap[0])            # 2（新的堆顶，自动调整）
#
# # ===== 如果要用最大堆，可以把值取负 =====
# max_heap = []
# heapq.heappush(max_heap, -3)   # 用负数存放
# heapq.heappush(max_heap, -1)
# heapq.heappush(max_heap, -2)
# largest = -heapq.heappop(max_heap)  # 弹出时再取负，得到最大值 3
# print(largest)            # 3


import heapq

def max_heappush(stones):
    max_heap = []
    for value in stones:
        heapq.heappush(max_heap, -value)

    while len(max_heap) > 1:
        a = -heapq.heappop(max_heap)
        b = -heapq.heappop(max_heap)
        if a != b:
            heapq.heappush(max_heap, -(a - b))

    if len(max_heap) == 0:
        return 0
    return -max_heap[0]

print(max_heappush([2,7,4,1,8,1]))


