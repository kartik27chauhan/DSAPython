#OOPS-->
#To map with real world scenarious, we started using objects code





#<-------OBJECT & CLASS---->

#Class is a BluePrint for creating objects.

#<---------CLASS------->
# class Student:
#     name ="Kartik"
#s1 = Student() #.......///////..Creating an Object.....///////////.......
# print(s1.name)

# s2 = Student()
# print("Name of the scond tudent will be same", s2.name)



#<--------CONSTRUCTOR-------->
#all classes have a function called _init_() which is always executed when the object is being initiated
#class Student:
 #   college_name = "CGC"  #Class Attribute
#    def __init__(self, name, marks): #*The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#         self.name = name
#         self.marks = marks
#         print("Adding new student in DataBase...")
# s1 = Student("Chauhan", 56)
# print(s1.name)
# s2 = Student("Kartik", 78)
# print(s2.name)
# s3 = Student("Monika", 98)
# print(s3.name)
# s4 = Student("Rahul", 88)
# print(s4.marks)
# print(s4.name)
# print(s4.college_name)
# print(s3.college_name)



#<------Attrinute------->
#Two types
#-->Class
#-->obj or Instance


#<-----Class ATTRIBUTE--->
#class Student:
#    clg_name = "CGC" #Class Attribute
#     def __init__(self, name, marks):
#         self.name = name #obj Atrributes
#         self.marks = marks
#         print("Adeed new student data...")
# s1 = Student("Kartik", 98)
# print(s1.name, s1.marks, s1.clg_name)
# s2 = Student("Monika", 100)
# print(s2.name, s2.marks, s2.clg_name)
# Student.clg_name



#<-------METHODS------->
# class Cars:
#     company_name:"Ford"
#     def __init__(self, car_name, engine, torque):
#         self.car_name = car_name
#         self.engine = engine
#         self.torque = torque
#         print("Adding car Data to DataBase...")
#     def model(self):
#         print("Model Specification", self.car_name, self.engine, self.torque)
# c1 = Cars("Mustang", 4951, 515)
# c1.model()
        



#Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hii", self.name, "You average score is:", sum/3)
        
# s1 = Student("Tony", [99,97,98])
# s1.avg()
    
    
    #<----------STATIC METHOD----------->
    #Methods that don’t use the self parameter (work at class level)

# class Student:
#      def __init__(self, name, marks):
#          self.name = name
#          self.marks = marks
#     @staticmethod         #DECORATOER -->*Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it
#      def hello():
#         print("Hello")
#      def avg(self):
#          sum = 0
#          for val in self.marks:
#              sum += val
#          print("Hii", self.name, "You average score is:", sum/3)
        
# s1 = Student("Tony", [99,97,98])
# s1.avg()
# s1.hello()


  #<----Important--->
#Abstraction--> Hiding the implementation details of a class and only showing the essential features to the user.


#Encapsulation --> Wrappimg Data and functions into single unit(object).

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
    #debit
    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount, "was debited")
        print(self.get_bal())
    #Credit
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount, "was Credited")
        print(self.get_bal())
    
    def get_bal(self):
        return self.balance
        
acc1 = Account(10000, 123456)
print(acc1.balance)
print(acc1.acc_no)

acc1.debit(5000)
acc1.credit(10000)


    
          








