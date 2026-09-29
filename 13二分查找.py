# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid             # 找到了
#         elif arr[mid] < target:
#             left = mid + 1         # 目标在右边
#         else:
#             right = mid - 1        # 目标在左边
#     return -1                      # 没找到
#
# # 测试
# nums = [1, 3, 5, 7, 9, 11, 13]
# print(binary_search(nums, 7))   # 3
# print(binary_search(nums, 8))   # -1


def binary_search(arr, target):
    def dfs(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return dfs(left, mid - 1)
        else:
            return dfs(mid + 1, right)

    return dfs(0, len(arr) - 1)

nums = [-1, 0, 3, 5, 9, 12]
print(binary_search(nums, 9))
print(binary_search(nums, 2))