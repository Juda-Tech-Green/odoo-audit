# analysis/metrics.py

from services.products import get_all_products
from services.categories import get_all_categories
from collections import defaultdict

def total_products():
    return len(get_all_products())


def products_per_company():
    products = get_all_products()
    by_company = defaultdict(int)

    for p in products:
        company = p["company_id"][1] if p["company_id"] else "Sin empresa"
        by_company[company] += 1

    return dict(by_company)


def products_per_category():
    products = get_all_products()
    by_category = defaultdict(int)

    for p in products:
        category = p["categ_id"][1] if p["categ_id"] else "Sin categoría"
        by_category[category] += 1

    return dict(by_category)

def empty_categories():
    categories = get_all_categories()
    products = get_all_products()

    used = set()
    for p in products:
        if p["categ_id"]:
            used.add(p["categ_id"][0])

    empties = [c for c in categories if c["id"] not in used]
    return empties


if __name__ == "__main__":
    print("Total productos:", total_products())
    print("\nProductos por empresa:")
    for k,v in products_per_company().items():
        print(k, v)

    print("\nCategorías vacías:")
    for c in empty_categories():
        print(c["name"])

