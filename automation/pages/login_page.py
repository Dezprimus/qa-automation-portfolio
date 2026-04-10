class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")

    def get_error_message(self):
        return self.page.locator("[data-test='error']") 

    def click_login(self):
        self.page.click("[data-test='login-button']")