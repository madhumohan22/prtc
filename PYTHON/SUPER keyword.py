class em1():
    def __init__(self) -> None:
        print("hi")
    def HR(self):
        print("hiring")

class em2():
    def __init__(self) -> None:
        super().__init__()
        print("im desinger")
    def design(self):
        print("design info")

class em3(em2,em1):
    def __init__(self) -> None:
        super().__init__()
        print("im desingfer")
    def design2(self):
        print("fdesign info")

m1=em3()
m1.HR()
#m1.design()

