from flask import Flask, request, url_for, redirect, flash
from flask import render_template
from suppliers import Suppliers
from ingredients import Ingredients
from products import Products
from transactions import Transactions
from login import Login
from employee import Employees
from locations import Locations


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['employee-name']
        number = request.form['employee-number']

        login_instance = Login()
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

@app.route('/employees')
def employees():
    employee_instance = Employees()
    data = employee_instance.get_employees()
    return render_template('employees.html', employees=data)


@app.route('/add_new_employee', methods=['GET', 'POST'])
def add_new_employee():
    if request.method == 'POST':
        name = request.form['employee-name']
        id = request.form['employee-id']
        wage = request.form['employee-wage']
        status = request.form['employee-status']
        location = request.form['employee-location']

        employee_instance = Employees()
        employee_instance.add_employee(name, id, wage, status, location)
        return redirect('/employees')
    else:
        return render_template('add_new_employee.html')


@app.route('/delete_employee', methods=['GET', 'POST'])
def delete_employee():
    if request.method == 'POST':
        id = request.form['employee-id']
        print(id)
        print(type(str(id)))

        employee_instance = Employees()
        employee_instance.delete_employee(id)
        return redirect('/employees')
    else:
        return render_template('delete_employee.html')

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

