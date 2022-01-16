import os


class Person(object):
    def __init__(self, key, name=""):
        self.key = key
        self.name = name
        self.right = None
        self.left = None
        self.height = 1


class AVLTree(object):

    def __init__(self):
        self.size = 0

    @staticmethod
    def get_height(root):
        if not root:
            return 0
        return root.height

    # difference between the height of the left subtree and that of the right subtree of that node
    @staticmethod
    def get_balance(root):
        if not root:
            return 0
        return AVLTree.get_height(root.left) - AVLTree.get_height(root.right)

    # the arrangements are first shifted to the left and then to the right.
    @staticmethod
    def left_rotate(z):
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        z.height = 1 + max(AVLTree.get_height(z.left), AVLTree.get_height(z.right))
        y.height = 1 + max(AVLTree.get_height(y.left), AVLTree.get_height(y.right))
        return y

    # the arrangements are first shifted to the right and then to the left.
    @staticmethod
    def right_rotate(z):
        y = z.left
        t3 = y.right
        y.right = z
        z.left = t3
        z.height = 1 + max(AVLTree.get_height(z.left), AVLTree.get_height(z.right))
        y.height = 1 + max(AVLTree.get_height(y.left), AVLTree.get_height(y.right))
        return y

    # do a binary search in tree
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

    @staticmethod
    def get_min_value_node(root):
        if root is None or root.left is None:
            return root
        return AVLTree.get_min_value_node(root.left)

    @staticmethod
    def print(root, space, count):

        if not root:
            return

        space += count[0]

        AVLTree.print(root.right, space, count)

        print()
        for i in range(count[0], space):
            print(end=" ")
        print(root.name)

        AVLTree.print(root.left, space, count)

    @staticmethod
    def print_2d(root, count):
        AVLTree.print(root, 0, count)

    def insert(self, root, key, name):
        if not root:
            return Person(key, name)

        elif key < root.key:
            root.left = self.insert(root.left, key, name)

        else:
            root.right = self.insert(root.right, key, name)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # balance the tree
        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            if key >= root.left.key:
                root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance_factor < -1:
            if key <= root.right.key:
                root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        self.size += 1

        return root

    def delete_node(self, root, key):
        if not root:
            return root

        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        # update the balance factor of nodes
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance_factor = self.get_balance(root)

        # balance the tree
        if balance_factor > 1:
            if self.get_balance(root.left) < 0:
                root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance_factor < -1:
            if self.get_balance(root.right) > 0:
                root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        self.size -= 1

        return root


def main():
    customers, root_tree, customers_num = AVLTree(), None, dict()
    os.system("cls")

    print("\n-------------------- Welcome to Kharkhon Bashi Restaurant | Party-Order ---------------------\n")
    while True:

        try:
            orders = input("\nPlease Enter Your Order: ").split()

            if orders[0] == "Insert":
                customers_num[orders[1]] = int(orders[2])
                root_tree = customers.insert(root_tree, int(orders[2]), orders[1])
                print("\nSuccessfully added!")

            elif orders[0] == "Search":
                try:
                    print(customers.search(root_tree, int(orders[1])))

                except ValueError:
                    print("Please enter a number after \"Search\"")

            elif orders[0] == "Delete":
                # noinspection PyTypeChecker
                root_tree = customers.delete_node(root_tree, customers_num[orders[1]])
                print("Successfully deleted!")

            elif orders[0] == "Print":
                customers.print_2d(root_tree, [customers.size])

            elif orders[0] == "Back" or orders[0] == "Exit":
                break

        except IndexError:
            print("Enter a valid order")


if __name__ == "__main__":
    main()
