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
2. [**Client Stories Testing**](#client-stories-testing)
3. [**Manual Testing**](#manual-testing)
    - [**Testing undertaken on laptop**](#testing-undertaken-on-laptop) 
    - [**Testing undertaken on mobile and pad devices**](#testing-undertaken-on-mobile-and-pad-devices)
    - [**Testing undertaken in DevTools**](#testing-undertaken-in-DevTools)
4. [**Bugs discovered**](#bugs-discovered)
    - [**Solved bugs**](#solved-bugs)
    - [**Unsolved bugs**](#unsolved-bugs)
5. [**Further Testing**](#further-testing)



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
