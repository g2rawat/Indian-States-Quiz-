
import turtle
import pandas
screen=turtle.Screen()
screen.tracer(0)
img="india_map.gif"
screen.title(img)
screen.bgcolor("black")
screen.addshape(img)
turtle.shape(img)
# ______________________________________________________________________
# def cor(x,y):
#     print("coredinates: ({0},{1})".format(x,y))
# screen.onscreenclick(cor,1)
# screen.listen()
# turtle.done()
# _______________________________________________________________________
data=pandas.read_csv("indian_state.csv")
states_only=data.States.to_list()
gig=turtle.Turtle()
gig.penup()
num=0
scr=0
tru=True
score=turtle.Turtle()
score.penup()
score.color("white")
score.hideturtle()
bg=turtle.Turtle()
bg.shape("square")
bg.shapesize(2,7)
bg.penup()
bg.goto(-10,245)
right_guess=[]
while tru:
    screen.update()
    score.clear()
    score.goto(-65,230)
    score.write(f"Score: {scr}",font=("Arial",20,"bold"))
    guess_state=screen.textinput(f"{scr}/28 gussed correctly","write a state name").title()
    if guess_state=="Exit":
        break

    if num>=28:
        tru=False
        break
    if guess_state in states_only:
        xcor=data[data.States==guess_state].x
        ycor=data[data.States==guess_state].y
        gig.goto(int(xcor),int(ycor))
        gig.write(guess_state)
        scr+=1
        right_guess.append(guess_state)
    num+=1
left_state=[]
for state in states_only:
    if state not in right_guess:
        left_state.append(state)
# print(left_state)
left_states=pandas.DataFrame(left_state)
left_states.to_csv("left_states.csv")




