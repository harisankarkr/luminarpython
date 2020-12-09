class student:
    def set_student(self,rol,course,total):
        self.rol=rol
        self.course=course
        self.total=total
    def print_student(self):
        print("roll number=",self.rol)
        print("course=",self.course)
        print("total=",self.total)

obj=student()
obj.set_student(100,"mca",150)
obj.print_student()

obj.total+=50
print(obj.total)