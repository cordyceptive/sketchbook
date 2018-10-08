from math import cos, sin, pi

def setup():
    size(500, 500)


def draw():
    make_polygon(4, 250, 250)


def make_polygon(sides, center_x, center_y):
    radius = 100
    CIRCLE_DEGREES = 360
    
    def parametric_x(angle):
        # angle given in degrees
        return radius * cos(float(angle * 180 / pi))
    def parametric_y(angle):
        return radius * sin(float(angle * 180 / pi))
    
    offset_degrees = CIRCLE_DEGREES / float(sides)
    current_degrees = 0
    prev_x = None
    prev_y = None
    for side in range(1, sides + 1):
        current_x = parametric_x(current_degrees)
        current_y = parametric_y(current_degrees)
        if prev_x is not None:
            line(prev_x, prev_y, current_x, current_y)
        prev_x = current_x
        prev_y = current_y
        current_degrees = current_degrees + offset_degrees
