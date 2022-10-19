from turtle import Screen
import time
from Snake import Snake
from Food import Food
from scoreboard import ScoreBoard
GAME_IS_ON = True


class SnakeGame:
    """create a new screen for you to play on and a new snake for you to play with. 
    beware, with each food pill that the snake eats it become longer and faster!
    try to avoid the walls and eating you own tail, and reach the highest score! GOOD LUCK"""
    def __init__(self):  # constructor
        self.screen = Screen()
        self.create_game_screen()
        self.score_num = 0
        self.snake = Snake()
        self.food = Food()
        self.score = ScoreBoard()
        self.start_game()
        self.define_exit()

    def create_game_screen(self):  # create the game screen
        self.screen.bgcolor("black")
        self.screen.setup(600, 600)
        self.screen.title("Snake")
        self.screen.tracer(0)  # turns off the animation and decide the delay between the segments

    def check_position(self):
        if self.snake.snake_head.xcor() > 300 or self.snake.snake_head.xcor() < -300:
            return True
        if self.snake.snake_head.ycor() > 300 or self.snake.snake_head.ycor() < -300:
            return True
        for i in range(2, len(self.snake.segments)):
            if self.snake.snake_head.distance(self.snake.segments[i]) < 10:
                return True
        else:
            return False

    def start_game(self):
        global GAME_IS_ON
        speed = 0.1
        while GAME_IS_ON:  # if snake is not at walls or does not eat itself
            self.screen.update()
            time.sleep(speed)  # speed of the snake
            self.snake.move()  # move forward
            if self.snake.snake_head.distance(self.food) < 15:  # snake eat food
                self.food.new_food()
                self.score.point()  # adds point to the score
                self.snake.add_seg()  # make the snake longer
                speed -= 0.002
            if self.check_position():
                GAME_IS_ON = False
            self.player_steps()
        self.score.game_over()

    def player_steps(self):  # keys commands
        self.screen.listen()
        self.screen.onkey(self.snake.go_right, "Right")
        self.screen.onkey(self.snake.go_left, "Left")
        self.screen.onkey(self.snake.go_up, "Up")
        self.screen.onkey(self.snake.go_down, "Down")

    def define_exit(self):
        self.screen.exitonclick()
