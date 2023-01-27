```
Feature: User logout process
    As a user I want to be able to exit the application from my account

    Scenario: User is able to logout from application
        Given I am already authenticated into the application
        When I select logout
        Then I am at the login page
```
