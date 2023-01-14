# Polygon Area Calculator

A little program for displaying squares and rectangles and calculating how many of a rectangle fit in a larger rectangle.

## Functionality

### Rectangle class

When a Rectangle object is created, it is initialized with width and height attributes. The class contains the following methods:

    set_width
    set_height
    get_area: Returns area (width * height)
    get_perimeter: Returns perimeter (2 * width + 2 * height)
    get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
    get_picture: Returns a string that represents the shape using lines of "*". This is used to display the shape as an area, where each unit is represented by a *. If the width or height is larger than 50, this returns: "Too big for picture.".
    get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

The Square class is a subclass of Rectangle.

Additionally, the set_width and set_height methods on the Square class should set both the width and height.

## Example Usage

    rect = shape_calculator.Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = shape_calculator.Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
    
Should output:  
    
    50
    26
    Rectangle(width=10, height=3)
    **********
    **********
    **********

    81
    5.656854249492381
    Square(side=4)
    ****
    ****
    ****
    ****

    8
    
## Tests
The unit tests are in `test_module.py`
