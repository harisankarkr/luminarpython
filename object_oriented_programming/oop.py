class person:
    def set_person(self,name1,age1,gender1):
        self.name=name1
        self.age=age1
        self.gender=gender1
    def print_person(self):
        print("name",self.name)
        print("age", self.age)
        print("gender", self.gender)

obj=person()
obj.set_person("ajay",25,"male")
obj.print_person()

obj1=person()
obj1.set_person("vijay",27,"male")
obj1.print_person()

obj1.age=28
obj1.print_person()