class parent:
    def __init__(self,fname,age):
        self.fname=fname
        self.age=age
        self.college='VIT'
    
    def view(self):
        print('name:',self.fname,'Age:',self.age,'college:',self.college)

class child1(parent):
    def __init__(self,fname,age):
        parent.__init__(self,fname,age)
        self.place='pamidi'
    def view1(self):
        print('Age:', self.age,'name:',self.fname,'place:',self.place)


class child2(parent):
    def __init__(self,fname,age):
        parent.__init__(self,fname,age)
        self.lastname='reddy'
    
    def view1(self):
        print('Age:',self.age,'fname:',self.fname,'lname',self.lastname)


ob=child1('madhusudhan',23)
ob1=child2('Ramesh',25)
ob.view()
ob.view1()
ob1.view()
ob1.view1()
