import turtle as t

class scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(0,300)
        self.write(f'Level :{self.level} ',align= 'center',font= 'Arial')

    def increase_score(self):
        self.level +=1
        self.clear()
        self.write(f'Level :{self.level} ', align='center', font='Arial')
