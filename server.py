from flask import Flask, render_template, jsonify

app = Flask(__name__)

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
    pid = int(pid)
    if pid in products:
        return render_template("product.html", name=products[pid], pid=pid)
    else:
        return "Error 404: Not Found"
    

@app.route("/api/products")
def api_products():
    return jsonify(products)