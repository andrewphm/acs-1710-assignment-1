from flask import Flask

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


if __name__ == "__main__":
    app.run(debug=True)
