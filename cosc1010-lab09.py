# Jake Huggins          
# UWYO COSC 1010
# 11/11/2024
# Lab 09    
# Lab Section: 14
# Sources, people worked with, help given to: None

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria

# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
# - If it is not, default to a 10" pizza (you can store ten). These checks should
# occur in init as well.
# - For toppings, you will need to add the toppings.
# - This method needs to be able to handle multiple values.
# - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety
# checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.
class Pizza:
    def __init__(self, size, sauce = "Red"):
        if (size < 10):
            self.size = 10
        else:
            self.size = size
        self.sauce = sauce
        self.toppings = ["Cheese"]
  
    def addToppings(self, toppings_added):
        
        for i in range(len(toppings_added)):
            self.toppings.append(toppings_added[i])
        
    def getAmountOfToppings(self):
        return len(self.toppings)

    def getSize(self):
        return self.size
    
    def getSauce(self):
        return self.sauce
    
    def getToppings(self):
        return self.toppings

# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per
#inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the
#list.
# You will need the following methods:
# - __init__()
# - This one does not need to take in any extra parameters.
# - It should create and set the attributes defined above.
# - placeOrder():
# - This method will allow a customer to order a pizza.
# - Which will increment the number of orders.
# - It will need to create a pizza object.
# - You will need to prompt the user for:
# - the size
# - the sauce, tell the user if nothing is entered it will default to red sauce
#(check for an empty string).
# - all the toppings the user wants, ending prompting on an empty string.
# - Implementation of this is left to you; you can, for example:
# - have a while loop and append new entries to a list
# - have the user separate all toppings by a space and turn that into a list.
# - Upon completion, create the pizza object and store it in the list.
# - getPrice()
# - You will need to determine the price of the pizza.
# - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings()
# * price_per_topping.
# - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
# - Creates a receipt of the current pizza.
# - Show the sauce, size, and toppings.
# - Show the price for the size.
# - The price for the toppings.
# - The total price.
# - getNumberOfOrders()
# - This will simply return the number of orders.
class Pizzeria:
    def __init__(self):
        self.orders = 0
        self.price_per_topping = 0.30
        self.price_per_inch = 0.60
        self.pizzas = []
    
    def placeOrder(self):
        self.orders += 1
        size = 0
        sauce = ""
        toppings = []

        while (True):
            size = input('\nPlease input a size for your pizza. It must be great than 10": ')
            try:
                size = int(size)
            except:
                print("\nPlease enter a whole number.")
                continue
            #int(size)
            sauce = input("\nPlease input a sauce for your pizza. If none entered, the pizza will have red sauce: ")
            if (sauce == ""):
                sauce = "Red"
            while (True):
                response = input("\nPlease list the toppings you'd like. Press enter to stop: ")
                if (not response == ""):
                    toppings.append(response)
                    continue
                break
            break

        new_pizza = Pizza(size, sauce)
        #print(len(toppings))
        #print(toppings)
        if (len(toppings) >= 1):
            new_pizza.addToppings(toppings)
        self.pizzas.append(new_pizza)

    def getPrice(self):
        pizza = self.pizzas[-1]
        return (pizza.getSize() * self.price_per_inch) + (pizza.getAmountOfToppings() * self.price_per_topping)
    
    def getReceipt(self):
        pizza = self.pizzas[-1]
        print("\nReceipt for your pizza.")
        print(f'Size: {pizza.getSize()}" \nSauce: {pizza.getSauce()} Sauce \nToppings: {pizza.getToppings()}')
        print(f"Ordered a {pizza.getSize()} for {round(pizza.getSize() * self.price_per_inch, 2)}$")
        print(f"Ordered {pizza.getAmountOfToppings()} toppings for {round(pizza.getAmountOfToppings() * self.price_per_topping, 2)}$")
    
    def getPizzasProduced(self):
        return self.orders

# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.
# Example output:

pizzeria = Pizzeria()

while (True):
    if (input("Welcome to the Pizzeria. Press enter to continue and type 'Exit' to exit: ").lower() == "exit"):
        print("\nPlease come again!")
        break
    pizzeria.placeOrder()
    pizzeria.getReceipt()
    print(f"The total price of your pizza will be: {round(pizzeria.getPrice(), 3)}$")
print(f"The pizzeria had {pizzeria.getPizzasProduced()} orders for pizzas.")