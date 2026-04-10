import pytest
from automation.pages.login_page import LoginPage


def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in page.url


def test_invalid_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "wrong_password")

    error = login.get_error_message()
    assert error.is_visible()


def test_invalid_username(page):
    login = LoginPage(page)
    login.navigate()
    login.login("invalid_user", "secret_sauce")

    error = login.get_error_message()
    assert error.is_visible()
    assert "do not match any user" in error.inner_text()


def test_empty_user_pass(page):
    login = LoginPage(page)
    login.navigate()
    login.click_login()

    error = login.get_error_message()
    assert error.is_visible()
    assert "Username is required" in error.inner_text()


def test_empty_username(page):
    login = LoginPage(page)
    login.navigate()
    login.login("", "secret_sauce")

    error = login.get_error_message()
    assert error.is_visible()
    assert "Username is required" in error.inner_text()


def test_empty_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "")

    error = login.get_error_message()
    assert error.is_visible()
    assert "Password is required" in error.inner_text()


def test_locked_out_user(page):
    login = LoginPage(page)
    login.navigate()
    login.login("locked_out_user", "secret_sauce")

    error = login.get_error_message()
    assert error.is_visible()
    assert "Sorry, this user has been locked out" in error.inner_text()