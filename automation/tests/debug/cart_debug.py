from playwright.sync_api import sync_playwright, expect
from automation.pages.login_page import LoginPage
from automation.pages.cart_page import CartPage

USERNAME = "standard_user"
PASSWORD = "secret_sauce"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
CART_URL = "https://www.saucedemo.com/cart.html"
CHECKOUT_STEP_ONE_URL = "https://www.saucedemo.com/checkout-step-one.html"


class SauceDemoCartDebug:
    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.cart_page = CartPage(page)

    def log(self, message: str):
        print(f"[DEBUG] {message}")

    def login(self):
        self.log("Opening login page with LoginPage.navigate()")
        self.login_page.navigate()
        self.login_page.login(USERNAME, PASSWORD)
        expect(self.page).to_have_url(INVENTORY_URL)
        self.log("Logged in successfully")

    def reset_app_state(self):
        self.log("Resetting app state")
        self.page.locator('#react-burger-menu-btn').click()
        self.page.locator('#reset_sidebar_link').click()
        self.page.locator('#react-burger-cross-btn').click()
        expect(self.page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)

    def go_to_inventory(self):
        self.page.goto(INVENTORY_URL)
        expect(self.page).to_have_url(INVENTORY_URL)

    def go_to_cart(self):
        self.cart_page.go_to_cart()
        expect(self.page).to_have_url(CART_URL)

    def get_inventory_items(self):
        return self.page.locator('.inventory_item')

    def get_inventory_item_name(self, index: int) -> str:
        return self.get_inventory_items().nth(index).locator('[data-test="inventory-item-name"]').inner_text().strip()

    def get_inventory_item_desc(self, index: int) -> str:
        return self.get_inventory_items().nth(index).locator('[data-test="inventory-item-desc"]').inner_text().strip()

    def get_inventory_item_price(self, index: int) -> str:
        return self.get_inventory_items().nth(index).locator('[data-test="inventory-item-price"]').inner_text().strip()

    def add_item_from_plp(self, index: int):
        if index == 0:
            name = self.get_inventory_item_name(0)
            self.log(f'Adding first item from PLP with CartPage: {name}')
            self.cart_page.add_first_item()
            return name

        name = self.get_inventory_item_name(index)
        self.log(f'Adding item from PLP: {name}')
        self.get_inventory_items().nth(index).locator('button').click()
        return name

    def remove_item_from_plp(self, index: int):
        name = self.get_inventory_item_name(index)
        self.log(f'Removing item from PLP: {name}')
        self.get_inventory_items().nth(index).locator('button').click()
        return name

    def open_pdp_from_plp(self, index: int):
        name = self.get_inventory_item_name(index)
        self.log(f'Opening PDP for: {name}')
        self.get_inventory_items().nth(index).locator('[data-test="inventory-item-name"]').click()
        expect(self.page).to_have_url(lambda url: 'inventory-item.html?id=' in url)
        return name

    def add_item_from_pdp(self):
        name = self.page.locator('[data-test="inventory-item-name"]').inner_text().strip()
        self.log(f'Adding item from PDP: {name}')
        self.page.locator('button', has_text='Add to cart').click()
        return name

    def remove_item_from_pdp(self):
        name = self.page.locator('[data-test="inventory-item-name"]').inner_text().strip()
        self.log(f'Removing item from PDP: {name}')
        self.page.locator('button', has_text='Remove').click()
        return name

    def back_to_products(self):
        self.log('Navigating back to PLP')
        self.page.locator('[data-test="back-to-products"]').click()
        expect(self.page).to_have_url(INVENTORY_URL)

    def get_cart_item_names(self):
        return [name.strip() for name in self.page.locator('[data-test="inventory-item-name"]').all_inner_texts()]

    def get_cart_badge_value(self):
        badge = self.page.locator('[data-test="shopping-cart-badge"]')
        return badge.inner_text().strip() if badge.count() else None

    def add_first_n_items_from_plp(self, count: int):
        added = []
        for i in range(count):
            added.append(self.add_item_from_plp(i))
        return added

    def add_all_items_from_pdp(self):
        added = []
        total = self.get_inventory_items().count()
        for i in range(total):
            self.go_to_inventory()
            name = self.open_pdp_from_plp(i)
            self.add_item_from_pdp()
            added.append(name)
            expected_badge = str(i + 1)
            actual_badge = self.get_cart_badge_value()
            self.log(f'Badge after add: expected {expected_badge}, actual {actual_badge}')
            assert actual_badge == expected_badge
            if i < total - 1:
                self.back_to_products()
        return added

    def remove_all_items_from_cart(self):
        buttons = self.page.locator('[data-test^="remove"]')
        while buttons.count() > 0:
            first_name = self.page.locator('[data-test="inventory-item-name"]').first.inner_text().strip()
            self.log(f'Removing from cart: {first_name}')
            buttons.first.click()
            buttons = self.page.locator('[data-test^="remove"]')


def run_test(page, title, fn):
    print(f"\n===== {title} =====")
    fn(page)
    print(f"[PASS] {title}")


def test_tc_cart_001(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    chosen_name = app.add_item_from_plp(0)
    app.go_to_cart()
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text(chosen_name)
    expect(page.locator('.cart_quantity')).to_have_text('1')
    expect(page.locator('[data-test="inventory-item-desc"]')).not_to_have_text('')


def test_tc_cart_002(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    chosen_name = app.open_pdp_from_plp(0)
    app.add_item_from_pdp()
    app.go_to_cart()
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text(chosen_name)
    expect(page.locator('.cart_quantity')).to_have_text('1')
    expect(page.locator('[data-test="inventory-item-desc"]')).not_to_have_text('')


def test_tc_cart_003(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    added = app.add_all_items_from_pdp()
    app.go_to_cart()
    expect(page.locator('.cart_item')).to_have_count(6)
    assert sorted(app.get_cart_item_names()) == sorted(added)
    expect(page.locator('button', has_text='Remove')).to_have_count(6)


def test_tc_cart_004(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    name = app.add_item_from_plp(0)
    app.go_to_cart()
    app.log(f'Removing single cart item: {name}')
    page.locator('button', has_text='Remove').click()
    expect(page.locator('.cart_item')).to_have_count(0)
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)


def test_tc_cart_005(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    app.add_first_n_items_from_plp(3)
    app.go_to_cart()
    app.remove_all_items_from_cart()
    expect(page.locator('.cart_item')).to_have_count(0)
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)


def test_tc_cart_006(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    app.add_item_from_plp(0)
    app.log('Removing first item from PLP')
    page.locator('#remove-sauce-labs-backpack').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)


def test_tc_cart_007(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    app.add_first_n_items_from_plp(6)
    for expected in ['5', '4', '3', '2', '1']:
        app.log(f'Expecting badge to become {expected} after remove')
        page.locator('button', has_text='Remove').first.click()
        expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text(expected)
    page.locator('button', has_text='Remove').first.click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)


def test_tc_cart_008(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    app.open_pdp_from_plp(0)
    app.add_item_from_pdp()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text('1')
    app.remove_item_from_pdp()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)


def test_tc_cart_009(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    app.go_to_cart()
    expect(page).to_have_url(CART_URL)
    expect(page.locator('.cart_item')).to_have_count(0)


def test_tc_cart_010(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    original_name = app.add_item_from_plp(0)
    app.go_to_cart()
    page.locator('[data-test="inventory-item-name"]').click()
    expect(page).to_have_url(lambda url: 'inventory-item.html?id=' in url)
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text(original_name)


def test_tc_cart_011(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    added = app.add_first_n_items_from_plp(6)
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text('6')
    expect(page.locator('button', has_text='Remove')).to_have_count(6)
    app.go_to_cart()
    assert sorted(app.get_cart_item_names()) == sorted(added)


def test_tc_cart_012(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    app.add_item_from_plp(0)
    app.go_to_cart()
    app.cart_page.click_checkout()
    expect(page).to_have_url(CHECKOUT_STEP_ONE_URL)
    expect(page.locator('[data-test="firstName"]')).to_be_visible()
    expect(page.locator('[data-test="lastName"]')).to_be_visible()
    expect(page.locator('[data-test="postalCode"]')).to_be_visible()
    expect(page.locator('[data-test="cancel"]')).to_be_visible()
    expect(page.locator('[data-test="continue"]')).to_be_visible()


def test_tc_cart_013(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    name = app.get_inventory_item_name(0)
    desc = app.get_inventory_item_desc(0)
    price = app.get_inventory_item_price(0)
    app.add_item_from_plp(0)
    app.go_to_cart()
    assert app.cart_page.get_cart_item_name().strip() == name
    expect(page.locator('[data-test="inventory-item-desc"]')).to_have_text(desc)
    expect(page.locator('[data-test="inventory-item-price"]')).to_have_text(price)
    expect(page.locator('button', has_text='Remove')).to_be_visible()


def test_tc_cart_014(page):
    app = SauceDemoCartDebug(page)
    app.login()
    app.reset_app_state()
    app.add_item_from_plp(0)
    app.go_to_cart()
    page.locator('[data-test="continue-shopping"]').click()
    expect(page).to_have_url(INVENTORY_URL)
    expect(page.locator('.inventory_item')).to_have_count(6)


if __name__ == '__main__':
    tests = [
        ("TC_CART_001 Add item from PLP", test_tc_cart_001),
        ("TC_CART_002 Add item from PDP", test_tc_cart_002),
        ("TC_CART_003 Add multiple items from PDP", test_tc_cart_003),
        ("TC_CART_004 Remove a single item from the cart", test_tc_cart_004),
        ("TC_CART_005 Remove multiple items from the cart", test_tc_cart_005),
        ("TC_CART_006 Remove a single item from the cart via PLP", test_tc_cart_006),
        ("TC_CART_007 Remove multiple items from the cart via PLP", test_tc_cart_007),
        ("TC_CART_008 Remove item from the cart via PDP", test_tc_cart_008),
        ("TC_CART_009 Accessing the cart when empty", test_tc_cart_009),
        ("TC_CART_010 Verify PDP can be accessed from cart", test_tc_cart_010),
        ("TC_CART_011 Add multiple items to the cart from the PLP", test_tc_cart_011),
        ("TC_CART_012 Verify navigation to checkout from cart", test_tc_cart_012),
        ("TC_CART_013 Verify item displays properly in cart", test_tc_cart_013),
        ("TC_CART_014 Verify navigation back to PLP from cart", test_tc_cart_014),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        for title, test_fn in tests:
            run_test(page, title, test_fn)
        browser.close()
