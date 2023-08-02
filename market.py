from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///markets.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    barcode = db.Column(db.String(10), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False, unique=True)
    description = db.Column(db.String(1000), nullable=False, unique=True)

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'ID': 1, 'Name': 'Laptop', 'Barcode': 100000002, 'Price': 22000},
        {'ID': 2, 'Name': 'Phone', 'Barcode': 100000003, 'Price': 11500},
        {'ID': 3, 'Name': 'Mouse', 'Barcode': 100000004, 'Price': 2000}
    ]
    return render_template('market.html', items=items)

@app.route('/about/<user>')
def about(user):
    return f'<h1>Hello {user}!</h1>'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)