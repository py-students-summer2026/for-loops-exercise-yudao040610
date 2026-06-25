import turtle

def create_turtle(stroke_color, bg_color):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(stroke_color)
    window = turtle.Screen()
    window.bgcolor(bg_color)
    return t

def pick_up_and_move_turtle(t, x, y):
    t.penup()
    t.setposition(x, y)
    t.pendown()

def print_turtle_position(t):
    print("Turtle at", t.position(), "rotated", t.heading(), "degrees")

def draw_square(t, start_x, start_y, length, rotation_direction, fill_color):
    pick_up_and_move_turtle(t, start_x, start_y)
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(4):
        print_turtle_position(t)
        t.forward(length)
        if rotation_direction == "left":
            t.left(90)
        else:
            t.right(90)
    t.end_fill()

def draw_star(t, start_x, start_y, length, angle, initial_rotation_direction, fill_color):
    pick_up_and_move_turtle(t, start_x, start_y)
    t.fillcolor(fill_color)
    t.begin_fill()
    small_angle = angle - 72
    for _ in range(5):
        print_turtle_position(t)
        t.forward(length)
        if initial_rotation_direction == "left":
            t.left(angle)
        else:
            t.right(angle)
        
        t.forward(length)
        if initial_rotation_direction == "left":
            t.right(small_angle)
        else:
            t.left(small_angle)
    t.end_fill()