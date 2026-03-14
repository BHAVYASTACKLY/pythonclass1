#bitwise operators(1-8)
#1
a=10
b=6
print(a&b)#2

#2
x=12
y=5
print(x|y)#13

#3
a=8
print(~a)#-9
#4
a=15
b=9
print(a^b)#6

#5
num=7
print(7<<2)#28
#6
num=20
print(20>>1)#10
#7
a=int(input("enter first number :"))
b=int(input("enter second number:"))
print(a&b) #2

#8
a=int(input("enter first number :"))
b=int(input("enter second number:"))
print(a^b)#5

#String Tasks (9–14)
#9
a="hi"
print(a*4)#hihihihi
#10
a="python"
print(a*3)
#11
str1="super"
str2="man"
print(str1+str2)#superman
#12
str1="hello"
str2=" "
str3="world"
print(str1+str2+str3)# hello world

#13
name=input("enter your name:")
print((name+"")*5)# bhavyabhavyabhavyabhavyabhavya

#14
str1=input("enter first string:")
str2=input("enter second string:")
print(str1+str2)#bhavyapidugu

#Input & Type Casting Tasks (15–20)
#15
name=input("enter your name:")
print("data type of name:" ,type(name))#str

#16
age=input("enter your age:")
age=int(age)
print("converted age:", age)
print("datatype of age:", type(age))#int

#17
a=int(input("enter first number:"))#3
b=int(input("enter second number:"))#3
num=a+b
print(num)#6
 
#18
m1=int(input("enter first mark:"))
m2=int(input("enter second mark:"))
average=(m1+m2)/2
print(average)#4.0


#19
a=int(input("enter value of a:"))#3
b=int(input("enter value of b:"))#2
result=3*(a**2)+b-2
print(result)#27

 #20
num=input("enter numer:")
print("before type casting:", type(num))#str

num=int(num)
print("after type casting:",type(num))#int

      
#Unit Digit Tasks (21–25)
#21
num=input("enter a number:")
print(num[-1])

#22
num=int(input("enter a number:"))#108
unit=num%10
print(unit)#8

#23
num=int(input("enter a number:"))
result=num//10
print(result)

#24
num=int(input("enter a number:"))
second=(num//10)%10
print(second)

#25
num=int(input("enter a 5 digit number:"))
lastdigit=num%10
print(lastdigit)

#If Statement Tasks (26–30)
#26
if 10>=5:
    print("10 is greather than or equal to 5")
    
#27
num=int(input("enter a number:"))
if num>50:
    print("the number is greater than 50")    

#28
age=int(input("enter your age:"))
if age>=18:
    print("you are an adult")

#29
num=int(input("enter a number:"))#101
if num>100:
 print ("greater than 100")
 
 #30
num =int(input("enter a number:"))
if num>=0:
    print("number is positive or zero")
    
#If-Else Tasks (31–34)
#31
num=int(input("enter a number:"))#10 then even answer
if num%2==0:
 print("even number")
else:
 print("odd number")

#32
marks=int(input("enter marks:"))#45 output even
if marks>=35:
    print("even number")
else:
    print("odd number")

#33
num=int(input("enter a number:"))
if num>0:
    print("positive number")
else:
    print("negative number")
    
 #34
num=int(input("enter a number:"))
if num>10:
     print("number is greater than 10")
else:
     print("number is not greater than 10")   
     
   #Nested If Tasks (35–37)
   #35
age=int(input("Enter your age:"))
height=int(input("enter your height(cm:)"))
weight=int(input("enter your weight(kg:)"))
if age>=18:
    if height>=160:
        if weight>=60:
            print("selected for the job")
        else:
            print("Rejected due to weight")
    else:
            print("Rejected due to height")
else:
        print("Rejected due to age")
        
   #36
marks=int(input("Enter your marks:"))
age=int(input("enter your age:"))
if marks>=60:
    if age>=17:
        print("Admission Granted")
    else:
        print("Admission Rejected due to age:")
else:
        print("Admission Rejected due to low marks")
        
        
#37
age=int(input("enter your age:"))
height=int(input("Enter your height(cm):"))
weight=int(input("Enter your weight(kg):"))
if age>=16:
    if height>=150:
        if weight>=50:
            print("Selected for sports team")
        else:
            print("Rejected due to weight")
    else:
            print("Rejected due to height")
else:
   print("Rejected due to age")

   
   #Match Statement Tasks (38–40)
#38

day=int(input("enter a number(1-7):"))
match day:
    case 1:
        print("Sunday")
    case 2:
     print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 7:
        print("saturday")
        
 #39
num=int(input("enter a number(1-3):"))
match num:
    case 1:
        print("Red")
    case 2:
        print("green")
    case 3:
            print("yellow")
            
 #40
num=int(input("enter a number:"))
match num:
  case 1:
         print("Apple")
  case 2:
         print("Mango")
  case 3:
         print("Orange")
  case 4:
         print("Banana")         
            
            

    
        
    
 
 
    

        

     
    
    
















