# Test Plan – Sauce Demo (Login & Cart Functionality)

## 1. Test Plan ID
TP_SD_001

---

## 2. Objective
The purpose of this test plan is to validate the Login and Cart functionalities of the Sauce Demo application to ensure they meet functional requirements and provide a reliable user experience.

This includes:
- Verifying authentication flows (valid/invalid login scenarios)
- Validating cart operations (add/remove/navigation/checkout)
- Ensuring UI elements and data consistency across pages

---

## 3. Scope

### In Scope

**Login Functionality**
- Valid login  
- Invalid login (username/password)  
- Empty field validations  
- Locked-out user handling  

**Cart Functionality**
- Add/remove items (PLP, PDP, Cart)  
- Multiple item handling  
- Cart badge updates  
- Navigation (Cart ↔ PLP ↔ PDP)  
- Checkout entry validation  
- UI validation of cart items  

---

### Out of Scope
- Payment processing
- Backend/database validation
- Performance testing
- Security testing

---

## 4. Test Strategy

### Testing Types
- Functional Testing
- UI Testing
- Regression Testing (after changes)
- Exploratory Testing (optional)

### Test Levels
- System Testing (end-to-end flows)
- Integration Testing (navigation between pages)

### Test Approach
- Manual testing using defined test cases
- Automated testing using:
  - Playwright (Python)
  - Pytest framework
  - Page Object Model (POM)

---

## 5. Test Environment

- Application: Sauce Demo
- Browser: Chrome (primary)
- OS: Windows
- Automation Tools: Playwright + Pytest
- Version Control: GitHub

---

## 6. Test Data

| Scenario | Username | Password |
|----------|----------|----------|
| Valid User | standard_user | secret_sauce |
| Invalid Password | standard_user | invalid_password |
| Invalid Username | invalid_user | secret_sauce |
| Locked User | locked_out_user | secret_sauce |

---

## 7. Entry Criteria

- Application is accessible
- Test environment is set up
- Test cases are created and reviewed
- Test data is available

---

## 8. Exit Criteria

- All test cases executed
- Critical and high defects resolved
- Test results documented
- Test summary report completed

---

## 9. Test Deliverables

- Test Plan
- Test Cases (Login & Cart)
- Test Execution Report
- Defect Reports
- Automation Scripts (Playwright)

---

## 10. Risk & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Application downtime | Testing blocked | Retest later / schedule buffer |
| Test data issues | Invalid results | Use predefined credentials |
| UI changes | Test failures | Update locators using POM |

---

## 11. Test Case Mapping

### Login Test Coverage
- TC_LOGIN_001 → Valid login  
- TC_LOGIN_002–003 → Invalid credentials  
- TC_LOGIN_004–006 → Empty field validation  
- TC_LOGIN_007 → Locked user  

### Cart Test Coverage
- TC_CART_001–003 → Add items  
- TC_CART_004–008 → Remove items  
- TC_CART_009 → Empty cart  
- TC_CART_010–014 → Navigation, UI, checkout  

---

## 12. Automation Strategy

- Use sync_playwright() version for debugging
- Use Pytest + fixtures for scalable execution
- Implement Page Object Model (POM) for:
  - Login Page
  - Inventory Page (PLP)
  - Product Page (PDP)
  - Cart Page

---

## 13. Reporting

- Pass/Fail status per test case
- Screenshots for failures
- Logs via Pytest
- GitHub repository as source of truth

---

## 14. Approval

| Role | Name | Status |
|------|------|--------|
| QA Engineer | (Your Name) | Pending |
| Reviewer | (Optional) | Pending |

