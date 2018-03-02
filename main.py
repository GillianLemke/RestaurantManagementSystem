from flask import Flask
from flask import render_template
from products import Products

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home(name=None):
    return render_template('home.html', name=name)


@app.route('/products')
def products():
    # data = Products.get_products()
    data = [
        {'name': 'banana', 'cost': 2.22, 'ingredients': 'none'},
        {'name': 'apple', 'cost': 2.22, 'ingredients': 'none'},
        {'name': 'orange', 'cost': 2.22, 'ingredients': 'none'},
    ]
    return render_template('products.html', products=data)
