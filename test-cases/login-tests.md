# Sauce Demo Login Test Cases

# Focus: Login Functionality

## Test Scenarios

1. User logs in with valid credentials  
2. User attempts to log in with an invalid password  
3. User attempts to log in with an invalid username  
4. User attempts to log in with empty fields (Username \+ Password)  
5. User attempts to log in with an empty field (Username)  
6. User attempts to log in with an empty field (Password)  
7. Locked-out user attempts login  
   

## Test Cases:

### ***Test Case ID:** TC\_LOGIN\_001:* 

### ***Title:** User logs in with valid credentials*

* **Precondition**:  
  * User is navigated to the login page  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/](https://www.saucedemo.com/)     
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Enter a valid username (standard\_user) in the Username field  
  2. Enter a valid password (secret\_sauce) in the Password field  
  3. Click the Login button

**Expected Result**: 

* User is successfully logged in   
* Redirected to PLP 


### ***Test Case ID:** TC\_LOGIN\_002:* 

### ***Title:** User attempts to log in with an invalid password*

* **Precondition**:   
  * User is navigated to the login page  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/](https://www.saucedemo.com/)   
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps:**  
  1. Enter a valid username (standard\_user) in the Username field  
  2. Enter an invalid password in the Password field  
  3. Click the Login button

**Expected Result**: 

* An error message is displayed stating “Epic sadface: Username and password do not match any user in this service.”   
* User remains on the login page

### ***Test Case ID:** TC\_LOGIN\_003:*

### ***Title:*** *User attempts to log in with an invalid username*

* **Precondition**:   
  * User is navigated to the login page  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/](https://www.saucedemo.com/)   
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps:**  
  1. Enter an invalid username  
  2. Enter a valid password (secret\_sauce) in the Password field  
  3. Click the Login button

**Expected Result:** 

* An error message is displayed stating, “Epic sadface: Username and password do not match any user in this service.”   
* User remains on the login page.

### ***Test Case ID:** TC\_LOGIN\_004:*

### ***Title:*** *User attempts to log in with empty fields (Username \+ Password)*

* **Precondition**:   
  * User is navigated to the login page	  
* **Test Data:**  
  * **URL:** https://www.saucedemo.com/  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps:**  
  1. Click the Login button

**Expected Result:** 

* An error message is displayed stating “Epic sadface: Username is required”.   
* User remains on the login page. 

### ***Test Case ID:** TC\_LOGIN\_005:*

### ***Title:*** *User attempts to log in with an empty field (Username)*

* **Precondition**:   
  * User is navigated to the login page  
* **Test Data:**  
  * **URL:** https://www.saucedemo.com/  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps:**  
  1. Enter a valid password (secret\_sauce) in the Password field  
  2. Click the Login button

**Expected Result:** 

* An error message is displayed stating “Epic sadface: Username is required”.   
* User remains on the login page.

### ***Test Case ID:** TC\_LOGIN\_006:*

### ***Title:*** *User attempts to log in with an empty field (Password)*

* **Precondition**:   
  * User is navigated to the login page  
* **Test Data:**  
  * **URL:** https://www.saucedemo.com/  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps:**  
  1. Enter a valid username (standard\_user) in the Username field  
  2. Click the Login button

**Expected Result:** 

* An error message is displayed stating “Epic sadface: Password is required”.   
* User remains on the login page.

### ***Test Case ID:** TC\_LOGIN\_007:*

### ***Title:*** *Locked-out user attempts login*

* **Precondition**:   
  * User is navigated to the login page  
* **Test Data:**  
  * **URL:** https://www.saucedemo.com/  
  * **Username:** locked\_out\_user  
  * **Password:** secret\_sauce  
* **Steps:**   
  1. Enter a valid username (locked\_out\_user) in the Username field  
  2. Enter a valid password (secret\_sauce) in the Password field  
  3. Click the Login button

**Expected Result:** 

* An error message is displayed stating “Epic sadface: Sorry, this user has been locked out.”   
* User remains on the login page.

