import turtle

import pandas

import csv
screen=turtle.Screen()
screen.title("U.S. States Game")

image="blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

guessed_states=[]
answer_state=screen.textinput(title="Guess the State",prompt="What's another state's name?").title()
missed_states = []
game_is_on=True

df=pandas.read_csv("50_states.csv")
print(df)

city_list=df["state"].to_list()

print(city_list)
city_list.append("exit")
correct=0
while correct<50:

    if answer_state in city_list:

        guessed_states.append(answer_state)
        tu=turtle.Turtle()
        tu.hideturtle()
        position=city_list.index(answer_state)

        tu.penup()
        x=df.loc[position,"x"]
        y=df.loc[position,"y"]

        tu.goto(x,y)

        tu.pendown()
        tu.write(answer_state)
        correct+=1
    answer_state = screen.textinput(title= str(correct)+"/50 States Correct", prompt="What's another state's name?").title()

    if answer_state=="Exit":
        print("Guessed states")
        print(guessed_states)

        for state in city_list:
            if state not in guessed_states:
                missed_states.append(state)
        print("Missed states")
        print(missed_states)
        with open("missing_states.csv",mode="w") as file:
            writer=csv.writer(file)
            writer.writerow(missed_states)

        break

