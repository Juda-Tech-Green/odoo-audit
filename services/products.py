# services/products.py

from odoo_client import OdooClient

odoo = OdooClient()

def get_all_products(batch=200):
    all_products = []
    offset = 0

    while True:
        products = odoo.search_read(
            model="product.template",
            domain=[],
            fields=[
                "id", "name", "categ_id",
                "company_id", "active",
                "available_in_pos",
                "website_published"
            ],
            limit=batch,
            offset=offset
        )

        if not products:
            break

        all_products.extend(products)
        offset += batch

    return all_products
