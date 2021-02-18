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
I have tested responsiveness of the website for various mobile, pad, laptop & desktop sized screens on:
- Google Chrome Devtools 
- [Responsive Checker](https://www.websiteplanet.com/webtools/responsive-checker/). 

### Client Stories Testing
The user stories are described in the UX section of [README.md](README.md) 

Wesbite visitors:
- First time website visitor:

User story: I want to get a clear idea what the website is about

    Testing: 
    - Open the home page, scroll it down 
    
    Results: 
    - Hero image slide shows featureing bicycles. 
    - Navbar menu contains "Bikes" & "Frames", as well as  "About" links. 
    - Scrolling down revels images with info and additional access buttons to urban, all-road, road bikes scetions.
    - Additionally you can info about brands the company works with. 
    - The footer contains additional links to Bikes, Frames, About, etc.

    Conclusion:
    - Passed. A visitor can easily understand what the website is about, as well as see the main navigation units allowing to continue exploring the website.
    
User story: I want to be able to easily see where I can find various info (menu, sections, links, individual pages/windows) and easily navigate there

    Testing: 
    - Located the Navbar, and clicked all of the links there: 
            1. Bikes>All Bikes/Urban/All Road/Road
            2. Frames
            3. Events
            4. About
            5. Contact
    - Clicked Search icon
    - Clicked Profile icon
    - Clicked Cart icon
    - Scrolled down and clicked Discover buttons for each of the sections Urban, All Road, Road
    - Located the footer and clicked Bikes, Frames, Events, About, Warranty Policy, Returns & Refunds, as well as social media icons - Facebook & Instagram, and finally emal icon. 

    Results: 
    - The navbar has all the necessay links for a visitor to explore the website. Clicking each individual link leads a user to a respective part of the website, eg. clicking Bikes>Urban will open a page with all the bikes categorized as urban; or clicking Frames takes user to a page with frames listed, and so on. 
    - Search icon opens a search window, where a user can type search parameters. 
    - Profile icon opens menu with two options: SIGN UP & SIGN IN (not-logged in view)
    - Cart icon leads to an empty cart page. 
    - All the links in the footer lead to respective pages, except Warranty Policy, Returns & Refunds, which both lead to Under Construction page. 
    - Facebook and Instagram open social media accounts. 
    - Email icon leads to Contact Us page. 

    Conclusion: 
    - Passed. All links work as exppected. There no wrong or broken links. 

User story: Find appropriate section - bikes or frames, urban bikes or all road bikes, etc, and be able to see all the products in the section

    Testing:
    - Click links Bikes>All Bikes/Urban/All Road/Road, Frames or Events
    - Scroll down and click Discover buttons for Urban, All Road or Road section
    - Click links in the footer for Bikes, Frames, Events

    Results:
    - All links open respecive pages - Bikes, Frames or Events from either navbar, or Discover buttons in the body of the home page, or the footer.
    - Bikes shows all three groupd of bikes in one page: Urban, All Road, Road, and allows a visitor to easily navigate either to a specific section, eg Urban or to an individual bike.
    - Frames shows both frames currently on offer, carbon fibre and titanium, and allows to navigate to either of them.
    - Events lists all upcoming events, indicating info about topic and date/time. A user can easily navigate to an individual event page to get more info or book a spot.
    - A user can always see the navbar menu, no matter where on the website one currently is, and can navigate back to any of the pages of interest. 

    Conclusion: 
    - Passed. The website offers several options from where a uers can reach respective sections of interest, bikes, frames or events.

    * Choose an individual product, and get all necessary info: images, descriptions, technical parameters, price, delivery terms, etc. 
    Testing:
    - Open any bike section(all bikes, urban, all road or road bikes) and click an individual product
    - Open frames and click one of the frames
    - Open events page and click More info on one of the events
    - Typed some search words into the search field

    Results:
    - An individual bicycle page contains all the necesessary info about the product: image, name, frame name, clickable color/size/components options, price and weight, list of components, info about geometry of the frames and sizes relative to a person's height. It includes production and delivery info. 
    - An individual frame page contains the same info as a bicycle page, except of the components. 
    - An event page has info about the topic, what attendees will learn during a workshop, price, time and date, location, and a button to contact the company to book a spot for an attendee.
    
    Conclusion:
    - Passed. All individual pages work as expected, and display necessary info for a visitor of the website to make a decsion of next steps from such a page, and provides necessary tools to continue. 

    * I want to be able to choose appropriate size, color and add the product to shopping cart
    Testing: 
    Results: 
    Conclusion:

    * I want to be able to easily navigate from the shopping cart back to products
    Testing: 
    Results: 
    Conclusion:

    * Then once I am done with products, I want to be able to easily find the shopping cart, and navigate there.
    Testing: 
    Results: 
    Conclusion:

    * I want to be able to go to checkout, see all the info about my purchase, be able to add billing/shipping details, add my card details, and pay with one-click.
    Testing: 
    Results: 
    Conclusion:

    * Also I want to be able to automatically (during checkout-payment process) add my details and automatically create an account (adding all my data, incl. shipping address).
    Testing: 
    Results: 
    Conclusion:

    * Once the payment is processed, I want to get a confirmation email about the payment, and the order, with all the order details. And be able to login into my account and see the order there.
    Testing: 
    Results: 
    Conclusion:

    * If I don’t purchase anything, I want to be able to create an account, add my details, and add products to my wish list. 
    Testing: 
    Results: 
    Conclusion:

    * If I decide not to create an account, I want to have an option to send a message or ask questions about the products
    Testing: 
    Results: 
    Conclusion:

- Returning visitor (in addition to possibilities described above, except those specific to first time visitors):
    * If I haven’t created a profile yet, to find easily where I can do that, and create one.
    * I want to be able to login into my account, update my data if needed, and see my wish list if I created it.
    * I want to be able to navigate across the website and get info necessary for me to decide about a purchase and purchase a product taking steps described above.

- Website administrator:
    * To have access to all the necessary data to manage products’ display on the web-site, customers’ accounts, and purchase histories, etc. 
    * To be able to easily login and navigate within the admin area of the website.
    * To be able to easily add, modify or delete products listings, with all the necessary info – images, descriptions, technical parameters, etc. 

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