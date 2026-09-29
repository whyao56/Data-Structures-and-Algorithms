# def min_subarray_len(target, nums):
#     left = 0
#     total = 0
#     min_len = float('inf')   # 初始无限大
#
#     for right in range(len(nums)):
#         total += nums[right]  # 右指针扩大窗口
#
#         while total >= target:  # 条件满足时，尝试缩小窗口
#             min_len = min(min_len, right - left + 1)
#             total -= nums[left]
#             left += 1           # 左指针收缩窗口
#
#     return 0 if min_len == float('inf') else min_len
#
# print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))  # 2（子数组 [4,3]）


def length_of_longest_substring(s):
    left = 0
    char_set = set()
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        max_len = max(max_len, right - left + 1)

    return max_len

print(length_of_longest_substring("abcabcbb"))