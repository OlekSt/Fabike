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

User story: Choose an individual product, and get all necessary info: images, descriptions, technical parameters, price, delivery terms, etc. 

    Testing:
    - Open any bike section(all bikes, urban, all road or road bikes) and click an individual product
    - Open frames and click one of the frames
    - Open events page and click More info on one of the events
    - Typed some search words into the search field

    Results:
    - An individual bicycle page contains all the necesessary info about the product.
    - Image, name, frame name, clickable color/size/components options, price and weight, list of components, info about geometry of the frames and sizes relative to a person's height. 
    - It includes production and delivery info. 
    - An individual frame page contains the same info as a bicycle page, except of the components. 
    - An event page has info about the topic, what attendees will learn during a workshop, price, time and date, location, and a button to contact the company to book a spot for an attendee.
    
    Conclusion:
    - Passed. All individual pages work as expected, and display necessary info for a visitor of the website to make a decsion of next steps from such a page, and provides necessary tools to continue. 

User story: I want to be able to choose appropriate size, color and add the product to shopping cart

    Testing: 
    - Click & choose individual parameters of a product - color, size, components
    - Click Add to Cart button
    - Click Shopping Cart 

    Results: 
    - All of the selectors work correctly responding to click, change of components also highlights respective price and weight of a products, depending where carbon fibre or alloy components are chosen. 
    - Clicking Add to Cart add a products to the cart. I get a confirmation message. Also can see the change of the color of the cart icon and number of products added.  
    - Shopping Cart icon takes me to the shopping cart page, where I can see info about products added. 
    Conclusion:
    - Passed. All the functionality works as planned and provides necessary feedback to a user. 

User story: I want to be able to easily navigate from the shopping cart back to products

    Testing: 
    - Click Back to Bikes button
    - Click links in the navbar
    Results: 
    - Back to Bikes takes me back to all the bicycles displayed together, and I can see more options
    - Using navbar menu takes me to Bikes, Frames or Events pages
    Conclusion:
    - Passed. Works as planned, a user can easily navigate back to explore more products, using several options.  

User story: Then once I am done with products, I want to be able to easily find the shopping cart, and navigate there

    Testing: 
    - Location Shopping cart icon and click it
    Results: 
    - The icon is easily and always visible in the upper right corner
    - It has blue color and displays a number of products added
    - Clicking it opens the shopping cart page, displaying all the necessary info about product
    - A user can update quantity of a product or delete a product from a shopping cart, a message is provided to a user upon each action
    - If the cart is empty it displays a message that it is empty and has a button Back to Bikes
    - If all products deleted, the icon becomes white and displays zero
    Conclusion:
    - Passed. Works as expected. 

User story: I want to be able to go to checkout, see all the info about my purchase, be able to add billing/shipping details, add my card details, and pay with one-click

    Testing: 
    - Click Checkout button from the cart
    - Check Checkout Summary
    - Add my billing/shipping details
    - Enter card info and press Complete Order

    Results: 
    - It takes me to checkout page as expected
    - The summary shows the product details: model, color, size, components, quantity, price, delivery cost, final sum to pay
    - It displays a form for billing and shipping details, which a user can fill in
    - Beneath the form there is an option to Sign Up or Sign In
    - Payment info field for card info
    - a user can choose buttons Back to Cart & Complete order
    - A user can see a message, informing how much an entered card will be charged

    Conclusion:
    - Passed.
    - I can see all the necessary info about my order
    - The form does not let to proceed unless all the necessary fields are filled in
    - Pressing Sign Up takes me to create an account
    - If card details are incomplete or missing, a relevant message is displayed, and an order cannot be paid

User story: Also I want to be able to automatically (during checkout-payment process) add my details and automatically create an account (adding all my data, incl. shipping address)

    Testing: 
    - Clicking Sign Up under the form to create an account

    Results: 
    - It takes me to create an account. 
    - Once an account is created and I navigate back to checkout I can save billing and shipping info into my account automatically
    - I get a confirmation message that I signed in as "user name"

    Conclusion:
    - Passed. All works as expected

User story: Once the payment is processed, I want to get a confirmation email about the payment, and the order, with all the order details. And be able to login into my account and see the order there.

    Testing: 
    - I get to order susccess summary page
    - i check my email    
    - I click Profile Icon and choose Profile
    - I update my info
    - i check purchase histroy and open a past order

    Results: 
    - Once checkout process is successful I get a message about an order
    - Then I am taken to a summary page with all the info of an order, saying that all the info will be sent to my email
    - I get an email with confirmation of my order
    - I can open my profile, where I can see my shipping details
    - I update them and get a success message
    - I can see my purchse history, and can open last orders details
    - I open a past order, which takes me to a page with the order summary: oder number/date, product details, shipping address, payment info. 
    Conclusion:
    - Passed.
    - All works as expected.

User story: If I don’t purchase anything, I want to be able to create an account, add my details, and add products to my wish list

    Note: Feature was removed from the current implementation due to time constriants, and postponed for further stages of the project development. 
    

User story: If I decide not to create an account, I want to have an option to send a message or ask questions about the products

    Testing: 
    - Navigate to contact page
    - Send a message

    Results: 
    - I am taken to a contact us form
    - I fill it in, and send
    - I get a confirmation that my message was sent succesfully

    Conclusion:
    - Passed. 
    - The contact form works as expected, does not allow a message with any field empty
    - I checked my email, a message was received

    Bug: 
    - Subject is missing in the message. 
    Fixed: 
    - Updated code in views.py of the contact app

    

- Returning visitor (in addition to possibilities described above, except those specific to first time visitors):


User story: If I haven’t created a profile yet, to find easily where I can do that, and create one
    
    Testing: 
    Results: 
    Conclusion:

User story: I want to be able to login into my account, update my data if needed, and see my wish list if I created it
    
    Testing: 
    Results: 
    Conclusion:

User story: I want to be able to navigate across the website and get info necessary for me to decide about a purchase and purchase a product taking steps described above
    
    Testing: 
    Results: 
    Conclusion:

- Website administrator:

User story: To have access to all the necessary data to manage products’ display on the web-site, customers’ accounts, and purchase histories, etc. 

    Testing: 
    Results: 
    Conclusion:

User story: To be able to easily login and navigate within the admin area of the website
    
    Testing: 
    Results: 
    Conclusion:

User story: To be able to easily add, modify or delete products listings, with all the necessary info – images, descriptions, technical parameters, etc.

    Testing: 
    Results: 
    Conclusion: 




## BUGS DISCOVERED
### SOLVED BUGS

Bug: 
- On Heroku getting 500 error upon pressing Checkout button, while it works from Gitpod.
Solution: 
- Added Stripe public, secret, & wh keys to heroku.
Solved

Bug: 
- Stripe webhooks don't work.
Solution: 
- Added Stripe public, secret, & wh keys to heroku.
Solved.

Bug: 
- Checkout works well, an order is created, but a confirmation email is not sent. Tried both signed-in purchase, and non signed-in purchase. 
Solution: 
- Updated secret keys on heroku.
Solved.

Bug: 
- Checkout works, and gives a toast message, an email is sent. But two orders are created with two different numbers. First order number is shown in a toast message, and this order is created without current cart data & stripe pid.
- Second order number is indicated in a confirmation email, and this 2nd order has both current cart data & stripe pid.
- Webhooks events are registered correctly on stripe. But I get a 500 error, if I send a webhook test for payment_intent.succeded.
Solution: 
- Added a couple of missing lines of code in webhooks_handler.py (lines 41-45). 
Solved: 
- Now one order is created, it has cart data + stripe pid in DB, a confirmation email is sent with a correct order number, strip registers all three events as succeded: payment_intent.created, payment_intent.succeded, charge.succeeded.

Bug: 
- Current images are not displayed correctly in Product management edit a product form.
Solution: 
- Moved all the product images from static/img to media, updated all the image links.
Solved: 
- Works as it should

### UNSOLVED BUGS

Bug: 
- Connected to the one above. When testing webhook 'payment_intent.succeded' get 'POST /checkout/wh/ HTTP/1.1" 500 135356' & 'AttributeError: cart'
Solution: 
- ...
Not solved?

