# Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an algorithm to determine if T2 is a subtree of Tl.
# O(n)
class tree:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class opeartions:
    def isEqual(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False

        return self.isEqual(s.left, t.left) and self.isEqual(s.right, t.right)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False

        if self.isEqual(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

root1 = tree(1)
root1.left = tree(4)
root1.right = tree(None)
root1.left.left = tree(2)
root1.left.right = tree(3)

root2 = tree(4)
root2.left = tree(2)
root2.right = tree(3)

obj=opeartions()

if obj.isSubtree(root1, root2):
    print("Tree is subtree")
else:
    print("Tree is not subtree")