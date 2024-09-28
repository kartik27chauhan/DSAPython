def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
a = 9
b = 80
calculateGmean(a,b)
def isGreater (a,b):
    if (a >b):
        print("First Number is Greater")
    else:
        print("Second Number is greater")
isGreater(a,b)
def add (a,b):
    print(a+b)
add(5,6)


#Default Arguments
print("Thi program is for Default Arguments:")
def average(a=9, b=1):
    print("The average is:", (a+b)/2)
average()

print("If we give arguments when we are calling function it will ignore the default values")
average(3,4)

#one More Example
def name(fname, mname="chauhan", lname="rajput"):
    print("Hello",fname, mname, lname)
name("Kartik")



#Keyword Arguments 
print("This program is for Keyword Arguments")
print("Order of the arguments does't matter")
def sum (a=9,b=8,c=10):
    print("The sum is:",a+b+c)
sum()
print("Now we will give arguments when we will call function but not the same order as giving in default")
sum(b=10,c=5,a=10)


#Required Argumenst
# print("We have to pass the argument value it is necesary")
# def name(fname, mname, lname):
#     print("Hello",fname, mname, lname)
# name("Kartik")
#Gives TypeError: name() missing 2 required positional arguments: 'mname' and 'lname'

#Variable Length Arguments
def av(*numbers):
    sum = 0
    for i in numbers:
        sum+=i
    print("Average is:", sum/len(numbers))
av(5,6)


#if we want as a Dictinories **
def na(**name):
    print("Hello", name["fname"],name["mname"],name["lname"])
na(mname="Chauhan",lname="rajput",fname="Kartik")


#Return Statment
print("The return statment is used to return the value of the expression back to the calling function")
def a(a,b):
    return a +b
c = a(4,5)
print("The sum is :",c)







