```
Feature: User login process
    As a user I want to be able to authenticate into the application

    Background:
        Given I am at the login page
        And I am already registered as an administrator

    @login_001
    Scenario: User is redirected to the home page
        Given I enter a valid credentials values
        When I select Entrar
        Then I am at the Home page
        And I am greeted by my name

    Background:
        Given I am at the login page
        And I am already registered as a regular user

    @login_002
    Scenario: User is redirected to the home page
        Given I enter a valid credentials
        When I select Entrar
        Then I am at the Home page
        And I see the Serverest Store

    @login_003
    Scenario: User is redirected to the registration page
        Given I am at the login page
        When I select Cadastrar-se
        Then I am at the registration page

    Rule: Users are notified about credentials issues
    Background:
        Given I am at the login page

    @login_004
    Scenario: Alert email address is required
        Given I enter a password
        When I select Entrar
        Then I am notified that an email address is required

    @login_005
    Scenario: Alert password is required
        Given I enter a valid email address
        When I select Entrar
        Then I am notified that a password is required

    @login_006
    Scenario: Alert credentials are invalid when email is not registered
        Given I am not registered
        And I enter a valid credential
        When I select Entrar
        Then I am notified that the email and/or password are invalid

    @login_007
    Scenario: Alert credentials are invalid when password is wrong
        Given I am already registered
        And I enter the registered email address
        But I enter a invalid password
        When I select Entrar
        Then I am notified that the email and/or password are invalid
```
