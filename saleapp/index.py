from flask import render_template, request

from saleapp import app, dao


@app.route("/")
def index():
    categories = dao.load_categories()
    products = dao.load_products(category_id=request.args.get("category_id"),
                                 kw=request.args.get("keyword"),
                                 #pr=request.args.get("price")
                                 )
    return render_template("index.html",
                           categories=categories,
                           products=products)


@app.route("/products_detail")
def product_detail():
    return render_template("products_detail.html")


if __name__ == '__main__':
    app.run(debug=True)
