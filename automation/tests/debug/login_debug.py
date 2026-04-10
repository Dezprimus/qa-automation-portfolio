import pytest
from playwright.sync_api import sync_playwright
from automation.pages.login_page import LoginPage

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "secret_sauce")

        assert "inventory" in page.url

        browser.close()

def test_invalid_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "wrong_password")

        error = page.locator("[data-test='error']")
        assert error.is_visible()

        browser.close()

def test_invalid_username():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login = LoginPage(page)
        login.navigate()
        login.login("invalid_user", "secret_sauce")

        error = login.get_error_message()
        
        assert error.is_visible()
        assert "do not match any user" in error.inner_text()

        browser.close()

def test_empty_user_pass():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login = LoginPage(page)
        login.navigate()
        login.click_login()

        error = login.get_error_message()

        assert error.is_visible()
        assert "Username is required" in error.inner_text()

        browser.close()

def test_empty_username():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login = LoginPage(page)
        login.navigate()
        login.login("", "secret_sauce")

        error = login.get_error_message()

        assert error.is_visible()
        assert "Username is required" in error.inner_text()

        browser.close()

def test_empty_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login = LoginPage(page)
        login.navigate()
        login.login("standard_user", "")

        error = login.get_error_message()

        assert error.is_visible()
        assert "Password is required" in error.inner_text()

        browser.close()

def test_locked_out_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login = LoginPage(page)
        login.navigate()
        login.login("locked_out_user", "secret_sauce")

        error = login.get_error_message()

        assert error.is_visible()
        assert "Sorry, this user has been locked out" in error.inner_text()

        browser.close()        