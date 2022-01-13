class Person(object):
    def __init__(self, key, name=""):
        self.key = key
        self.name = name
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

    def insert(self, root, key, name):
        if not root:
            return Person(key, name)

        elif key < root.key:
            root.left = self.insert(root.left, key, name)

        else:
            root.right = self.insert(root.right, key, name)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            if key >= root.left.key:
                root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance_factor < -1:
            if key <= root.right.key:
                root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    @staticmethod
    def search(root, key):
        if not root:
            return "Not Found!"

        if root.key == key:
            return root.name

        elif key < root.key:
            return AVLTree.search(root.left, key)

        else:
            return AVLTree.search(root.right, key)


if __name__ == "__main__":
    customers, root_tree, customers_num = AVLTree(), None, dict()

    while True:
        orders = input("Please Enter Your Order: ").split()

        if orders[0] == "Insert":
            customers_num[orders[1]] = int(orders[2])
            # noinspection PyTypeChecker
            root_tree = customers.insert(root_tree, int(orders[2]), orders[1])

        elif orders[0] == "Search":
            # noinspection PyTypeChecker
            print(customers.search(root_tree, int(orders[1])))
