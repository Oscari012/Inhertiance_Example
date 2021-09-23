clas Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def what_am_i (self):
        print("I am a shape")

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

rectangle = Rectangle(4, 5)
square = Square(4, 4)

rectangle.what_am_i()
square.what_am_i()s
