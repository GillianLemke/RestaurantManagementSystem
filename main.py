from flask import Flask
from flask import render_template
from suppliers import Suppliers

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home(name=None):
    return render_template('home.html', name=name)

@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html')

@app.route('/suppliers')
def suppliers():
    suppliers_instance = Suppliers()
    data = suppliers_instance.get_suppliers()
    return render_template('suppliers.html', suppliers=data)

if __name__ == "__main__":
    app.run()