# Pattern 1 square (*) pattern
def pattern1():
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            print("*", end=" ")
            j = j+1
        print()
        i = i+1
pattern1()


# Using for loop
print("Using For loop")
def pattern_1(n):
    
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
pattern_1(5)


# Pattern 2 Right angle

print("Right angle * Pattern")
def rightPatt(a):
    i = 0
    while i < a :
        j = 0
        while j <= i :
            print("*", end=" ")
            j = j + 1
        print()
        i = i + 1
    
rightPatt(5)


#Pattern 3 Right angle

def numberPatt(b):
    i = 1
    while (i <= b):
        j = 1
        while (j <= i):
            print(j, end=" ")
            j = j + 1
        print()
        i = i + 1 
numberPatt(5)     


# Pattern 4
print("Pattern 4")
def pattern5 (c):
    i = 1
    while(i <= c):
        j = 1
        while (j <= i):
            print(i, end=" ")
            j = j + 1
        print()
        i = i + 1
pattern5(5)        
  
# Pattern 5
def pattern5(d):
    i = 1 
    while (i <= d):
        j = 0
        while (j < (d - i + 1)):
            print("*", end=" ")
            j = j + 1
        print()
        i = i + 1
pattern5(5)

# Pattern 7
print("Pattern 6")
def pattern6(e):
    i = 1
    while(i <= e):
        j = 1
        while(j <= (e - i + 1)):
            print(j, end=" ")
            j = j + 1
        print()
        i = i + 1
pattern6(5)

#Pattern 7
def pattern7(f):
    i = 0
    while (i < f):
        # for space
        j = 0
        while(j < (f - i -1)):
            print(" ")
            j = j + 1
            #for star 
            while (j < (2 * i -1)):
                j = j + 1
                
                # for space
                j = 0
                while(j < (f - i -1)):
                    print(" ")
                    j = j + 1
    i = i + 1
pattern7(5)
                

         


    

    