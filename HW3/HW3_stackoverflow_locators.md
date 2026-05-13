# HW3 - StackOverflow Create Account Page Locators

**Page URL:** https://stackoverflow.com/users/signup

### Optimal Locators:

- **Email field**: `By.ID("email")`
- **Display name field**: `By.ID("display-name")`
- **Password field**: `By.ID("password")`
- **Next / Continue button**: `By.XPATH("//button[text()='Next']")`
- **Sign up with Google**: `By.XPATH("//button[contains(., 'Google')]")`
- **Sign up with GitHub**: `By.XPATH("//button[contains(., 'GitHub')]")`
- **Sign up with Facebook**: `By.XPATH("//button[contains(., 'Facebook')]")`

These locators use **ID** where possible (best practice for speed and reliability).
