from flask import Flask, request, url_for, redirect, flash
from flask import render_template
from ingredients import Ingredients

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home(name=None):
    return render_template('home.html', name=name)

@app.route('/ingredients')
def ingredients():
    ingredients_instance = Ingredients()
    data = ingredients_instance.get_ingredients()
    return render_template('ingredients.html', ingredients=data)

@app.route('/add_new_ingredient', methods=['GET', 'POST'])
def add_new_ingredient():
    if request.method == 'POST':
        name = request.form['ingredient-name']

        ingredients_instance = Ingredients()
        ingredients_instance.add_ingredient(name)
        return redirect('/ingredients')
    else:
        return render_template('add_new_ingredient.html')


@app.route('/delete_ingredient', methods=['GET', 'POST'])
def delete_ingredient():
    if request.method == 'POST':
        name = request.form['ingredient-name']

        ingredients_instance = Ingredients()
        ingredients_instance.delete_ingredient(name)
        return redirect('/ingredients')
    else:
        return render_template('delete_ingredient.html')

if __name__ == "__main__":
    app.run()