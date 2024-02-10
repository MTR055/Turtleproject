import turtle as t
import random
colour = ['black','red','blue','green','pink','grey','yellow','orange','deep pink','medium slate blue','linen','gold','violet']
y_cor = [ -240 , -200, -160, -120, -80, -40 ,0,40,80,120,160,200,240]
starting_move_distance =10

moving_distance =10
class cars_crossing():
    def __init__(self):
        self.all_cars = []
        self.car_speed = 10


    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance ==1 :
            my_one = t.Turtle()
            my_one.shape('square')
            my_one.shapesize(stretch_wid=1, stretch_len=2)
            my_one.penup()
            my_one.color(random.choice(colour))
            random_y = random.choice(y_cor)
            my_one.goto(300,random_y)
            self.all_cars.append(my_one)


    def move(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed +=moving_distance







