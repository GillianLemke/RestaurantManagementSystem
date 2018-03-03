from flask import Flask, request, url_for, redirect
from flask import render_template
from products import Products

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home(name=None):
    return render_template('home.html', name=name)


@app.route('/products')
def products():
    product_instance = Products()
    data = product_instance.get_products()
    return render_template('products.html', products=data)

@app.route('/add_new_product')
def add_new_product():
    return render_template('add_new_product.html')
