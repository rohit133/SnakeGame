from turtle import Turtle, left, right

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
           

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segment.append(snake)
    
    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]





    def extend(self):
        """Extend the tail of the Sanke"""
        self.add_segment(self.segment[-1].position())

    def move(self):
        """ **FOR DEVELOPERS ONLY**
        for seg_num in range(start = len(segment)-1, stop = 0, step = -1) 
        the loop is will start from the last index and will stop at 0 index and will take steps of -1 or 1 in reverse 
        """
        
        for seg_num in range(len(self.segment)-1, 0, -1):  
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP: 
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT: 
            self.head.setheading(RIGHT)