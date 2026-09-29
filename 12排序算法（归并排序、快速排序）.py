# def merge_sort(arr):
#     # 终止条件：只剩一个元素或空列表，天然有序
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])    # 递归排序左半
#     right = merge_sort(arr[mid:])   # 递归排序右半
#
#     # 合并两个有序列表
#     merged = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
#
#     # 把剩余部分接上
#     merged.extend(left[i:])
#     merged.extend(right[j:])
#     return merged
#
# print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# # 输出：[3, 9, 10, 27, 38, 43, 82]



# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr) // 2]   # 选中间元素当基准
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#
#     return quick_sort(left) + middle + quick_sort(right)
#
# print(quick_sort([38, 27, 43, 3, 9, 82, 10]))
# # 输出：[3, 9, 10, 27, 38, 43, 82]



def sort_array(nums):
    return sorted(nums)

print(sort_array([5, 2, 3, 1]))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

print(merge_sort([5, 2, 3, 1]))



def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([5, 2, 3, 1]))