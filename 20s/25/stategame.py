import pandas
import turtle

FONT = ("Courier", 8, "normal")

# open csv
data = pandas.read_csv('50_states.csv')
list_of_states = data.state.to_list()

# set up screen
screen = turtle.Screen()
screen.title("US States Game")

# work with image
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# list of guessed states to compare
guessed_states = []

# game controller
correct = 0
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state in list_of_states:
        guessed_states.append(answer_state)
        correct += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(x = int(state_data.x), y=int(state_data.y))
        t.write(state_data.state.item(), align='center', font=FONT)
    if correct >= 50:
        game_on = False
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        t.write("You guessed all the states, congrats!", align='center', font=("Courier", 24, "normal"))
    if answer_state == 'Exit':
        missing_states = [missing_state for state in list_of_states if not in guessed_states]
        learning_data = pandas.DataFrame(missing_states)
        learning_data.to_csv('missed_states.csv')
        break
