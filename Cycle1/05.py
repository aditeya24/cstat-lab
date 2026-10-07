fruits = ["apple", "orange", "banana", "grapes", "pineapple", "watermelon", "mango", "kiwi", "passion fruit"]

fruit = input("Enter a fruit name: ")
if fruit in fruits:
    print(fruit, "is a fruit")
else:
    print(fruit, "is not a fruit")