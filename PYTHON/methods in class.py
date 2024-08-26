class laptop():
    #class varaible
    cabletype="C-type"
    def __init__(self):
        self.price="15"
    def dell(self):
        print(self.price,self.cabletype)
    @staticmethod
    def dell1():
        print("nothing")

laptop1=laptop()
laptop1.price="21"
laptop1.dell()
laptop1.dell1()