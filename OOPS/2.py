#Multi-Level inheritance
class A:  
    def speak(self):  
        print("Animal Speaking")  
#The child class Dog inherits the base class Animal  
class B(A):  
    def bark(self):  
        print("dog barking")  
#The child class Dogchild inherits another child class Dog  
class C(B):  
    def eat(self):  
        print("Eating bread...")  
d = C()  
d.bark()  
d.speak()  
d.eat() 