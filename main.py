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
                kitchen.start()
                main_food_prep = dict(filter(lambda l: l[0] in kitchen.food_menu, kitchen.food_prep.items()))
                customer.start(main_food_prep)
                customer.main()

            elif selection == 2:
                pass
                # kitchen.main()

        except ValueError:
            input("\nOops!  That was no valid number.  Try again...")
