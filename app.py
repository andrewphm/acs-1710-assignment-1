from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def homepage():
    """Shows a greeting to the user."""
    return "Are you there, world? It's me, Ducky!"


@app.route("/animal/<users_animal>")
def favorite_animal(users_animal):
    return f"Wow, {users_animal} is my favorite animal, too!"


@app.route("/desserts/<favorite_dessert>")
def favorite_dessert(favorite_dessert):
    return f"How did you know I liked {favorite_dessert}?"


@app.route("/madlibs/<adjective>/<noun>")
def madlibs(adjective, noun):
    return (
        f"That is an interesting {noun}, I've never seen one so {adjective} before!"
    )


@app.route("/multiply/<num1>/<num2>")
def multiple(num1, num2):
    if num1.isdigit() and num2.isdigit():
        return f"{num1} times {num2} is {int(num1) * int(num2)}"
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"


@app.route("/sayntimes/<word>/<num>")
def say_n_times(word, num):
    if num.isdigit() is False:
        return "Invalid inputs. Please try again by entering a word and a number!"

    repeated_str = ""
    for i in range(int(num)):
        repeated_str += word + " "

    return repeated_str


@app.route("/dicegame")
def dicegame():
    rand_num = random.randint(1, 6)
    if rand_num is not 6:
        return f"You rolled a {rand_num}. You lost!"
    else:
        return "You rolled a 6. You won!"


if __name__ == "__main__":
    app.run(debug=True)
