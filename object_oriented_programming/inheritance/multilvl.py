class parent:
    def m1(self):
        print("inside parent")

class child(parent):
    def m2(self):
        print("inside child")

class subchild(child):
    def m3(self):
        print("inside subchild")

ch2=subchild()
ch2.m3()
ch2.m2()
ch2.m1()