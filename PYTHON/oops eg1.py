class shape:
    def area(self):
        return 0

class rectangle(shape):
    def area(self):
        l=int(input())
        b=int(input())
        return (l*b)

s1=rectangle()
print(s1.area())

    