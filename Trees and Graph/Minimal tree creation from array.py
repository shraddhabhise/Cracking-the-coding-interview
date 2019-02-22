#Time Complexity: O(n)
#Given a sorted (increasing order) array with unique integer elements, write an algo- rithm to create a binary search tree with minimal height.
class tree:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class solution:
    def preOrder(self, node):
        if not node:
            return

        print( node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        mid = len(nums)//2
        root = tree(nums[mid])
        if len(nums)>1:
            root.left = self.sortedArrayToBST(nums[0:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

arr = [1, 2, 3, 4, 5, 6, 7]
obj = solution()
root = obj.sortedArrayToBST(arr)
obj.preOrder(root)