# Desmond's QA  Portfolio

## 📌 Project Overview
This project is a QA Automation practice framework built using SauceDemo as the application under test. It demonstrates core QA skills including manual test design, UI automation planning, Page Object Model (POM) structure, and debugging-oriented test development.

The goal of this project is to simulate real-world QA workflows including test case design, automation structure, and defect reporting.

---

# 📁 Folder Structure

QA-Portfolio-Practice/
- `automation/config` -> Constants containing resuable data such as URLS and user accounts
- `automation/pages` -> Page fills where locators and functions are stored
- `automation/tests/pytest` -> Test scripts
- `automation/tests/debug` -> Debug versions of the test scripts 
- `bug-reports/` -> Screenshots of bug reports
- `test-cases/` -> Test cases for login and cart
- `test-plans/` Test plan for project detail strategy, objective and more

---

# 🛠 Tech Stack

Python  
Playwright (UI automation)  
Pytest (test framework)  
Page Object Model (POM)  
Git & GitHub (version control)

---

# 🧠 Page Object Model (POM)

This framework follows the Page Object Model (POM) design pattern.

Why POM is used:
- Separates test logic from UI selectors
- Improves maintainability
- Reduces duplication
- Makes tests easier to debug and scale

Structure:
- pages/login_page.py → handles login actions and selectors
- pages/cart_page.py → handles cart interactions

---

# 📦 Constants Usage

Test data is centralized in constants/test_data.py

Purpose:
- Stores usernames and passwords
- Avoids hardcoding values inside tests
- Improves reusability and maintainability

Example credentials:
- standard_user
- secret_sauce

---

# 🔐 Login Test Scenarios

Coverage:
- Valid login
- Invalid password login
- Invalid username login
- Empty fields validation
- Locked-out user validation

---

## ✔️ Test Case: Valid Login

Precondition: User is on SauceDemo login page  

Steps:
1. Enter valid username (standard_user)
2. Enter valid password (secret_sauce)
3. Click Login button  

Expected Result:
User is redirected to Inventory page and products are visible

---

## ❌ Test Case: Invalid Password Login

Precondition: User is on SauceDemo login page  

Steps:
1. Enter valid username (standard_user)
2. Enter invalid password
3. Click Login button  

Expected Result:
Error message is displayed: “Epic sadface: Username and password do not match any user in this service.”  
User remains on login page

---

# 🛒 Cart Test Scenarios

Coverage:
- Add item to cart
- Remove item from cart
- View cart with items
- View empty cart state

---

## ✔️ Add Item to Cart

User selects product from inventory  
Product appears in cart badge  
Item is visible in cart page  

---

## ❌ Empty Cart State

User navigates to cart without adding items  
Cart displays empty state  
No items shown  

---

# 🐞 Bug Reporting

Bug reports include:
- Title
- Environment
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Screenshots

---

## 📸 Screenshots

Stored in:
bugs/screenshots/

Used for:
- UI failure evidence
- Debug test documentation

---

# 🧪 Debug Test Files

- debug_test_login.py
- debug_test_cart.py

Purpose:
- Step-by-step debugging
- Validate selectors and flows
- Stabilize automation before POM refactor

---

# 🧪 Test Strategy

1. Manual test case design
2. Debug automation tests
3. Clean POM-based automation
4. Pytest execution

---

# ▶️ How to Run

pip install -r requirements.txt  
pytest

---

# 📊 Future Improvements

- GitHub Actions CI/CD
- HTML reporting (pytest-html)
- Expanded test coverage
- Data-driven testing
- Enhanced POM structure

---

# 👨‍💻 Author Notes

This project demonstrates:
- QA test design thinking
- UI automation using Playwright
- Debugging and test refinement
- Framework structuring using POM
