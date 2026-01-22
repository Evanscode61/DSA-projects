def delete_bst(root, key):
    if not root:
        return root

    if key < root.data:
        root.left = delete_bst(root.left, key)
    elif key > root.data:
        root.right = delete_bst(root.right, key)
    else:
        # Case 1 & 2
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Case 3
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete_bst(root.right, temp.data)

    return root

def find_min(node):
    while node.left:
          node = node.left
    return node
