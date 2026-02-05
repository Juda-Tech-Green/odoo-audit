# app.py

from flask import Flask, render_template
from analysis.metrics import (
    total_products,
    products_per_company,
    products_per_category,
    empty_categories
)
from analysis.quality_checks import (
    find_products_without_category,
    find_products_by_company,
    find_products_without_channels,
    find_products_only_pos,
    find_products_only_web,
    find_duplicate_category_names
)

app = Flask(__name__)


@app.route("/")
@app.route("/overview")
def overview():
    return render_template(
        "overview.html",
        total_products=total_products(),
        total_categories=len(find_duplicate_category_names()[1]),
        products_per_company=products_per_company(),
        products_per_category=products_per_category(),
        empty_categories=empty_categories(),
        products_without_channels=find_products_without_channels(),
        products_only_pos=find_products_only_pos(),
        products_only_web=find_products_only_web()
    )

@app.route("/products")
def products():
    return render_template(
        "products.html",
        products_without_category=find_products_without_category(),
        products_by_company=find_products_by_company(),
        products_without_channels=find_products_without_channels(),
        products_only_pos=find_products_only_pos(),
        products_only_web=find_products_only_web()
    )


if __name__ == "__main__":
    app.run(debug=True)
