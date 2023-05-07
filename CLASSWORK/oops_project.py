#class define for student
class student:
    #blank dictionary
    db={}
    
    #input method-which accept from student user
    
    def input(self):
        email=input("enter your mail")
        password=input("enter your password")
        
        #storing data in db
        #here email is key and password is value
        #e.g manav@gmail.com: 123456
        
        self.db[email]=password
        
    def display(self):
        #display all students
        for k,v in self.db.items():
            print("email=",k)
            print("password=",v)
            
class faculty:
    db={}
    
    def inputdata(self):
        email=input("enter your mail")
        password=input("enter your password")
        
        self.db[email]=password
        
    def display(self):
        for k,v in self.db.items():
            print("email=",k)
            print("password=",v)
            
f1=faculty()
status=True
                          
            
#object creation of student class
s1=student()
status=True
while status:                


    data="""

press 1 for student registration
press 2 for faculty registration
press 3 for view all student
press 4 for exit

"""
    print(data)
    user_input=int(input("enter your choice:-"))
    if user_input==1:
        s1.input()
        
    elif user_input==2:
        f1.inputdata()
        
        
    elif user_input==3:
        s1.display()
        
    else:
        status=False
        
    choice=input("do you want to perform more operations?:-")
    if choice=='n':
        status=False                