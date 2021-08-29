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



class Square(Rectangle):
    def __init__(self):
        super().__init__()

