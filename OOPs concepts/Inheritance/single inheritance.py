class parent:
    def __init__(self,fname,age):
        self.fname=fname
        self.age=age
    
    def view(self):
        print(self.fname,self.age)


class child(parent):
    def __init__(self,fname,age):
        parent.__init__(self,fname,age)
        self.lastname='reddy'
    
    def view(self):
        print(self.age,self.fname,self.lastname)


ob=child('madhusudhan',23)
ob.view()
