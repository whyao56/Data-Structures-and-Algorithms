# class SimpleHashTable:
#     def __init__(self, size=10):
#         self.size = size
#         self.table = [[] for _ in range(size)]   # 每个位置放一个列表（解决碰撞）
#
#     def _hash(self, key):
#         return sum(ord(char) for char in str(key)) % self.size  # 把字符转ASCII求和再取模
#
#     def put(self, key, value):
#         index = self._hash(key)
#         # 检查该位置是否已有这个 key，有则更新
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 pair[1] = value
#                 return
#         self.table[index].append([key, value])    # 没找到就追加
#
#     def get(self, key):
#         index = self._hash(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 return pair[1]
#         return None   # 没找到


class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find(self):
        seen = {}

        for index, x in enumerate(self.nums):
            need = self.target - x

            if need in seen:
                return [seen[need], index]
            seen[x] = index

        return None


s = TwoSum([2, 7, 11, 15], 9)
print(s.find())

s2 = TwoSum([3, 2, 4], 6)
print(s2.find())

s3 = TwoSum([3, 2, 5], 6)
print(s3.find())