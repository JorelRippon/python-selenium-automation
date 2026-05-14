# HW3 - StackOverflow Create Account Page Locators

**Page:** https://stackoverflow.com/users/signup

### Optimal Locators:

- **Email field**: `By.ID("email")`
- **Display name**: `By.ID("display-name")`
- **Password**: `By.ID("password")`
- **Next button**: `By.XPATH("//button[text()='Next']")`
- **Google button**: `By.XPATH("//button[contains(.,'Google')]")`
- **GitHub button**: `By.XPATH("//button[contains(.,'GitHub')]")`
- **Facebook button**: `By.XPATH("//button[contains(.,'Facebook')]")`

These use ID where possible (best practice).
