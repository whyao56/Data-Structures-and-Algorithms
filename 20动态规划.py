# def climb_stairs(n):
#     if n <= 2:
#         return n
#
#     dp = [0] * (n + 1)   # dp[i] = 爬到第 i 级的方法数
#     dp[1] = 1            # 爬到第 1 级：1 种
#     dp[2] = 2            # 爬到第 2 级：1+1 或 2
#
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]   # 状态转移方程
#
#     return dp[n]
#
# print(climb_stairs(5))   # 8




def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[n - 1]

print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))