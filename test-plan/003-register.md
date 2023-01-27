```
Feature: User register process
    As a user I want to be able to create an account

    Background:
        Given I am at the registration page

    Scenario: Register an administrator user
        Given I enter a valid credentials values
        And I select to register as administrator
        When I select Cadastrar
        Then I am at the Home page
        And I am greeted by my name

    Scenario: Register a regular user
        Given I enter a valid credentials values
        When I select Cadastrar
        Then I am at the Home page
        And I see the Serverest Store

    Rule: Users are notified about credentials issues
    Background:
        Given I am at the registration page

    Scenario: Alert name is required
        Given I enter a valid email address
        And I enter a password
        When I select Cadastrar
        Then I am notified that the name is required

    Scenario: Alert email address is required
        Given I enter a name
        And I enter a password
        When I select Cadastrar
        Then I am notified that an email address is required

    Scenario: Alert password is required
        Given I enter a valid email address
        And I enter a name
        When I select Cadastrar
        Then I am notified that a password is required

    Scenario: Alert email is already registered
        Given I am already registered
        And I enter the same credentials
        When I select Cadastrar
        Then I am notified that the email is already in use
```
