"""
#easy
#1
def kvadrat(n):
    return n**2
print(kvadrat(11))

#2
def cem(a, b):
    return a+b
print(cem(4, 5))

#3
def tek_cem(a):
    if a % 2 == 0:
        return "cem"
    else:
        return "tek"
print(tek_cem(8))

#4
def salamla(ad):
    return f"salam({ad})"
print(salamla(Meleyke))
#why doesn't work?

#5
def ortalama(a,b,c):
    return (a + b + c)/3
print(ortalama(6, 6, 12))

#medium
#6
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_of_list([4, 6 ,10, 2]))

#7 don't know how

#8
def reverse_string(text):
    return text[::-1]
print(reverse_string("Python"))

#9
def faqctorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(faqctorial(5))

#10
def simple_calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error"
    else:
        return "Invalid operation"
print(simple_calculator(11, 6, "*"))

#11 how?

#12
def kwargs_keys(**kwargs):
    for key in kwargs.keys():
        print(key)
print(kwargs_keys(name="Maleyka", age=16, city="Baku"))
#why doesn't print right things?

#13
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))

#14 what does it mean?
"""
#15
def palidrome(text):
    reversed_text = text[::-1]
    if text == reversed_text:
        return True
    else:
        return False
print(palidrome("ana"))
print(palidrome("something"))

#16 dont know how

#17
def average(*args):
    if not args:
        return 0
    total_sum = sum(args)
    count = len(args)
    return total_sum / count
print(average(10, 20, 30))

#18
def user_data(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += f"{key}: {value}"
print(user_data(name="Maleyka", age=16))
#why doesnt work?

#19,20 dont know how to do