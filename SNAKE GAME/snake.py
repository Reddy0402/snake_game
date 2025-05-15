from  turtle import Turtle

move_distance =20
start_pos =[(0,0),(-20,0),(-40,0)]
Up =90
Down =270
Left =180
Right =0



class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in start_pos:
            self.add_segments(pos)
    def add_segments(self,pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        # lay.shapesize(1)
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        #add extra boxes
        self.add_segments(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)
    def up(self):
       if  self.head.heading() !=Down:
           self.head.setheading(Up)

    def down(self):
       if  self.head.heading() !=Up:
           self.head.setheading(Down)

    def left(self):
       if self.head.heading() !=Right:
           self.head.setheading(Left)

    def right(self):
       if self.head.heading() !=Left:
           self.head.setheading(Right)



