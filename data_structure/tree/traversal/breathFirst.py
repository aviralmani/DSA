class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def breathFirst(root):
    height =  Height(root)
    for level in range(1, height):
        search(root, level)


def search(root, level):
    if not root:
        return
    elif level == 1:
        print(root.data)

    else:
        search(root.left, level -1)
        search(root.right, level -1)

def Height(root):
    if not root:
        return 0

    left_height = Height(root.left)
    right_height = Height(root.right)

    if left_height > right_height:
        left_height = left_height + 1
        return left_height
    else:
        right_height = right_height + 1
        return right_height



root = newNode(1);
root.left = newNode(2);
root.right = newNode(3);
root.left.left = newNode(4);
root.left.right = newNode(5);
root.right.right = newNode(6);
root.right.right.left = newNode(7);
height = Height(root)
print(height)
breathFirst(root)
