import re
import pytest
from playwright.sync_api import Page, expect
from automation.pages.login_page import LoginPage
from automation.pages.cart_page import CartPage
from automation.config.constants import STANDARD_USER, PASSWORD, INVENTORY_URL, CART_URL, CHECKOUT_STEP_ONE_URL

@pytest.fixture
def logged_in_page(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(STANDARD_USER, PASSWORD)
    expect(page).to_have_url(INVENTORY_URL)

    page.locator('#react-burger-menu-btn').click()
    page.locator('#reset_sidebar_link').click()
    page.locator('#react-burger-cross-btn').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)
    return page


def inventory_items(page: Page):
    return page.locator('.inventory_item')


def inventory_name(page: Page, index: int) -> str:
    return inventory_items(page).nth(index).locator('[data-test="inventory-item-name"]').inner_text().strip()


def inventory_desc(page: Page, index: int) -> str:
    return inventory_items(page).nth(index).locator('[data-test="inventory-item-desc"]').inner_text().strip()


def inventory_price(page: Page, index: int) -> str:
    return inventory_items(page).nth(index).locator('[data-test="inventory-item-price"]').inner_text().strip()


def add_from_plp(page: Page, index: int) -> str:
    cart_page = CartPage(page)
    if index == 0:
        name = inventory_name(page, 0)
        cart_page.add_first_item()
        return name

    name = inventory_name(page, index)
    inventory_items(page).nth(index).locator('button', has_text='Add to cart').click()
    return name


def open_pdp(page: Page, index: int) -> str:
    name = inventory_name(page, index)
    inventory_items(page).nth(index).locator('[data-test="inventory-item-name"]').click()
    expect(page).to_have_url(re.compile(r"inventory-item\.html\?id="))
    return name


def add_from_pdp(page: Page) -> str:
    name = page.locator('[data-test="inventory-item-name"]').inner_text().strip()
    page.locator('button', has_text='Add to cart').click()
    return name


def go_to_cart(page: Page):
    cart_page = CartPage(page)
    cart_page.go_to_cart()
    expect(page).to_have_url(CART_URL)


def get_cart_names(page: Page):
    return [name.strip() for name in page.locator('[data-test="inventory-item-name"]').all_inner_texts()]


def add_first_n_from_plp(page: Page, count: int):
    names = []
    for i in range(count):
        names.append(add_from_plp(page, i))
    return names


def add_all_from_pdp(page: Page):
    names = []
    total = inventory_items(page).count()
    for i in range(total):
        page.goto(INVENTORY_URL)
        name = open_pdp(page, i)
        add_from_pdp(page)
        names.append(name)
        expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text(str(i + 1))
        if i < total - 1:
            page.locator('[data-test="back-to-products"]').click()
    return names


def test_tc_cart_001_add_item_from_plp(logged_in_page: Page):
    page = logged_in_page
    chosen_name = add_from_plp(page, 0)
    go_to_cart(page)
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text(chosen_name)
    expect(page.locator('.cart_quantity')).to_have_text('1')
    expect(page.locator('[data-test="inventory-item-desc"]')).not_to_have_text('')


def test_tc_cart_002_add_item_from_pdp(logged_in_page: Page):
    page = logged_in_page
    chosen_name = open_pdp(page, 0)
    add_from_pdp(page)
    go_to_cart(page)
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text(chosen_name)
    expect(page.locator('.cart_quantity')).to_have_text('1')
    expect(page.locator('[data-test="inventory-item-desc"]')).not_to_have_text('')


def test_tc_cart_003_add_multiple_items_from_pdp(logged_in_page: Page):
    page = logged_in_page
    added = add_all_from_pdp(page)
    go_to_cart(page)
    expect(page.locator('.cart_item')).to_have_count(6)
    assert sorted(get_cart_names(page)) == sorted(added)
    expect(page.locator('button', has_text='Remove')).to_have_count(6)


def test_tc_cart_004_remove_single_item_from_cart(logged_in_page: Page):
    page = logged_in_page
    add_from_plp(page, 0)
    go_to_cart(page)
    page.locator('button', has_text='Remove').click()
    expect(page.locator('.cart_item')).to_have_count(0)
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)


def test_tc_cart_005_remove_multiple_items_from_cart(logged_in_page: Page):
    page = logged_in_page
    add_first_n_from_plp(page, 3)
    go_to_cart(page)
    while page.locator('button', has_text='Remove').count() > 0:
        page.locator('button', has_text='Remove').first.click()
    expect(page.locator('.cart_item')).to_have_count(0)
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)


def test_tc_cart_006_remove_single_item_via_plp(logged_in_page: Page):
    page = logged_in_page
    add_from_plp(page, 0)
    page.locator('#remove-sauce-labs-backpack').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)


def test_tc_cart_007_remove_multiple_items_via_plp(logged_in_page: Page):
    page = logged_in_page
    add_first_n_from_plp(page, 6)
    for expected in ['5', '4', '3', '2', '1']:
        page.locator('button', has_text='Remove').first.click()
        expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text(expected)
    page.locator('button', has_text='Remove').first.click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)


def test_tc_cart_008_remove_item_via_pdp(logged_in_page: Page):
    page = logged_in_page
    open_pdp(page, 0)
    add_from_pdp(page)
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text('1')
    page.locator('button', has_text='Remove').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)


def test_tc_cart_009_access_empty_cart(logged_in_page: Page):
    page = logged_in_page
    go_to_cart(page)
    expect(page.locator('.cart_item')).to_have_count(0)


def test_tc_cart_010_open_pdp_from_cart(logged_in_page: Page):
    page = logged_in_page
    chosen_name = add_from_plp(page, 0)
    go_to_cart(page)
    page.locator('[data-test="inventory-item-name"]').click()
    expect(page).to_have_url(re.compile(r"inventory-item\.html\?id="))
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text(chosen_name)


def test_tc_cart_011_add_multiple_items_from_plp(logged_in_page: Page):
    page = logged_in_page
    added = add_first_n_from_plp(page, 6)
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text('6')
    expect(page.locator('button', has_text='Remove')).to_have_count(6)
    go_to_cart(page)
    assert sorted(get_cart_names(page)) == sorted(added)


def test_tc_cart_012_navigate_to_checkout_from_cart(logged_in_page: Page):
    page = logged_in_page
    cart_page = CartPage(page)
    add_from_plp(page, 0)
    go_to_cart(page)
    cart_page.click_checkout()
    expect(page).to_have_url(CHECKOUT_STEP_ONE_URL)
    expect(page.locator('[data-test="firstName"]')).to_be_visible()
    expect(page.locator('[data-test="lastName"]')).to_be_visible()
    expect(page.locator('[data-test="postalCode"]')).to_be_visible()
    expect(page.locator('[data-test="cancel"]')).to_be_visible()
    expect(page.locator('[data-test="continue"]')).to_be_visible()


def test_tc_cart_013_verify_item_displays_properly_in_cart(logged_in_page: Page):
    page = logged_in_page
    cart_page = CartPage(page)
    name = inventory_name(page, 0)
    desc = inventory_desc(page, 0)
    price = inventory_price(page, 0)
    add_from_plp(page, 0)
    go_to_cart(page)
    assert cart_page.get_cart_item_name().strip() == name
    expect(page.locator('[data-test="inventory-item-desc"]')).to_have_text(desc)
    expect(page.locator('[data-test="inventory-item-price"]')).to_have_text(price)
    expect(page.locator('button', has_text='Remove')).to_be_visible()


def test_tc_cart_014_continue_shopping_from_cart(logged_in_page: Page):
    page = logged_in_page
    add_from_plp(page, 0)
    go_to_cart(page)
    page.locator('[data-test="continue-shopping"]').click()
    expect(page).to_have_url(INVENTORY_URL)
    expect(page.locator('.inventory_item')).to_have_count(6)
