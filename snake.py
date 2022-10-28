import turtle

MOVE_DISTANCE = 20
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
COLORS = ["green", "blue", "orange", "purple", "pink", "brown"]


class Snake:
    """Create a snake of size 3, based on Turtle Graphics"""
    def __init__(self):
        self.segments = []
        self.recycled = []
        self.initialize()
        
    def add_segment(self, x, y):
        """Creates a turtle as a segment in position x, y and appends turtle data to a list"""
        # Try to recycle a turtle
        if len(self.recycled) >= 1:
            self.recycled[0].goto(x=x, y=y)
            self.recycled[0].showturtle()
            self.segments.append(self.recycled.pop(0))
        # Create turtle
        else:
            turtle_loc = turtle.Turtle()
            turtle_loc.shape("square")
            turtle_loc.color("cyan")
            turtle_loc.penup()
            turtle_loc.goto(x=x, y=y)
            self.segments.append(turtle_loc)

    def initialize(self):
        """Recycles turtles and resets main Snake"""
        # Hide and recycle
        for former_segment in self.segments:
            former_segment.hideturtle()
            self.recycled.append(former_segment)
        
        # New snake
        self.segments.clear()
        a = 0
        for _ in range(3):
            self.add_segment(a, 0)
            a -= 20
        self.head = self.segments[0]

    def move(self):
        # Move starting from the tail to prevent empty spaces
        for segment_number in range(len(self.segments) - 1, 0, -1):
            self.segments[segment_number].goto(self.segments[segment_number - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def go_right(self):
        self.head.right(90)

    def go_left(self):
        self.head.left(90)
