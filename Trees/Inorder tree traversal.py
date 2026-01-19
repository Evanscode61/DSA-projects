class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def inorder(self):
        if self is None:
            return

        if self.left:
            self.left.inorder()

        print(self.data, end=" ")

        if self.right:
            self.right.inorder()


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

root.inorder()




