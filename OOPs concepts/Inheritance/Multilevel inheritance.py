class parent:
    def __init__(self,fname,age):
        self.fname=fname
        self.age=age
    
    def view(self):
        print(self.fname,self.age)

class parent2(parent):
    def __init__(self,fname,age):
        parent.__init__(self,fname,age)
        self.place='pamidi'
    def view1(self):
        print(self.age,self.fname,self.place)


class child(parent2):
    def __init__(self,fname,age):
        parent2.__init__(self,fname,age)
        self.lastname='reddy'
    
    def view2(self):
        print(self.age,self.fname,self.lastname,self.place)


ob=child('madhusudhan',23)
ob.view()
ob.view1()
ob.view2()
