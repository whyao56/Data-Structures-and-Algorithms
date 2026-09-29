# def remove_duplicates(nums):
#     if not nums:
#         return 0
#     slow = 0                     # 慢指针记录“下一个合法元素该放哪”
#     for fast in range(1, len(nums)):
#         if nums[fast] != nums[slow]:
#             slow += 1
#         nums[slow] = nums[fast]
#     return slow + 1              # 去重后新长度
#
# print(remove_duplicates([1, 1, 2, 2, 3]))   # 3，数组前三个是 [1,2,3]

def valid_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

print(valid_palindrome("A man, a plan, a canal: Panama"))
