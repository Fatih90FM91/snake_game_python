from turtle import Turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
Up = 90
Down = 270
Left = 180
Right = 0
MOVE_DISTANCE = 20
class Snake:


    def __init__(self):
        self.upgraded_segment = []
        self.create_snake()
        self.head = self.upgraded_segment[0]

    def create_snake(self):

        for position in starting_positions:
            self.add_segment(position)


    def add_segment(self, position):
        segment_1 = Turtle('square')
        segment_1.color('white')
        segment_1.penup()
        segment_1.goto(position)
        self.upgraded_segment.append(segment_1)

    def extend(self):
        self.add_segment(self.upgraded_segment[-1].position()) #position() comes from turtle class...



    def move(self):
        for seg_num in range(len(self.upgraded_segment) - 1, 0, -1):
            new_x = self.upgraded_segment[seg_num - 1].xcor()
            new_y = self.upgraded_segment[seg_num - 1].ycor()

            self.upgraded_segment[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

