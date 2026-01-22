def validateBST(root):
    if root is None:
        return True
    stack = [(root, float('-inf'), float('inf'))]

    while stack:
        node, low, high = stack.pop()
        if not (low < node.val < high):
            return False
        if node.right:
            stack.append((node.right, node.val, high))
        if node.left:
            stack.append((node.left, low, node.val))

    return True
