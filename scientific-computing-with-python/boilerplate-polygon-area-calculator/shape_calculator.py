from _typeshed import Self


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.width
    
    def get_perimeter(self):
        perimeter = (self.width * 2) + (self.width * 2)
        return perimeter
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else: picture = ""

        for line in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
    
    def get_amount_inside(self, other):
        amount_inside = self.get_area() / other.get_area()
        return int(amount_inside)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):
    def __init__(self, length):
        super().__init__()
        self.width = length
        self.height = length

    def set_side(self, length):
        self.height = length
        self.width = length
    
    def set_height(self, length):
        self.set_side(length)
    
    def set_width(self, length):
        self.set_side(length)

    def __str__(self):
        return f"Square(side={self.width})"
