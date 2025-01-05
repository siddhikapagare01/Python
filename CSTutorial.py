#Taking input from user & printing it
'''name = input("name :") #string input
print(name)

age = int(input("age : ")) #int input
print(age)

price = float(input("price : ")) #float input
print("My name is",name, "am I am",age, "year old")

#Condition Statements
Light = input("Light color : ")

if (Light == "red"):
    print("stop")
elif(Light == "yellow"):
    print("Look")
elif(Light == "green"):
    print("go")
else:
    print("Light is broken")

#Grades of students 
marks = input("marks : ")

if(marks >= "90"):
    print("A")
elif(marks >= "80" and marks < "90"):
    print("B")
elif(marks >= "70" and marks < "80"):
    print("C")
else:
    print("D")
    
A = int(input("A : "))
G = input("M/F : ")
if((A ==1 or A ==2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G =="F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")
else:
    print("no fee")
    
#conditional Statements - single line if I ternary operator
food = input("food :") # <var> =  <var1> if < condition > else < val2 >
eat = "Yes" if food == "cake" else "no"
print(eat)

food = input("food :") #<str1> if <condition> else <str2>
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet"

age = int(input("age : ")) # Clever if i ternary operator
vote = ("yes","no") [age >= 18]
print(vote)

sal = float(input("salary : "))
tax = sal*(0.1,0.2) [sal>50000]
print(tax)

#Calculate simple interest
p = float(input("p :"))
r = float(input("r :"))
t = float(input("t :"))
si = (p*r*t)/100
print(si)

#arithmetic operators
a = 5
b = 2 
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #remainder
print(a ** b) #a^b

#relational operators
a = 50
b = 20
 
print(a == b) #False
print(a != b) #True
print(a >= b) #Ture
print(a > b) #True
print(a <= b) #False
print(a < b) #False

#assignment operator
num = 10
#num = num + 10 #10+10 =>20
num += 10  #(-= , *= , /= , **=)
print("num :", num)

#logical operator
a = 50
b = 30
print(not False) #not 
print(not (a > b))

val1 = True
val2 = False
print("ans operator:", val1 and val2)

print("or operator:", (a ==b) or (a > b))'''


