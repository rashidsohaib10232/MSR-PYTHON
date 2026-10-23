class Student:
    def __init__(self,name,rollNo,marks):
        self.name = name
        
        self.marks = marks
        self.rollNo = rollNo

    def study(self):
        print("we r study! ")
        print("I am ",self.name," and my roll no. is ",self.rollNo," and my marks " ,self.marks," and know i am playing ")

    def play(self):
        print("We are playing! ")


s1 = Student("MSR",14,90)

print(s1.name,s1.marks)

# print(self.play())
