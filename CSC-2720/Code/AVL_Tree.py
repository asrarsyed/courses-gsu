class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance_factor(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, N):
        L = N.left
        LR = L.right

        L.right = N
        N.left = LR

        N.height = 1 + max(self.get_height(N.left), self.get_height(N.right))
        L.height = 1 + max(self.get_height(L.left), self.get_height(L.right))

        return L

    def rotate_left(self, N):
        R = N.right
        RL = R.left

        R.left = N
        N.right = RL

        N.height = 1 + max(self.get_height(N.left), self.get_height(N.right))
        R.height = 1 + max(self.get_height(R.left), self.get_height(R.right))

        return R

    def insert(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance_factor(node)

        # Left Heavy
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        # Right Heavy
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        # Left Right Heavy
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left Heavy
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def in_order_traversal(self, node):
        if not node:
            return []
        return self.in_order_traversal(node.left) + [node.value] + self.in_order_traversal(node.right)


avl = AVLTree()
root = None

for key in [10, 20, 30, 40, 50, 25]:
    root = avl.insert(root, key)

print("In-order Traversal:", avl.in_order_traversal(root))
