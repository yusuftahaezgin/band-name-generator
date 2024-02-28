import time
from turtle import Screen
from snake import Snake
from scoreboard import ScoreBoard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ezgin's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # 0.1 sn delay koyduk ki bir butun seklinde karelerin gidisini gorebilelim
    snake.move()

    # Yılanın yemekle carpısması kontrolu
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Yılanın duvara carpması kontrolu
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Yılanın kendi kuyruguna carpması kontrolu

    #for segment in snake.segments:
        # if segment == snake.head: # bunu yazmazsak oyun baslar baslamaz biter cunku yılanın kafasını atlamalıyız yoksa dongu 0 dan baslıyacagı icin yılanın kafasının yılanın kafasına olan uzaklıgını da hesaba katar bu uzunluk 10 dan az olacagı icin oyun baslamdan biter!!!
        #     pass
        # elif snake.head.distance(segment) < 10: # yılanın kafasının geri kalan segmentlere uzaklıgı 10 dan azsa demek ki kendisine carpmıstır
        #     game_is_on = False
        #     score.game_over()

        # ustteki kod sorunsuz calısır ancak bu koda ek olarak altta daha basit sekilde yapılacak yontem vardır pythonda
        # bu yontem ise slicing yontemidir yani dilimleme yontemi day-21 196.video

    for segment in snake.segments[1:]: # burada [1:] slicing yaptık lsitenin birinci elemanı haric hepsini aldık
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
