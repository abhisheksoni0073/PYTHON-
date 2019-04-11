#The isinstance() method is used to check the relationship between the objects 
#and classes. It returns true if the first parameter, i.e., 
#obj is the instance of the second parameter, i.e., class.
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(isinstance(d,Derived)) 