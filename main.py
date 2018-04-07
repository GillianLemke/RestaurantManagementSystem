from flask import Flask, request, url_for, redirect, flash
from flask import render_template
from products import Products
from transactions import Transactions


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

@app.route('/transactions')
def transactions():
    transaction_instance = Transactions()
    data = transaction_instance.get_transactions()
    return render_template('transactions.html', transactions=data)

@app.route('/add_new_transaction', methods=['GET', 'POST'])
def add_new_transaction():
    if request.method == 'POST':
        name = request.form['transaction-name']
        cost = request.form['transaction-cost']
        ingredients = request.form['transaction-ingredients']

        transaction_instance = Transactions()
        transaction_instance.add_transaction(name, cost, ingredients)
        return redirect('/transactions')
    else:
        return render_template('add_new_transaction.html')

@app.route('/delete_transaction', methods=['GET', 'POST'])
def delete_transaction():
    if request.method == 'POST':
        name = request.form['transcation-name']

        transaction_instance = Transactions()
        transaction_instance.delete_transaction(name)
        return redirect('/transactions')
    else:
        return render_template('delete_transaction.html')

if __name__ == "__main__":
    app.run()
