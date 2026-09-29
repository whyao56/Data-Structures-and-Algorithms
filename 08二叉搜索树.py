# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None                # 整棵树的根节点
#
#     # ===== 插入值（平均 O(log n)，最坏 O(n)）=====
#     def insert(self, value):
#         if self.root is None:
#             self.root = BSTNode(value)  # 空树，直接当根
#             return
#
#         cur = self.root
#         while True:
#             if value < cur.value:       # 比当前节点小，往左走
#                 if cur.left is None:    # 左边空，直接放这里
#                     cur.left = BSTNode(value)
#                     return
#                 cur = cur.left          # 左边不空，继续往下走
#             else:                       # 比当前节点大或等于，往右走
#                 if cur.right is None:
#                     cur.right = BSTNode(value)
#                     return
#                 cur = cur.right
#
#     # ===== 查找值（平均 O(log n)，最坏 O(n)）=====
#     def search(self, value):
#         cur = self.root
#         while cur is not None:
#             if value == cur.value:
#                 return True             # 找到了
#             elif value < cur.value:
#                 cur = cur.left          # 目标更小，去左子树
#             else:
#                 cur = cur.right         # 目标更大，去右子树
#         return False                    # 走到空节点都没找到
#
#     # ===== 中序遍历：左-根-右，正好从小到大输出（O(n)）=====
#     def inorder(self, node):
#         if node is None:
#             return
#         self.inorder(node.left)
#         print(node.value, end=" ")
#         self.inorder(node.right)
#
# # 测试
# bst = BinarySearchTree()
# for v in [5, 3, 8, 1, 4, 7, 9]:
#     bst.insert(v)
#
# print(bst.search(4))    # True
# print(bst.search(6))    # False
#
# bst.inorder(bst.root)   # 输出：1 3 4 5 7 8 9




class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeNode:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return

        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = BSTNode(value)
                    return

                cur = cur.left

            else:
                if cur.right is None:
                    cur.right = BSTNode(value)
                    return

                cur = cur.right

    def Binary_search(self, value):

        cur = self.root
        if cur is None:
            return False

        while cur is not None:
            if value == cur.value:
                return cur

            elif value < cur.value:
                cur = cur.left

            else:
                cur = cur.right

        return None



bst = TreeNode()
for v in [4, 2, 7, 1, 3]:
    bst.insert(v)

node = bst.Binary_search(2)

print(node.value)
print(node.left.value)
print(node.right.value)


'''优化'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return

        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = TreeNode(value)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = TreeNode(value)
                    return
                cur = cur.right

    def search_subtree(self, value):
        cur = self.root

        while cur is not None:
            if value == cur.value:
                return cur
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        return None  # 统一返回 None 表示找不到


# ===== 测试 =====
bst = BinarySearchTree()
for v in [4, 2, 7, 1, 3]:
    bst.insert(v)

node = bst.search_subtree(2)
if node:
    print(node.value)        # 2
    print(node.left.value)   # 1
    print(node.right.value)  # 3
else:
    print("没找到")


