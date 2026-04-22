"""
my_profile = {
    "name": "Maleyka",
    "last_name": "Sadiqzade",
    "age": 16,
    "favorite_programming_language": "Python"
}
print(my_profile["age"])
my_profile["age"] += 1
print(my_profile["age"])

menu = {
    "Coffe": 3.50,
    "Tea": 1.00,
    "Bun": 1.50
}
menu["Lemonade"]=4.00
menu["Tea"]=1.50
menu.pop("Bun")
print(len(menu))

inventory = {
    "laptop": 15,
    "monitor": 8,
    "mouse": 40
}
for item, quantity in inventory.items():
    print(quantity, item, "in stock")

country_codes = {"AZ": "+994", "TR": "+90", "US": "+1"}
code = input("Please enter your country code: ")
result = country_codes.get(code, "Invalid country code")
print(result)

fruits = ["apple", "quinace", "apple", "pomegranate", "quinace", "apple"]
fruit_counts = {}
for fruit in fruits:
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1
print(fruit_counts)

#these were from task dictionary

shopping_list = []
shopping_list.append("bread")
shopping_list.append("milk")
shopping_list.append("butter")
shopping_list.insert(0, "water")
shopping_list.remove("milk")
print(shopping_list)
print(len(shopping_list))

numbers = [12, 45, 7, 23, 56, 89, 11]
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)
print(sum(numbers))

#dont know how to do 3rd one

scores = [45, 67, 82, 34, 90, 55, 20,]
passing_scores = []
for score in scores:
    if score > 51:
        passing_scores.append(score)
print(passing_scores)

names = []
while True:
    name = input("Please enter a name (or type 'exit' to stop): ")
    if name.lower() == "exit":
        break
    names.append(name)
names.sort()
print(names)
"""











