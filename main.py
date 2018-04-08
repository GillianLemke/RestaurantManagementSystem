from flask import Flask, request, url_for, redirect, flash
from flask import render_template
from products import Products
from locations import Locations


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


@app.route('/add_new_product', methods=['GET', 'POST'])
def add_new_product():
    if request.method == 'POST':
        name = request.form['product-name']
        cost = request.form['product-cost']
        ingredients = request.form['product-ingredients']

        product_instance = Products()
        product_instance.add_product(name, cost, ingredients)
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


@app.route('/locations')
def locations():
    location_instance = Locations()
    data = location_instance.get_locations()
    return render_template('locations.html', locations=data)


@app.route('/add_new_location', methods=['GET', 'POST'])
def add_new_location():
    if request.method == 'POST':
        address = request.form['location-address']
        type = request.form['location-type']
        hours = request.form['location-hours']
        manager = request.form['location-manager']

        location_instance = Locations()
        location_instance.add_location(address, type, hours, manager)
        return redirect('/locations')
    else:
        return render_template('add_new_location.html')


@app.route('/delete_location', methods=['GET', 'POST'])
def delete_location():
    if request.method == 'POST':
        address = request.form['location-address']

        location_instance = Locations()
        location_instance.delete_location(address)
        return redirect('/locations')
    else:
        return render_template('delete_location.html')


if __name__ == "__main__":
    app.run()
