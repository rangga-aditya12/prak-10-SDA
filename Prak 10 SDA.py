class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None
        self.parent = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, node, key):
        if node is None:
            print(f"== Menambahkan node {key}")
            return AVLNode(key), ""

        direction = ""
        if key < node.key:
            node.left, direction = self.insert(node.left, key)
            node.left.parent = node
        else:
            node.right, direction = self.insert(node.right, key)
            node.right.parent = node

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.balance(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            print(f"== R----{node.key}")
            print(f"==          L----{node.left.key}")
            print(f"==          I         L----{node.left.left.key}")
            return self.rotate_right(node), "right"

        # Right Right Case
        if balance < -1 and key > node.right.key:
            print(f"== R----{node.key}")
            print(f"==          R----{node.right.key}")
            return self.rotate_left(node), "left"

        # Left Right Case
        if balance > 1 and key > node.left.key:
            print(f"== R----{node.key}")
            print(f"==          L----{node.left.key}")
            print(f"==                    R----{node.left.right.key}")
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node), "right"

        # Right Left Case
        if balance < -1 and key < node.right.key:
            print(f"== R----{node.key}")
            print(f"==          R----{node.right.key}")
            print(f"==                    L----{node.right.left.key}")
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node), "left"

        return node, direction

    def insert_key(self, key):
        self.root, _ = self.insert(self.root, key)

    def post_order_traversal(self, node):
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.key, end=" ")

    def pre_order_traversal(self, node):
        if node:
            print(node.key, end=",")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def search_key(self, key):
        return self.search(self.root, key)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
        else:
            print("Inorder traversal of AVL tree:")
            self.inorder_traversal(self.root)

if __name__ == '__main__':
    avl_tree = AVLTree()

    # Insert nodes into the AVL tree
    numbers = [26, 5, 22, 4, 20, 64]
    for num in numbers:
        avl_tree.insert_key(num)

    # Print post-order traversal
    print("postOrder")
    avl_tree.post_order_traversal(avl_tree.root)
    print("\npreOrder:")
    avl_tree.pre_order_traversal(avl_tree.root)

    # Search for a specific number
    search_key = int(input("Masukan angka: "))
    result = avl_tree.search_key(search_key)
    if result:
        print(f"\ncari angka? :{search_key}\n{search_key} ditemukan.")
    else:
        print(f"\ncari angka? :{search_key}\n{search_key} tidak ditemukan.")
