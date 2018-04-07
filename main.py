from flask import Flask, request, url_for, redirect, flash
from flask import render_template
from products import Products
from login import Login


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        print('in post')
        name = request.form['employee-name']
        number = request.form['employee-number']

        print(name, number)
        login_instance = Login()
        print(login_instance.login_success(name, number))
        if login_instance.login_success(name, number):
            return render_template('home.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


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


if __name__ == "__main__":
    app.run()
