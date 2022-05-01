from flask import Flask, render_template, request
from recipe_helper import get_recipes_steps, get_recipes_title

app = Flask(__name__)


@app.route('/recipe/', methods=["GET", "POST"])
def get_recommend():
    if request.method == "POST":
        ingredient = request.form["ingredient"]
        calories=float(request.form["calories"])
        title=get_recipes_title(ingredient,calories)
        steps=get_recipes_steps(ingredient,calories)
        return render_template("recipe_result.html", title=title, steps=steps)
    return render_template("recipe_form.html")

@app.route('/')
def hello():
    return 'Hi, welcome to Recipe Generator, put /recipe/ behind url to get to the main page!'

if __name__ == "__main__":
    app.run(debug=True)