from flask import Flask
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

@app.route('/suppliers')
def suppliers():
    return render_template('suppliers.html')

if __name__ == "__main__":
    app.run()