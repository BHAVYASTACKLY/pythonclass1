# for Loop Basics (1–10)
#1 Print numbers from 1 to 50 using for loop

for i in range (1,101):
 print(i)
 
 #2 Print even numbers from 1 to 100

for i in range (1,101):
     if i%2==0:
         print(i)
         
 #3 Print odd numbers from 1 to 100

for i in range (1,101,2):
       print(i)

#4 Print multiplication table of 7

for i in range(1, 11):
    print("7 x", i, "=", 7 * i)


#5 Find sum of numbers from 1 to 100

sum = 0
for i in range(1, 101):
    sum += i
print(sum)

#6 Print numbers in reverse from 50 to 1
for i in range(50, 0, -1):
    print(i)
    
#7 Count how many numbers are divisible by 3 (1–100)
count=0
for i in range (1,101):
        if 1%3==0:
          count +=1
print(count)
    
#8. Print squares from 1 to 10
for i in range (1,11):
    print(i*i)

#9. Print cubes of first 10 numbers
for i in range(1, 11):
    print(i ** 3)

#10. Take input n, print numbers from 1 to n
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i)

#Section 2: While Loop (11–15) 
#11 Print numbers from 1 to 20 using while             
i = 1
while i <= 20:
    print(i)
    i += 1

#12 Find factorial of a number
n = int(input("Enter a number: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial:", fact)

#13 Reverse a number
n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed number:", rev)

#14. Count digits in a number
n = int(input("Enter a number: "))
count = 0

while n > 0:
    n //= 10
    count += 1

print("Number of digits:", count)

#15. Keep asking input until user enters "stop"
user_input = ""

while user_input.lower() != "stop":
    user_input = input("Enter something (type 'stop' to end): ")

print("Loop ended.")

# Section 3: Nested Loop (16–20)
#16
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()

#17
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#18 Print multiplication table (1 to 5)
for i in range(1, 6):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()

#19 abc pattern
for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()

#20 
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()
    
 #Section 4: String Basics (21–25)
 #21.Count total characters in a string 
s = input("Enter a string: ")
print("Total characters:", len(s))

#22 
s = input("Enter a string: ").lower()

count = (s.count('a') + s.count('e') +
         s.count('i') + s.count('o') +
         s.count('u'))

print("Vowel count:", count)

#23
#Count consonants in a string //check oncee
def count_consonants(s):
    s = s.lower()
    consonants = "bcdfghjklmnpqrstvwxyz"
    return sum(s.count(c) for c in consonants)

text = "Hello World!"
print(f"Number of consonants: {count_consonants(text)}")

#24
#Reverse a string using loop
s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev  # Prepend each character

print("Reversed string:", rev)

#25 Check if string is palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam")) #true
print(is_palindrome("python")) #false

#Section 5: String Slicing (26–30)
#26 Print first 5 characters of a string
name="Helloworld"
print(name[:6])

#27 text = "HelloWorld"
text = "HelloWorld"
last_three = text[-3:]
print(last_three)

#28 
text = "HelloWorld"
reversed_text = text[::-1]
print(reversed_text)

#29 Print every 2nd character 
text = "HelloWorld"
every_second = text[::2]
print(every_second) 

#30 Remove first and last character from string
text = "HelloWorld"
modified_text = text[1:-1]
print(modified_text)

#Section 6: List Basics (31–35)
#31 Create a list of 5 numbers and print sum
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(total)

#32 Find maximum value in list
numbers = [10, 20, 30, 40, 50]
max_value = max(numbers)
print(max_value)

#33 Find minimum value in list

numbers = [10, 20, 30, 40, 50]
min_value = min(numbers)
print(min_value)

#34 Count total elements in list
numbers = [10, 20, 30, 40, 50]
total_elements = len(numbers)
print("Total elements:", total_elements)

#35 Check if element exists in list 
numbers = [10, 23, 45, 67, 89]
search_value = 23
print(f"{search_value} exists in list: {search_value in numbers}")
search_value = 100
print(f"{search_value} exists in list: {search_value in numbers}")

 #Section 7: List Operations (36–40)

 #36.Add 3 elements using append()
numbers = [10, 20, 30]
numbers.append(40)
numbers.append(50)
numbers.append(60)
print(numbers)

#37 Insert element at specific index
numbers = [10, 30, 20, 50, 40]
numbers.insert(2, 25)
print("After insert:", numbers)

#38 Remove element using remove()

numbers = [10, 30, 20, 50, 40]
numbers.remove(50)
print("After remove:", numbers)

#39 Reverse list without using .reverse()
numbers = [10, 30, 20, 50, 40]
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)


#40 Sort list without using .sort()

numbers = [10, 30, 20, 50, 40]
sorted_list = sorted(numbers)
print("Sorted list:", sorted_list)







