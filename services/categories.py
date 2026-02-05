# services/categories.py

from odoo_client import OdooClient

odoo = OdooClient()

def get_all_categories():
    """
    Retorna todas las categorías de productos
    """
    categories = odoo.search_read(
        model="product.category",
        domain=[],
        fields=["id", "name", "parent_id"]
    )

    return categories


if __name__ == "__main__":
    cats = get_all_categories()
    for c in cats:
        print(c)
