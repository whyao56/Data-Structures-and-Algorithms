# # ===== 1. 定义二叉树节点类 =====
# class TreeNode:
#     def __init__(self, value):
#         self.value = value      # 节点存放的数据
#         self.left = None        # 左子节点（初始为空）
#         self.right = None       # 右子节点（初始为空）
#
# # ===== 2. 手动创建一棵小树 =====
# root = TreeNode("产品部")
# root.left = TreeNode("研发组")
# root.right = TreeNode("设计组")
# root.left.left = TreeNode("小明")   # 研发组下面有两个员工
# root.left.right = TreeNode("小红")
# root.right.left = TreeNode("小刚")   # 设计组下面有一个员工
#
# # 树结构：
# #        产品部
# #       /     \
# #   研发组   设计组
# #    /  \     /
# # 小明 小红 小刚
#
# # ===== 3. 先序遍历：根 -> 左 -> 右 =====
# def preorder(node):
#     if node is None:            # 遇到空节点，直接返回（递归终止条件）
#         return
#     print(node.value)           # 先访问当前节点
#     preorder(node.left)         # 再递归遍历左子树
#     preorder(node.right)        # 最后递归遍历右子树
#
# preorder(root)
# # 输出：
# # 产品部
# # 研发组
# # 小明
# # 小红
# # 设计组
# # 小刚


# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# def preorder(root):
#     result = []
#
#     def dfs(node):
#         if node is None:
#             return
#
#         result.append(node.value)
#         preorder(node.left)
#         preorder(node.right)
#
#     preorder(root)
#     return result



'''修正'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    result = []

    def dfs(node):
        if node is None:
            return

        result.append(node.value)
        dfs(node.left)   # 调用 dfs（自己递归）
        dfs(node.right)  # 调用 dfs（自己递归）

    dfs(root)            # 调用 dfs，从根节点开始
    return result


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
# 注意：root.left 是 None（不需要写）

print(preorder(root))


'''优化'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    result = []

    def dfs(node):
        if node:  # 等价于 if node is not None
            result.append(node.value)
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return result
