# # ===== 1. 阶乘：n! = n × (n-1)! =====
# def factorial(n):
#     if n == 1:          # 终止条件：1! = 1
#         return 1
#     return n * factorial(n - 1)   # 自己调用自己，问题缩小
#
# print(factorial(5))     # 5 × 4 × 3 × 2 × 1 = 120
#
# # ===== 2. 斐波那契数：F(n) = F(n-1) + F(n-2) =====
# def fib(n):
#     if n <= 1:          # 终止条件：F(0)=0, F(1)=1
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(6))           # 0 1 1 2 3 5 8 → 第6个是 8







# def fib(n):
#     memo = {}
#
#     def dfs(n):
#         if n in memo:
#             return memo[n]
#
#         if n <= 1:
#             return n
#
#         result = dfs(n - 1) + dfs(n - 2)
#         memo[n] = result
#         return result
#
#     return dfs(n)
#
# print(fib(10))




'''优化'''

def fib(n):
    memo = {}

    def dfs(n):
        if n <= 1:  # 终止条件：必须先判断
            return n

        if n in memo:  # 再查缓存
            return memo[n]

        result = dfs(n - 1) + dfs(n - 2)
        memo[n] = result
        return result

    return dfs(n)

print(fib(10))



'''再优化'''


def fib(n):
    # 1. 处理非法输入（工程健壮性）
    if n < 0:
        raise ValueError("n 不能为负数")

    # 2. 预存基础情况
    memo = {0: 0, 1: 1}

    def dfs(n):
        # 命中缓存 → O(1) 直接返回
        if n in memo:
            return memo[n]

        # 计算并缓存
        memo[n] = dfs(n - 1) + dfs(n - 2)
        return memo[n]

    return dfs(n)


# ===== 测试 =====
print(fib(10))  # 55
print(fib(0))  # 0
print(fib(1))  # 1

# print(fib(-5))  # 会抛出 ValueError
