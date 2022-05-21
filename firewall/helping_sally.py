#!/usr/bin/env python3

business_name = "Sally's Fruity Loops"

#This is the list of all the fruits I'll be selling
                                                                                                                                                 
fruit_list = ["Apple", "Banana", "Cherries", "Dragon Fruit" "Fig"
               "Grapefruit", "Kiwi", "Lemon" "Lime" "Mango" "Oranges", "Pineapple"
              "Grapes" "Watermelon"]

#This is the list of the prices of each fruit in the fruit list.

fruit_prices_list = [ 1.35, 1.30, 0.32, 0.60, 0.80, 1.76, 3.32, 0.34, 2, 3, 2.46, 1.43,
                      1.8, 1.9]

#Check if the first item in the fruit list is apple and then display
#a notice to customers.

if fruit_list[0] == "apple":
    print("Sally sells apples too!")


#Calculate how much discount to give customers on opening day
#by adding the prices of the first 2 fruits, divide by 100 and
#multiply by 5

discount_amount = (fruit_prices_list[0]+ fruit_prices_list[1] / 100) * 5
discount_percent = discount_amount * 100
print("Thanks for being a valued customer! Your discount is: ", "discount-percent", "%")

#'' The code below will be used to show customers a list of random fruits on sale. ''

first_sample_from_fruit_list = fruit_list[1]
second_sample_from_fruit_list = fruit_list[5]
third_sample_from_fruit_list = fruit_list[5]
fourth_sample_from_fruit_list = fruit_list[4]
fifth_sample_from_fruit_list = fruit_list[1]

print("Here are the fruits on sale today:")
print("first sample from fruit-list")
print("second sample from fruit-lists")
print("third samples from fruit-list")
print("fourth sample from fruit-lists")

#This is a list of the first three fruits. I'll give these for free on my birthday

fruit1, fruit2, fruit3 = fruit_list[1],fruit_list[2],fruit_list[3]
print("fruit1, fruit2, fruit3")

#Declare a variable to store a customer's shopping cart total BEFORE they start shopping'

customer_total = None

#This is the raw string that will be displayed on the homepage of the store's website
#The website can process newline characters (\n) and turn them into smiley faces,
#so we'll need those to show when the string is printed

Raw_Welcome = "Welcome to Sally's \n fruity loop store"
print(Raw_Welcome)

#Check that the customer cart total works properly by testing the cart total functionality

customer_total = ("customer-total" + "10")
print(customer_total)

#Declare a string to thank a customer for shopping and show them their cart total
#after ordering:

goodbye_msg = "Thanks for shopping at Sally's Fruity Loops"
print("Your total for today is: Customer-Total")


#SET OF GREETINGS THAT EACH CUSTOMER WOULD SEE
print("Good Morning",'\n',"Good Afternoon", '\n', "Good Evening", '\n', "Hello", '\n' "Welcome")

#Using dictionaries for 5 vegetables
d = {"Cucumber": "$1.50", "Onions": "$2.50", "Peppers": "$3.50", "Cabbage": "$4.50", "Brocolli": "5.50"}
#d["Cucumber"] = "$1.50"
#d["Onions"] = "$2.50"
#d["Peppers"] = "$3.50"
#d["Cabbage"] = "$4.50" 
#d["Brocolli"] = "$5.50"

for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print("")

#Boolean for customers cart
x = 1 == True
y = 1 == False
a = True + 0
cart_empty= False + 0

print("x is:", x)
print("y is:", y)
print("a:", a)
print("cart_empty:", cart_empty)


