import pandas as pd

from app.database import DATABASE
from app.models import Product


class StockChecker:

    database = pd.DataFrame(DATABASE)

    async def is_product_available(self, product: Product) -> bool:
        from app.main import cache

        """
        Check if a product has stock in the DataFrame.

        Args:
        - product_name: Name of the product to check.
        - quantity: stock wanted.

        Returns:
        - True if the product has stock, False otherwise.
        """
        cache_key = f"{product.product_name}__{product.quantity}"
        cached_product = cache.get(cache_key)
        if cached_product is not None:
            # If the client has ask for the same product more than three times, raise an error.
            if cached_product[1] > 3:
                raise Exception("too many requests")
            return cached_product[0]

        product_row = self.database[
            self.database["product_name"] == product.product_name
        ]

        has_stock = (
            False
            if product_row.empty
            else product_row["quantity"].item() >= product.quantity
        )
        cache.set(cache_key, has_stock)
        return has_stock
