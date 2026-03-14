## **Objective**

The objective of this test plan is to verify that the core user workflows (**happy path)** on the Sauce Demo website function correctly and meet expected behavior. Testing will validate that users can log in, browse inventory, manage their cart, and complete checkout without functional defects.

---

## **Test Scope**

Testing will focus on the primary e-commerce workflows available on the site.

**Features Included in Testing:**

* Login functionality (valid and invalid credentials)  
* Menu navigation  
* Item sorting functionality  
* Adding and removing items from the cart  
* Cart page functionality  
* Checkout process

These features represent the main user journey from login through order completion.

---

## **Out of Scope**

The following items will not be included in testing:

* Backend database validation  
* Performance or load testing  
* Security testing  
* API testing  
* Mobile device compatibility testing  
* Integration with external payment systems

Testing will focus strictly on **front-end functional testing** of the application.

---

## **Test Strategy**

Testing will primarily be conducted using **manual functional testing** techniques. Test cases will be designed to validate positive and negative user scenarios across the main workflows.

Additional testing methods include:

* Exploratory testing to identify unexpected defects  
* Regression testing to ensure existing functionality remains stable after changes

Automation testing may also be introduced using **Playwright** for repeated user flows such as login and checkout.

*(Since you're learning Playwright, this aligns well with your automation goals.)*

---

## **Test Environment**

Testing will be performed in the following environment:

* **Application:** Sauce Demo  
* **URL:** https://www.saucedemo.com  
* **Browser:** Google Chrome (latest version)  
* **Operating System:** Windows 10 / Windows 11  
* **Testing Type:** Manual functional testing

Test accounts provided by the application will be used for authentication.

---

## **Entry / Exit Criteria**

### **Entry Criteria**

Testing will begin when:

* The test environment is accessible  
* Test data and user credentials are available  
* Test cases have been reviewed and approved  
* The application build is stable enough for testing

  ### **Exit Criteria**

Testing will conclude when:

* All planned test cases have been executed  
* Critical and high-priority defects have been resolved or documented  
* No blocking defects remain  
* Test results have been documented and reviewed