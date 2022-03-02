"""
leetcode上面第100题有对树的解法总结：记得学习下

"""
# class Solution:
#     def isSameTree(self, p, q):
#         if p is None or q is None:
#             return p == q
#         if p.val == q.val:
#             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#         else:
#             return False

def is_same(root1, root2):
    if root1.val == root2.val:
        return is_same(root1.left, root2.left) and is_same(root1.right, root2.right)
    else:
        return False