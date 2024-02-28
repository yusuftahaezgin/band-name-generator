# snake sınıfının olusturulması : day-20 187.video

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position()) # self.segments[-1].position() bu kodla segments listesindeki son elemanın positionuna eristik


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # 3 segment varsa 2,1,0 diye gider dongu
            # sondan bir onceki yani ortadaki karenin koordinatlarını alıp bunu sondaki kareye aktaracaz ilerlemenin mantıgı soyle olacak
            # 321 diye sıralanmıs kareler dusununce en sondaki kare ortadaki karenini yerini alacak yani 3 2 nin yerini alacak
            # ortadaki kare en bastaki karenin yerini alacak yani 2 1 in yerini alacak kısaca kaydırarak gideceklerki donuslerde sorun olmasın
            # anlamadıysan day-20 186. video bak
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: # asagı gidiyorsa yukarıya donemesin! (snake oyunu kuralları)
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP: # yukarı gidiyorsa asagı donemesin!
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT: # sola gidiyorsa saga donemesin!
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT: # saga gidiyorsa sola donemesin!
            self.head.setheading(LEFT)
