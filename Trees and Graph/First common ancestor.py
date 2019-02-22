#https://www.youtube.com/watch?v=13m9ZCB8gjw
# for binary tree

class tree:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class solution:

    def ancestor(self, root, n1, n2):

        if root ==None:
            return None
        if n1==root or n2==root:
                return root

        lf=self.ancestor(root.left, n1, n2)
        lr=self.ancestor(root.right, n1, n2)

        if lr and lf:
            return root
        if lr and not lf:
            return lr
        if lf and not lr:
            return lf

root = tree(6)
root.left = tree(7)
root.right = tree(8)
root.left.left = tree(3)
root.left.right = tree(5)
root.right.left = tree(4)
root.right.right = tree(9)


obj=solution()
res= obj.ancestor(root, root.left, root.right.right)

print ("ancestor is:", res.val)
