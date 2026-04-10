# cart_page.py

class CartPage:
    def __init__(self, page):
        self.page = page
        # Locators
        self.cart_icon = "a.shopping_cart_link"
        self.first_item_add_button = "#add-to-cart-sauce-labs-backpack"
        self.cart_item_name = ".inventory_item_name"
        self.checkout_button = "#checkout"

    # Navigate to cart (if needed)
    def go_to_cart(self):
        self.page.click(self.cart_icon)

    # Add first item to cart
    def add_first_item(self):
        self.page.click(self.first_item_add_button)

    # Get cart item name (for assertion)
    def get_cart_item_name(self):
        return self.page.inner_text(self.cart_item_name)

    # Proceed to checkout
    def click_checkout(self):
        self.page.click(self.checkout_button)