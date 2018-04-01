from flask import Flask, request, url_for, redirect, flash
from flask import render_template
from ingredients import Ingredients
from products import Products


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


@app.route('/products')
def products():
    product_instance = Products()
    data = product_instance.get_products()
    return render_template('products.html', products=data)


@app.route('/add_new_product', methods=['GET', 'POST'])
def add_new_product():
    if request.method == 'POST':
        name = request.form['product-name']
        cost = request.form['product-cost']
        product_ingredients = request.form['product-ingredients']

        product_instance = Products()
        product_instance.add_product(name, cost, product_ingredients)
        return redirect('/products')
    else:
        return render_template('add_new_product.html')


@app.route('/delete_product', methods=['GET', 'POST'])
def delete_product():
    if request.method == 'POST':
        name = request.form['product-name']

        product_instance = Products()
        product_instance.delete_product(name)
        return redirect('/products')
    else:
        return render_template('delete_product.html')


if __name__ == "__main__":
    app.run()

