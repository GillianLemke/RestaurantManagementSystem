from flask import Flask, request, url_for, redirect, flash
from flask import render_template
from suppliers import Suppliers
from products import Products


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def home(name=None):
    return render_template('home.html', name=name)

@app.route('/suppliers')
def suppliers():
    suppliers_instance = Suppliers()
    data = suppliers_instance.get_suppliers()
    return render_template('suppliers.html', suppliers=data)

@app.route('/add_new_supplier', methods=['GET', 'POST'])
def add_new_supplier():
    if request.method == 'POST':
        name = request.form['supplier-name']
        contact_name = request.form['supplier-contact-name']
        contact_phone = request.form['supplier-contact-phone']

        suppliers_instance = Suppliers()
        suppliers_instance.add_supplier(name, contact_name, contact_phone)
        return redirect('/suppliers')
    else:
        return render_template('add_new_supplier.html')

@app.route('/delete_supplier', methods=['GET', 'POST'])
def delete_supplier():
    if request.method == 'POST':
        name = request.form['supplier-name']

        suppliers_instance = Suppliers()
        suppliers_instance.delete_supplier(name)
        return redirect('/suppliers')
    else:
        return render_template('delete_supplier.html')

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
        name = request.form['supplier-name']

        product_instance = Products()
        product_instance.delete_product(name)
        return redirect('/products')
    else:
        return render_template('delete_product.html')


if __name__ == "__main__":
    app.run()

