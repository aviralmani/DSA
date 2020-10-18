class newNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def inOrder(root):
    if root:
        print(root.data)
        inOrder(root.left)
        inOrder(root.right)

def preOrder(root):
    if root:
        preOrder(root.left)
        print(root.data)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.right = newNode(6)
root.right.right.left = newNode(7)

print("IN ORDER: ")
inOrder(root)
print("PRE ORDER: ")
preOrder(root)
print("POST ORDER: ")
postOrder(root)
