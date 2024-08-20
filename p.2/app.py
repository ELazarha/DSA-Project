class Node:
    def __init__(self, value):
        # Initialize a node with a given value, left and right children as None, and height as 1
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        # Initialize an AVL tree with root as None
        self.root = None

    def insert(self, value):
        # Public method to insert a value into the AVL tree
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        # Helper method to insert a value into the subtree rooted with the given node
        if not node:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        # Update the height of the ancestor node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        # Get the balance factor to check whether this node became unbalanced
        balance = self._get_balance(node)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and value < node.left.value:
            return self._right_rotate(node)
        # Right Right Case
        if balance < -1 and value > node.right.value:
            return self._left_rotate(node)
        # Left Right Case
        if balance > 1 and value > node.left.value:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        # Right Left Case
        if balance < -1 and value < node.right.value:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def delete(self, value):
        # Public method to delete a value from the AVL tree
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        # Helper method to delete a value from the subtree rooted with the given node
        if not node:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)

        # Update the height of the current node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        # Get the balance factor to check whether this node became unbalanced
        balance = self._get_balance(node)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        # Perform a left rotation on the subtree rooted with z
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        # Perform a right rotation on the subtree rooted with z
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        # Get the height of the node
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        # Get the balance factor of the node
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _min_value_node(self, node):
        # Get the node with the smallest value in the subtree rooted with the given node
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _search(self, node, value):
        # Helper method to search a value in the subtree rooted with the given node
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def search(self, value):
        # Public method to search a value in the AVL tree
        return self._search(self.root, value)

    def display(self):
        # Public method to display the AVL tree
        lines, *_ = self._display(self.root)
        for line in lines:
            print(line)

    def _display(self, node, prefix="", is_left=True):
        # Helper method to display the subtree rooted with the given node
        if node is None:
            return [], 0, 0, 0
        line1 = []
        line2 = []
        if node.left is not None:
            left_lines, left_pos, left_width, left_height = self._display(node.left,
                                                                          prefix + ("│   " if is_left else "    "),
                                                                          True)
            line1.extend(left_lines)
            line2.extend(left_lines)
        line1.append(f"{prefix}{'└── ' if is_left else '┌── '}{node.value}")
        if node.right is not None:
            right_lines, right_pos, right_width, right_height = self._display(node.right,
                                                                              prefix + ("    " if is_left else "│   "),
                                                                              False)
            line1.extend(right_lines)
            line2.extend(right_lines)
        return line1, 0, 0, 0


if __name__ == "__main__":
    tree = AVLTree()

    values = [
             "NICC" , "CKCC" ,
             "STEM" , "BUILDING A", "BUILDING B" ,
             "BUILDING C" , "BUILDING D" , "BUILDING T",
             "STUDY OFFICE", "LIBRARY" , "NISSET COFFEE" ,

    ]
    for value in values:
        tree.insert(value)
    while True:
        print("\nMenu:")
        print("1. Insert a node")
        print("2. Search for a node")
        print("3. Delete a node")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Insert a node
            tree.insert(str(input("Enter the value to insert: ")))
        elif choice == "2":
            # Search for a node
            value = str(input("Enter the value to search: "))
            if tree.search(value):
                print("Node found")
            else:
                print("Node not found")
        elif choice == "3":
            # Delete a node
            value = str(input("Enter the value to delete: "))
            tree.delete(value)
        elif choice == "4":
            # Display the tree
            tree.display()
        elif choice == "5":
            # Exit the program
            print("Exiting...")
            break
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")
