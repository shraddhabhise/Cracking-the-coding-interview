# bfs traversal
# time complexity: O(n)
# space complexity : O(n)
# no visited here:  https://www.youtube.com/watch?v=9PHkM0Jri_4

class tree:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class Solution:

    def level(self, root):
        queue=[]
        res=[]
        queue.append(root)

        while queue:
            s = queue.pop(0)
            print (s.val)
            res.append(s.val)
            if s.left:
                queue.append(s.left)
            if s.right:
                queue.append(s.right)

        return list(res)

obj= Solution()
root = tree(1)
root.left = tree(2)
root.right = tree(3)
root.left.left = tree(4)
root.left.right = tree(5)
root.left.left.left = tree(8)

res=obj.level(root)
print("res", res)