Feature: Target Sign In Navigation

  Scenario: Logged out user can navigate to Sign In form
    Given I am on Target home page
    When I click on Sign In from header
    And I click Sign In from side navigation
    Then I should see the Sign In form
