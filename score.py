from turtle import Turtle 


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score_sum=0
        self.right_score_sum=0
        self.up()
        self.color("white")    
        self.hideturtle()   
        self.update_score()

        

    def update_score(self):
        self.clear()
        self.goto(-50,240)    
        self.write(self.left_score_sum,align="center",font=("Arial",30,"bold"))
        self.goto(50,240)
        self.write(self.right_score_sum,align="center",font=("Arial",30,"bold"))
