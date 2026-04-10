# Sauce Demo Cart Test Cases

# **Focus:** Cart Functionality

## **Test Scenarios**

1. Add item from PLP  
2. Add item from PDP  
3. Adding Multiple items to the cart from PDP  
4. Remove a single item from the cart  
5. Remove multiple items from the cart  
6. Remove a single from the cart via PLP  
7. Remove multiple items from the cart via PLP  
8. Remove item from the cart via PDP  
9. Accessing the cart when empty  
10. Verify that the PDP of an item can be accessed from the cart page   
11. Verify that the user can add multiple items to the cart from the PLP  
12. Verify navigation to checkout from cart   
13. Verify Item displays properly in cart  
14. Verify navigation back to PLP from cart

## **Test Cases:**

### ***Test Case ID:** TC\_CART\_001*

#### ***Title:** Add item from PLP*

* **Precondition**:   
  * User is logged in with valid credentials   
* **Test Data:**   
  * **URL:** https://www.saucedemo.com/  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Click the “Add to Cart” button on any item.  
  2. Click the cart icon in the top right corner 

**Expected Result:** 

* The cart item UI should consist of  
  * Item name  
  * Quantity  
  * Description

### ***Test Case ID:** TC\_CART\_002*

#### ***Title:** Add item from PDP*

* **Precondition**:  
  * User is logged in  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/inventory-item.html](https://www.saucedemo.com/inventory-item.html)  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Navigate to PDP (Any item)  
  2. Click the “Add to Cart” button on any item.  
  3. Click the cart icon in the top right corner

**Expected Result:** 

* User is navigated to the cart page.  
* The cart item UI should consist of  
  * Item name  
  * Quantity  
  * Description

### ***Test Case ID:** TC\_CART\_003*

#### ***Title:** Adding Multiple items to the cart from PDP*

* **Precondition**:   
  * User is logged in  
  * User must be on the PLP  
* **Test Data:**  
  * **URLS:** [https://www.saucedemo.com/inventory-item.html](https://www.saucedemo.com/inventory-item.html)  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Navigate to any PDP  
  2. Click the **“Add to Cart”** button for any product  
  3. Verify the cart badge reflects the correct QTY  
  4. Navigate back to PLP  
  5. Repeat steps until all 6 items are added

**Expected Result:** 

* The cart badge updates dynamically as items are added (Max of 6\)  
* All selected items are displayed in the cart  
* Each item displays a **“Remove”** button

### ***Test Case ID:** TC\_CART\_004*

#### ***Title:** Remove a single item from the cart*

* **Precondition**:   
  * User must be logged in  
  * Navigated to the cart page  
  * Single item exists in the cart  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/cart.html](https://www.saucedemo.com/cart.html)   
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Click the “Remove” button on the selected item

**Expected Result:** 

* The item should be removed from the cart  
* The cart page should be empty

### ***Test Case ID:** TC\_CART\_005*

#### ***Title:** Remove multiple items from the cart*

* **Precondition**:   
  * User must be logged in  
  * Navigated to the cart page  
  * Multiple items exist in the cart (Max. of 6\)  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/cart.html](https://www.saucedemo.com/cart.html)    
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Click the “Remove” button on any selected item  
  2. Repeat the step until the cart page is empty

**Expected Result:** 

* All items should be removed from the cart  
* The cart badge should be updated dynamically

### ***Test Case ID:** TC\_CART\_006*

#### ***Title:** Remove a single from the cart via PLP*

* **Precondition**:   
  * User must be logged in  
  * Navigated to the PLP   
  * Single item exists in the cart  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/inventory-item.html](https://www.saucedemo.com/inventory-item.html)  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Click the “Remove” button on the selected item

**Expected Result:** 

* The item should be removed from the cart  
* The quantity on the cart badge should be removed

### ***Test Case ID:** TC\_CART\_007*

#### ***Title:** Remove multiple items from the cart via PLP*

* **Precondition**:   
  * User must be logged in  
  * Navigated to the PLP   
  * Multiple items exist in the cart (Max. of 6\)  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/inventory-item.html](https://www.saucedemo.com/inventory-item.html)  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Click the “Remove” button on any selected item  
  2. Repeat the step until the cart page is empty

**Expected Result:** 

* The item should be removed from the cart  
* The cart badge decreases by **1** after each item is removed (e.g., 6 → 5 → 4 → 3 → 2 → 1 → 0\)  
* The cart badge should be removed after the last item has been removed

### ***Test Case ID:** TC\_CART\_008*

#### ***Title:** Remove item from the cart via PDP*

* **Precondition**:   
  * User must be logged in  
  * Navigated to the PDP of an item already in the cart  
  * Single item exists in the cart  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/inventory-item.html](https://www.saucedemo.com/inventory-item.html)  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Click the “Remove” button on the selected item

**Expected Result:** 

* The item should be removed from the cart  
* The cart badge decreases by **1** after item removal (e.g., 6 → 5 → 4 → 3 → 2 → 1 → 0\)  
* The cart badge should be removed after the last item has been removed

### ***Test Case ID:** TC\_CART\_009*

#### ***Title:** Accessing the cart when empty*

* **Precondition**:   
  * User must be logged in  
  * Navigated to any page other than the cart  
  * No item exists in the cart  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/inventory-item.html](https://www.saucedemo.com/inventory-item.html)  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Click the cart icon in the top-right corner of the PLP.

**Expected Result:** 

* User should be navigated to the cart page  
* No items should be displayed

### ***Test Case ID:** TC\_CART\_010*

#### ***Title:** Verify that the PDP of an item can be accessed from the cart page*

* **Precondition**:   
  * User must be logged in  
  * Navigated to cart page  
  * Item exists in the cart page  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/inventory-item.html](https://www.saucedemo.com/inventory-item.html)  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Click on the product's name in the cart UI

**Expected Result:** 

* User should be navigated to the products PDP  
* The correct product should display

### ***Test Case ID:** TC\_CART\_011*

#### ***Title:** Verify that the user can add multiple items to the cart from the PLP*

* **Precondition**:   
  * User is logged in with valid credentials  
  * User is on the Product Listing Page (PLP)  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/inventory-item.html](https://www.saucedemo.com/inventory-item.html)  
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Identify all available products on the PLP  
  2. Click the **“Add to Cart”** button for the first product  
  3. Click the **“Add to Cart”** button for the second product  
  4. Click the **“Add to Cart”** button for the third product  
  5. Click the **“Add to Cart”** button for the fourth product  
  6. Click the **“Add to Cart”** button for the fifth product  
  7. Click the **“Add to Cart”** button for the sixth product 

**Expected Result:** 

* The cart badge displays 6 items  
* Each selected product button changes from “Add to Cart” to “Remove.”  
* All selected items are successfully added to the cart

### ***Test Case ID:** TC\_CART\_012*

#### ***Title:** Verify navigation to checkout from cart*

* **Precondition**:    
  * User is logged in with valid credentials  
  * User has at least one item added to the cart  
  * User is on the Cart page  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/cart.html](https://www.saucedemo.com/cart.html)   
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Observe the items displayed in the cart  
  2. Click the “**Checkout**” button

**Expected Result:**

* User is redirected to the checkout information page  
* **URL** should update to**:** [https://www.saucedemo.com/checkout-step-one.html](https://www.saucedemo.com/checkout-step-one.html)   
* The following UI elements are displayed:  
  * **First Name** input field  
  * **Last Name** input field  
  * **Zip/Postal Code** input field  
  * **Cancel** button  
  * **Continue** button

### ***Test Case ID:** TC\_CART\_013*

#### ***Title:** Verify Item displays properly in cart*

* **Precondition**:    
  * User is logged in with valid credentials  
  * User has at least 1 item added to the cart  
  * User is on the Cart page  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/cart.html](https://www.saucedemo.com/cart.html)   
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Navigate to cart

**Expected Result:**

* The selected item is displayed in the cart  
* Item name matches the product added from the PLP  
* Item description is visible and not empty  
* Item price is displayed and matches the PLP price  
* The **“Remove”** button is visible for the item

### ***Test Case ID:** TC\_CART\_014*

#### ***Title:** Verify navigation back to PLP from cart*

* **Precondition**:    
  * User is logged in with valid credentials  
  * User has at least 1 item added to the cart  
  * User is on the Cart page  
* **Test Data:**  
  * **URL:** [https://www.saucedemo.com/cart.html](https://www.saucedemo.com/cart.html)   
  * **Username:** standard\_user  
  * **Password:** secret\_sauce  
* **Steps**:  
  1. Click the “**Continue Shopping**” button

**Expected Result:**

* The site should navigate back to the PLP  
* Full item listing should be present in the PLP

