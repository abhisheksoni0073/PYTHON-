class Mss:  # base class to drive class 
    def speak(self):  
        print("Animal Speaking")  
#child class Mss inherits the base class Animal  
class hacker(Mss):  
    def bark(self):  
        print("dog barking")  
d = hacker()  
d.bark()  
d.speak()  