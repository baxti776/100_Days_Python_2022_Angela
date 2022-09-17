import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# def get_mouse_click_coor(x, y):
'''Gets the coordination of the click on the screen.'''
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

guessed_states = []
while len(guessed_states) < 50:
    answer_state = turtle.textinput(prompt="What's another state name?",
                                    title=f"{len(guessed_states)}/50 answer correct.").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
# It is a test
