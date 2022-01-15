import avl
import customer
import kitchen
import os

if __name__ == "__main__":

    kitchen.start()
    main_food_prep = dict(filter(lambda l: l[0] in kitchen.food_menu, kitchen.food_prep.items()))

    while True:
        os.system("cls")
        print("\n-------------------- Welcome to Kharkhon Bashi Restaurant ---------------------\n")
        print("\n1. Usual mood reservation")
        print("\n2. Party mood reservation")
        print("\n3. Exit")

        try:
            selection = int(input("\n Please enter a number: "))

            if selection == 1:
                customer.start(main_food_prep)
                customer.main()

            elif selection == 2:
                pass
                # kitchen.main()

            elif selection == 3:
                print("Have Fun!")
                print("\nby: Kian & Adrina")
                exit(0)

        except ValueError:
            input("\nOops!  That was no valid number.  Try again...")
