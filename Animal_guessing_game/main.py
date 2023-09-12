import turtle

import pandas as pd

screen = turtle.Screen()
screen.setup(width=655, height=712)
screen.title("Animal Guessing Game")
image = "animals.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("animals_name.csv")
animal_name = data.name.to_list()

guessed_animals = []
while len(guessed_animals) < 46:
    answer_animal = screen.textinput(title=f"{len(guessed_animals)}/46 Correct Answer",
                                     prompt="What's another animal's name?").title()
    if answer_animal == "Exit":
        break
    if answer_animal in animal_name:
        guessed_animals.append(answer_animal)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        animal_data = data[data.name == answer_animal]
        t.goto(int(animal_data.x), int(animal_data.y))
        t.pencolor("grey")
        t.write(answer_animal, font=("Arial", 14, "normal"))

