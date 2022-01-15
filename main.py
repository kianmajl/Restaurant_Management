import avl
import customer
import kitchen

if __name__ == "__main__":

    while True:

        print("\n1. Usual mood reservation")
        print("\n2. Party mood reservation")

        try:
            selection = int(input("\n Please enter a number: "))

            if selection == 1:
                kitchen.main()

            elif selection == 2:
                kitchen.main()

        except ValueError:
            input("\nOops!  That was no valid number.  Try again...")
