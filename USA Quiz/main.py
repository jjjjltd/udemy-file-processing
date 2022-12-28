import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Name Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")



guessed_states = []
missed_states = []
guesses = 0
right_guesses = 0

while len(guessed_states) < 50:

        screen_title = f"USA State Guesses: {len(guessed_states)} / {guesses}.  Total:  50"
        
        answer_state = screen.textinput(screen_title, "Please Enter a State name in the USA?")
        
        # Cancel
        if answer_state == None:
                break

        guesses += 1
        allstates = data.state.to_list()
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        if answer_state in allstates:
                statedata = data[data.state == answer_state]
                t.goto(int(statedata.x), int(statedata.y))
                t.write(answer_state)
                guessed_states.append(answer_state)
                right_guesses += 1

        else:
                t.goto(-200, 0)
                t.write("You f***wit!!")

print("made it this far.")
# for state in allstates:
#         if state not in guessed_states:
#                 missed_states.append(state)
# Using list comprehension for new list
missed_states = [state for state in allstates if state not in guessed_states]
new_data = pandas.DataFrame(missed_states)
new_data.to_csv("missed guesses.csv")

print(missed_states)

def get_mouse_click_coor(x, y):
        print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()