
class em2():
    def __init__(self) :
        print("cn")
    def display(self):
        print("hom")

class em3(em2):
    def __init__(self):
        print("ncd")
        super().__init__()
    def display(self):
        print("vkesd")

hari=em3()
