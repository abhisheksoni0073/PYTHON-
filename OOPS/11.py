class Student:  
    def __init__(self,name,id,age):  
        self.name = name;  
        self.id = id;  
        self.age = age  
    def display_details(self):  
        print(self.id)  
s = Student("John",101,22)  
print("Doc ", s.__doc__)  
print("dict",s.__dict__)  
print("moduel",s.__module__)  