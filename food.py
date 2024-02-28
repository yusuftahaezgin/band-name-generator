import random
from turtle import Turtle


class Food(Turtle):  # Kalıtım: Turtle classını Food classına kalıtım ettik ana class Turtle kalıtım alan class Food oldu

    def __init__(self):  # class olusturulunca cagrılacak metodlar
        super().__init__()
        self.food = Turtle()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # dairenin default boyutunun (20,20) yarısı olarak ayarla dedik (10,10)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
