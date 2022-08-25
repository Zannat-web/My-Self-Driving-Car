class student:
    def  __init__(self,id, CGPA=0):
           self.id = id
           self.CGPA = CGPA

    def display(self):
        print (self.id)
        print (self.CGPA)
student = student(223, 3.78)
print(student.id)
print(student.CGPA)