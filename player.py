import turtle as t

class player_game(t.Turtle):
    def __init__(self):
        super(). __init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.goto(0,-280)
        self.setheading(90)

    def go_up(self):
        self.forward(10)

    def level_up(self):
        self.penup()
        self.goto(0,-280)

