# analysis/quality_checks.py

from services.categories import get_all_categories
from services.products import get_all_products
from collections import defaultdict

def find_duplicate_category_names():
    categories = get_all_categories()
    by_name = defaultdict(list)

    for c in categories:
        by_name[c["name"].strip().lower()].append(c)

    duplicates = {
        name: items
        for name, items in by_name.items()
        if len(items) > 1
    }

    return [duplicates, categories]


def find_category_tree_depth():
    categories = get_all_categories()
    parents = {c["id"]: c["parent_id"][0] if c["parent_id"] else None for c in categories}

    def depth(cat_id):
        d = 0
        while parents.get(cat_id):
            cat_id = parents[cat_id]
            d += 1
        return d

    depths = {c["name"]: depth(c["id"]) for c in categories}
    return depths


def find_products_without_category():
    products = get_all_products()
    return [p for p in products if not p["categ_id"]]


def find_products_by_company():
    products = get_all_products()
    by_company = defaultdict(list)

    for p in products:
        company = p["company_id"][1] if p["company_id"] else "Sin empresa"
        by_company[company].append(p)

    return by_company

def find_products_without_channels():
    """
    Productos que no están ni en POS ni en Web
    """
    products = get_all_products()
    return [
        p for p in products
        if not p.get("available_in_pos") and not p.get("website_published")
    ]


def find_products_only_pos():
    """
    Productos que solo están en POS
    """
    products = get_all_products()
    return [
        p for p in products
        if p.get("available_in_pos") and not p.get("website_published")
    ]


def find_products_only_web():
    """
    Productos que solo están en Web
    """
    products = get_all_products()
    return [
        p for p in products
        if not p.get("available_in_pos") and p.get("website_published")
    ]



if __name__ == "__main__":
    duplicates = find_duplicate_category_names()
    jerarquia = find_category_tree_depth()
    products_without_category = find_products_without_category()
    products_by_company = find_products_by_company()
    print(products_by_company.values())
    """
    for name, items in duplicates.items():
        print(f"\nCategoría duplicada: {name}")
        for c in items:
            print(c)
    """

