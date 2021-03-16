class Rectangle:
    # Create Rectangle Class

    def __init__(self, width, height):
        # Rectangle object constructor
        self.width = width
        self.height = height

    def set_width(self, length):
        self.width = length

    def set_height(self, length):
        self.height = length

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        txt = ''
        if self.width > 50 or self.height > 50:
            txt ="Too big for picture."
        else:
            for i in range(self.height):
                txt += ''.ljust(self.width, '*') + '\n'        
        return txt

    def get_amount_inside(self, shape):
        ''' Takes another shape (square or rectangle) as an argument.
        Returns the number of times the passed in shape could fit inside the shape (with no rotations)'''
        n = int(self.height / shape.height)
        m = int(self.width / shape.width)

        return (n * m)

    def __repr__(self):
        return('Rectangle(width=%s, height=%s)'%(self.width, self.height))


class Square(Rectangle):
    # Create Square Class
    
    def __init__(self, side):
        # Square object constructor
        self.side = side
        self.width = self.height = self.side

    def set_side(self, side):
        self.side = self.width = self.height = side

    def set_width(self, side):
        self.side = self.width = self.height = side

    def set_height(self, side):
        self.side = self.width = self.height = side

    def __repr__(self):
        return('Square(side=%s)'%self.side)
