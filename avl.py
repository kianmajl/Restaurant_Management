class Person(object):
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.height = 1


class AVLTree(object):

    @staticmethod
    def get_height(root):
        if not root:
            return 0
        return root.height

    @staticmethod
    def get_balance(root):
        if not root:
            return 0
        return AVLTree.get_height(root.left) - AVLTree.get_height(root.right)

    @staticmethod
    def left_rotate(z):
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        z.height = 1 + max(AVLTree.get_height(z.left), AVLTree.get_height(z.right))
        y.height = 1 + max(AVLTree.get_height(y.left), AVLTree.get_height(y.right))
        return y

    @staticmethod
    def right_rotate(z):
        y = z.left
        t3 = y.right
        y.right = z
        z.left = t3
        z.height = 1 + max(AVLTree.get_height(z.left), AVLTree.get_height(z.right))
        y.height = 1 + max(AVLTree.get_height(y.left), AVLTree.get_height(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return Person(key)

        elif key < root.key:
            root.left = self.insert(root.left, key)

        else:
            root.right = self.insert(root.right, key)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            if key >= root.left.key:
                root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance_factor < -1:
            if key <= root.right.key:
                root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root


if __name__ == "__main__":
    customers, root_tree = AVLTree(), None

    root_tree = customers.insert(root_tree, 18)
    root_tree = customers.insert(root_tree, 24)
    root_tree = customers.insert(root_tree, 1)
    root_tree = customers.insert(root_tree, 20)

    orders = input("Please Enter Your Order: ")
