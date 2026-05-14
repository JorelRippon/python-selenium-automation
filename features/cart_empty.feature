Feature: Target Cart Functionality

  Scenario: Logged out user sees empty cart message
    Given I am on Target home page
    When I click on the cart icon
    Then I should see "Your cart is empty" message
