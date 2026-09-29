# def count_target(arr, target):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] == target:
#             count += 1
#             return count

'''代码修正'''
def count_target(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
    return count

print(count_target([], 1))

'''代码优化'''
def count_target(arr, target):
    count = 0
    for num in arr:        # 直接拿到每个元素，不用 range(len(...))
        if num == target:
            count += 1
    return count