# def build_prefix_sum(arr):
#     pre = [0] * (len(arr) + 1)   # 多一位，pre[i] = arr[0] 到 arr[i-1] 的和
#     for i in range(len(arr)):
#         pre[i + 1] = pre[i] + arr[i]
#     return pre
#
# def range_sum(pre, left, right):
#     # 返回 arr[left..right] 的和（下标从0开始）
#     return pre[right + 1] - pre[left]
#
# # 测试
# arr = [3, 2, -1, 6, 5, 4]
# pre = build_prefix_sum(arr)
# print(pre)  # [0, 3, 5, 4, 10, 15, 19]
# print(range_sum(pre, 1, 3))  # arr[1..3] = 2 + (-1) + 6 = 7



class NumArray():
    def __init__(self, nums):
        self.pre = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.pre[i + 1] = self.pre[i] + nums[i]

    def sumRange(self, left, right):
        return self.pre[right + 1] - self.pre[left]

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
obj.sumRange(0, 2)  # 返回 1（-2+0+3）
obj.sumRange(2, 5)  # 返回 -1（3-5+2-1）
obj.sumRange(0, 5)  # 返回 -3