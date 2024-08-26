class employee:
    def __init__(self,name,salary) -> None:
        self.name=name
        self.salary=salary
class manager(employee):

    def __init__(self, name, salary,departement) -> None:
        super().__init__(name,salary)
        self.departement=departement

    def display(self):
        print(self.name,self.salary,self.departement)

m1=manager("hari","2000","ece")
m1.display()

