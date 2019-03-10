class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def inOrderSuccessor(root, n):
    # Step 1 of the above algorithm
    if n.right is not None:
        return minValue(n.right)

        # Step 2 of the above algorithm
    p = n.parent
    while (p is not None):
        if n != p.right:
            break
        n = p
        p = p.parent
    return p



def minValue(node):
    current = node

    # loop down to find the leftmost leaf
    while (current is not None):
        if current.left is None:
            break
        current = current.left

    return current

def insert(node, data):
    # 1) If tree is empty then return a new singly node
    if node is None:
        return Node(data)
    else:

        # 2) Otherwise, recur down the tree
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node

            # return  the unchanged node pointer
        return node


root = None

# Creating the tree given in the above diagram
root = insert(root, 20)
root = insert(root, 8);
root = insert(root, 22);
root = insert(root, 4);
root = insert(root, 12);
root = insert(root, 10);
root = insert(root, 14);
temp = root.left.right.right

succ = inOrderSuccessor(root, temp)
if succ is not None:
    print ("\nInorder Successor of %d is %d ", (temp.data, succ.data))
else:
    print ("\nInorder Successor doesn't exist")