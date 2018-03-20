from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home(name=None):
    return render_template('home.html', name=name)

@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html')

if __name__ == "__main__":
    app.run()