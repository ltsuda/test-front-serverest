```
Feature: User register process
    As a user I want to be able to create an account

    Background:
        Given I am at the registration page

    @register_001
    Scenario: Register an administrator user
        Given I enter a valid credentials values
        And I select to register as administrator
        When I select Cadastrar
        Then I am at the Home page
        And I am greeted by my name

    @register_002
    Scenario: Register a regular user
        Given I enter a valid credentials values
        When I select Cadastrar
        Then I am at the Home page
        And I see the Serverest Store

    @register_003
    Scenario: User is redirected to the logion page
        Given I am at the registration page
        When I select Entrar
        Then I am at the login page

    Rule: Users are notified about credentials issues
    Background:
        Given I am at the registration page

    @register_004
    Scenario: Alert name is required
        Given I enter a valid email address
        And I enter a password
        When I select Cadastrar
        Then I am notified that the name is required

    @register_005
    Scenario: Alert email address is required
        Given I enter a name
        And I enter a password
        When I select Cadastrar
        Then I am notified that an email address is required

    @register_006
    Scenario: Alert password is required
        Given I enter a valid email address
        And I enter a name
        When I select Cadastrar
        Then I am notified that a password is required

    @register_007
    Scenario: Alert email is already registered
        Given I am already registered
        And I enter the same credentials
        When I select Cadastrar
        Then I am notified that the email is already in use
```
