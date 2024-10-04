light = "green"

if (light == "red"):
    print("Stop")
elif(light == "green"):
    print("go")
else:
    print("end of code")
    
    
#Grade students

marks = int(input("Enter your marks :"))
if (marks >= 90):
    print("Your Grade is : A")
elif(marks >= 80 and marks < 90):
    print("Your Grade is : B ")
elif(marks >=70 and marks < 80):
    print("Your Grade is : C")
else:
    print("Your Grade is : D")
    
#................//////////////////............../////////////////.........    
#NESTING
age = int(input("Enter you age :"))
if(age >= 18):
    if(age>=51):
        print("You can not Drive")
    print("You can Drive")
else:
    print("You cannot Drive")
    
#...........///////////////////////..................//////////////////.....

#Practice Question

#Wap to check if a number entered by the user is odd or even
num = int(input("enter your number :"))
if(num % 2 == 0):
    print("Your number is Even")
else:
    print("Your number is odd") 
#..............////////////////////..............////////////////..

#WAP to find the Greates of 3 numbers entered by the user
num1 = int(input("Enter your first number :"))
num2 = int(input("Enter your second number :"))
num3 = int(input("Enter your third number :"))
if (num1 > num2 and num1 > num3):
    print("The Greatest number is :",num1)
elif( num2 > num3):
    print("The Greatest number is :",num2)
else:
    print("The greates number is :",num3)
#..........///////////////////...............//////////////....../////

#WAP to check if number is a multiple of 7 or not.
a = int(input("Enter your number"))
if(a % 7 == 0):
    print("The number",a,"is multiple of 7")
else:
    print("Its not the Multiple")
#......../////////////..................//////////
#The task is to write a program that calculates the electricity bill based on the following criteria:

# First 100 units: No charge.
# Next 100 units (101 to 200): Rs 5 per unit.
# Beyond 200 units: Rs 10 per unit.

amt = 0
nu = int(input("Enter your unit :"))
if (nu <= 100):
    print("You don't have to pay any charges",amt)
elif (nu > 100 and nu <= 200):
    amt = (nu-100)*5
    print("Your amount to be paid is :", amt)
else:
    amt = 500 + (nu-200)*10
    print("Your amout to be paid is :",amt)
    
#............//////////////////........///////////////////////////

print("To Check whether the last digit of a number is divisible by 3 or not")
n = int(input("Enter your number : "))
c = n % 10
if (c % 3 == 0):
    print("last digit is divisible by 3 ->",c)
else:
    print("Last digit  is not divisible by 3")
