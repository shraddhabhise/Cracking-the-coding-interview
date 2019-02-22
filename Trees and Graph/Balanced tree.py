#complexity: O(n^2)
#a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
#https://www.cs.cornell.edu/courses/cs3110/2012sp/lectures/lec20-master/lec20.html for complexity
class tree:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def height(root):
        if root==None:
            return 0
        return max(height(root.left), height(root.right))+1

def isBalanced(root):
        if root==None:
            return True
        lh = height(root.left)
        lr = height(root.right)

        if abs(lh-lr)<=1 and isBalanced(root.left) and isBalanced(root.right):
            return True
        return False

root = tree(1)
root.left = tree(2)
root.right = tree(3)
root.left.left = tree(4)
root.left.right = tree(5)
root.left.left.left = tree(8)

if isBalanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")