# Loops are used to repeat instructions.
#While Loops
#for loop
# n = 1 #Iterator
# while (n <= 5):
#     print("Hello")
#     n += 1

#Print numbers from 1 to 100.
# i = 1
# while (i <= 100):
#     print(i)
#     i += 1
# print("Loop Ended")

# Print numbers from 100 to 1.
# n = 100
# while (n >= 1):
#     print(n)
#     n -=1
# print("Loop Ended")


#Print the multiplication table of a number n.

# n = int(input("Enter the number :"))
# a = 1
# while (a <= 10):
#     print(n * a)
#     a += 1
#Print the elements of the following list using a loop:
# l = [1, 4, 9, 16, 25, 36, 49, 64 , 81, 100]
# i = 0
# while (i <= len(l)-1):
#     print(l[i])
#     i +=1

#Search for a number x in this tuple using loop:
l1 = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
indx = 0 #intial
x = 49
while (indx <= len(l1)-1):
    if (l1[indx] == x):
        print("Number found on index -->", indx)
    indx += 1    
    

     