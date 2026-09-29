def contains_duplicate(s):
    seen = set()

    for i in range(len(s)):
        if s[i] in seen:
            return True

        seen.add(s[i])

    return False

print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1, 1, 1, 1]))
print(contains_duplicate([]))


'''优化'''
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False