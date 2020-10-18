# Python3 program for above approach
class newNode:
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

# Iterative method to do level order traversal
# line by line
def printLevelOrder(root):

	# Base case
	if root is None:
		return
	# Create an empty queue for level order traversal
	q = []

	# Enqueue root and initialize height
	q.append(root)
	while q:
			count = len(q)
			while count:
				temp = q.pop(0)
				print(temp.val, end = ' ')
				if temp.left:
					q.append(temp.left)
				if temp.right:
					q.append(temp.right)
				count = count -1
			print()

# Driver Code
root = newNode(1);
root.left = newNode(2);
root.right = newNode(3);
root.left.left = newNode(4);
root.left.right = newNode(5);
root.right.right = newNode(6);

printLevelOrder(root);

# This code is contributed by Praveen kumar
