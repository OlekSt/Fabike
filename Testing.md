# FABIKE - Testing
## High-end bicycle & frames e-shop - Testing
#### Full Stack Project - Testing write-up

<img src="static/readme/t2x_rohloff_drop_lr.jpg" alt="Title image" style="margin: 0 10px;" width="100%"/>

This document is intended to record testing at various stages of development of the project, as well as different functions, functionalities, correct display of the project's page, etc. 

[Main README.md file](README.md)

## FABIKE e-shop

## Table of Contents
1. [**Automated Testing**](#automated-testing)
    - [**Validation services**](#validation-services)
2. [**Manual Testing**](#manual-testing)
    - [**Responsiveness **](#responsiveness)
    - [**Client Stories Testing**](#client-stories-testing)
    
    - [**Testing undertaken in DevTools**](#testing-undertaken-in-DevTools)
3. [**Bugs discovered**](#bugs-discovered)
    - [**Solved bugs**](#solved-bugs)
    - [**Unsolved bugs**](#unsolved-bugs)
4. [**Further Testing**](#further-testing)

## Automated Testing

### Validation services
The following validation services were used to check the validity of the website code.
- [W3C Markup Validation]( https://validator.w3.org/): 

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/):

- [JSHint](https://jshint.com/) & [Esprima](https://esprima.org/demo/validate.html):

- [PEP8 Python Validator](http://pep8online.com):

- Console errors:

## Manual Testing

### Responsiveness


### Client Stories Testing
The user stories are described in the UX section of [README.md](README.md) 



4. Bugs discovered

Bug: On Heroku getting 500 error upon pressing Checkout button, while it works from Gitpod.
Solution: Added Stripe public, secret, & wh keys to heroku.
Solved.

Bug: Stripe webhooks don't work.
Solution: Added Stripe public, secret, & wh keys to heroku.
Solved.

Bug: Checkout works well, an order is created, but a confirmation email is not sent. Tried both signed-in purchase, and non signed-in purchase. 
Solution: Updated secret keys on heroku.
Solved.

Bug: Checkout works, and gives a toast message, an email is sent. But two orders are created with two different numbers. First order number is shown in a toast message, and this order is created without current cart data & stripe pid.
Second order number is indicated in a confirmation email, and this 2nd order has both current cart data & stripe pid.
Webhooks events are registered correctly on stripe. But I get a 500 error, if I send a webhook test for payment_intent.succeded.
Solution: Added a couple of missing lines of code in webhooks_handler.py (lines 41-45). 
Solved: Now one order is created, it has cart data + stripe pid in DB, a confirmation email is sent with a correct order number, strip registers all three events as succeded: payment_intent.created, payment_intent.succeded, charge.succeeded.

Bug: Connected to the one above. When testing webhook 'payment_intent.succeded' get 'POST /checkout/wh/ HTTP/1.1" 500 135356' & 'AttributeError: cart'
Solution:
Solved / Not solved?

Bug: Current images are not displayed correctly in Product management edit a product form.
Solution:
Solved / Not solved?