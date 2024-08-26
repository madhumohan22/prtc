class calcu:
    def __init__(self,A,B) -> None:
        self.a=A
        self.b=B
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)

answer=calcu(1,2)
answer.add()
