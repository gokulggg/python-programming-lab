class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
    def rectangle_perimeter(self):
        return 2*(self.length+self.width)
l=int(input("Enter the length of the rectangle:"))
w=int(input("Enter the width of the rectangle:"))
object=Rectangle(l,w)
print("The area of the rectangle:",object.rectangle_area())
print("The perimeter of the rectangle:",object.rectangle_perimeter())

