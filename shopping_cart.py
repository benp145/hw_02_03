class Product:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    

class Cart:
    items = []

    def __init__(self):
        print("\n\nWelcome to our e-store.")
        self.shop = input("Would you like to shop? (y/n): ").lower()
        shopping(self)

    def add_item(self):
        item_name = input("What item would you like to purchase? ").title()
        self.product = Product(item_name)
        self.items.append(self.product)
        print(f"{item_name} added to cart!\n")

    def show_cart(self):
        print("Here is your cart:")
        for item in self.items:
            print(item)
        print('\n')

    def remove_item(self):
        deleted_item = input("What item would you like to delete? ").title()
        for i in range(len(self.items)):
            if deleted_item == self.items[i].name:
                del self.items[i]
                print(f'{deleted_item} deleted from cart. \n')
                return

        print("Item not found in your cart.\n")


def shopping(cart_instance):
    if cart_instance.shop == 'y':
       print("""
Enter 'add' to add a new item to your cart.
Enter 'show' to see all items in your cart.
Enter 'delete' to delete an item from your cart.
Press 'quit' to end program. \n""","="*8)
    while cart_instance.shop == 'y':
        print("What would you like to do?")
        prompt = input("Add | Show | Delete | Quit ").lower()
        print('\n')
        if prompt == 'add':
            cart_instance.add_item()
        elif prompt == 'show':
            cart_instance.show_cart()
        elif prompt == 'delete':
            cart_instance.remove_item()
        elif prompt == 'quit':
            quit = input("Are you sure you want to quit? (y/n): ").lower()
            if quit == 'y':
                break
        else:
            input("Invalid input. press enter to try again.")
    print("Thanks for visiting!!")


my_cart = Cart()
