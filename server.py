from flask import Flask, render_template, jsonify, request
import db

app = Flask(__name__)

db.create_db()

products = {
    1: "Mouse",
    2: "Keyboard",
    3: "Monitor",
    4: "Laptop"
}

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/product/<pid>")
def product(pid):
    product = db.get_product(pid)
    return render_template("product.html", product=product)
    

@app.route("/api/products")
def api_products():
    products = db.get_all_products()
    products_list = []
    for product in products:
        products_list.append(product.serialize())
    return jsonify(products_list)


@app.route("/add/product")
def add_product():
    return render_template("add_product.html")


@app.route("/add/product", methods=['POST'])
def do_add_product():
    data = request.form
    print(data['name'], data['price'])
    db.add_new_product(data['name'], data['price'])
    return render_template("done.html")