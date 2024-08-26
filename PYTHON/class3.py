class teacher:
    def __init__(self,name,no):
        self.name=name
        self.regno=no
    def display(self):
        print(self.name,self.regno)
t1=teacher("hin","21")
t1.display()

t2=teacher("hari","34")
t2.display()