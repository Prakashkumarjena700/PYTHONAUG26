# OOP 
# Class and Object
# Method
# Constructor

# class Employee:       # Class (Blue print)
#     name = "Rahul"
#     emp_id = 1
#     salary = 50000
#     dept = "IT"
    
# emp1 = Employee()  
# emp2 = Employee()  

# print(emp1.name)
# print(emp1.emp_id)
# print(emp1.salary)
# print(emp1.dept)
# print("---------")
# print(emp2.name)



# Method 
# class Mobile:
#     brand = "IPhone"
#     price = 100000
    
#     def Ringing(self):
#         # print("Incomming call", self.brand)
#         return "Incomming call.."
        
#     def Notification(self):        # Method
#         print("1 notification")    
        
# mobile1 = Mobile()   
 
# print(mobile1.price)
# mobile1.Ringing()
# print(mobile1.Ringing())


# class Employee:
#     name = "Rahul"
#     salary = 50000
    
    
#     def __init__(self):
#         self.address = "BBSR"
#         print("Constructor 1")   

# emp1 = Employee()

# print(emp1.name)
# print(emp1.address)

        
# class Employee:                                 # Class
#     def __init__(self,name,salary,address):     # Constructor
#         self.name = name
#         self.salary = salary
#         self.address = address
    
#     def EmployeeDetails(self):                  # Method
#         print("Emplee Name" , self.name)
#         print("Emplee Salary" , self.salary)
#         print("Emplee Address" , self.salary)
        

# e1 = Employee(name="Sonali", salary=50000,address="BBSR")        
# e2 = Employee(name="Sushree", salary=50000, address="Delhi")        

# e1.EmployeeDetails()              
# print(e2.address)        

# class Employee:
#     def __init__(self, name, salary=45000):
#         self.name = name
#         self.salary = salary
        
#     def ReturnDetails(self):
#         return "adjadjasd"


# e1 = Employee(name="Rahul")    
# e2 = Employee(name="Rahit", salary=50000)    
            
# print(e1.salary) 
# print("-------------")           
# print(e2.salary)            


class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print("Diposit amount is : ",amount)
    
    def withdraw(self,amount):
       if amount <= self.balance:
            self.balance -= amount
            print("Withdrow amount is : ",amount)
       else:
           print("Insuffcient balance")     
    
    def viewBalance(self):
        print("Here is your balance",self.balance)     
        
u1 = BankAccount("Sushree",1000) 
u1.deposit(5000) 
u1.withdraw(8000)        
u1.viewBalance() 
        
        