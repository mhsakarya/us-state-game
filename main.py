import turtle
import pandas as pd
from text import Text

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)


data = pd.read_csv("50_states.csv")

text = Text()
answer_list = []
while len(text.text_list)<50:

    answer_state = screen.textinput(title=f"{len(text.text_list)}/50 States Correct", prompt="What's another state's name ?")
    answer_state = answer_state.title()
    states = data["state"].to_list()

    if answer_state == "Exit":
        state_for_learn = data.state.to_list()

        for each in answer_list:
            if each in state_for_learn:
                state_for_learn.remove(each)


        pd.DataFrame(state_for_learn).to_csv("learn.csv")

        break

    if answer_state in text.text_list:
        print()

    if answer_state in states:
        letter= answer_state
        xcor= data[data.state == letter].x
        ycor= data[data.state == letter].y
        text.create(letter, xcor, ycor)
        answer_list.append(answer_state)

    screen.update()

# states to learn.csc










screen.exitonclick()
