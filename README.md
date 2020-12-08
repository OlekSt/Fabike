# FABIKE
## DESIGNED FOR EXPERIENCE

#### E-commerce website for a bicycle brand producing carbon fibre and titanium frames, selling them as well as fully assembled bicycles with high end components. (Full Stack project)

<img src="" alt="Title image" style="margin: 0 10px;" width="100%"/>

[FABIKE - Heroku link](website will be here)

************************************************************

<img src="media/readme/t2x_rohloff_drop_lr.jpg" alt="Title image" style="margin: 0 10px;" width="100%"/>

************************************************************

## Table of Contents

1. [**UX**](#ux)
    - [**Goals**](#goals)
    - [**Strategy**](#strategy)
    - [**Scope**](#scope)
    - [**Structure**](#structure)
    - [**Skeleton**](#skeleton)
    - [**Surface**](#surface)

2. [**Information Architecture**](#information-architecture)
    - [**Database Choice**](#database-choice)
    - [**Data Modelling**](#data-modelling)

3. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features to be Implemented**](#features-to-be-implemented)

4. [**Technologies used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Libraries and Frameworks**](#libraries-and-frameworks)
    - [**Tools**](#tools)
    - [**Databases**](#databases)

5. [**Testing**](#testing)

6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Heroku Deployment**](#heroku-deployment)

7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Images**](#images)
    - [**Code**](#code)
    - [**Acknowledgments**](#acknowledgments)

8. [**Disclaimer**](#disclaimer)  
---

## UX

### GOALS

Target audience:
- Cyckling enthusiast, semi- & professionals, who value high quality products for sports, who are very knowledgeable about the industry, and want to purchase a high end customizable frame or fully assembled bicyckle for their sports or recreational cyckling.

Main goal of this site: 
- Build a full cycle e-shop to present the brand's products to potential buyers, and enable the latter with an easy way to choose a product, get all necessary info about the products on the web or additional info by contacting the website's onwer, quickly and easily purchase one, or save it for buying later.

Organizational Goals:
- Present products in way to make a purchase easy
- Enable convenient & quick way of buying products via its e-shop
- Sell frames & bicyckles
- Promote & provide educational support on how to service and take care of bicicles
- Strengthen the brand's image

User Goals:
- Browse through products & get all necessary info about them, and all related info (e.g., components, shipping)
- Quickly and easily purchase a product
- Get answers from the producers in case any 
- Attend educational workshops

##### back to [top](#table-of-contents)


### STRATEGY



### SCOPE 

User Stories

Wesbite visitors:
- First time website visitor:
    * I want to get a clear idea what the website is about
    * I want to be able to easily see where I can find various info (menu, sections, links, individual pages/windows) and easily navigate there
    * Find appropriate section - bikes or frames, urban bikes or all road bikes, etc, and be able to see all the products in the section
    * Choose an individual product, and get all necessary info: images, descriptions, technical parameters, price, delivery terms, etc. 
    * I want to be able to choose appropriate size, color and add the product to shopping cart
    * I want to be able to easily navigate from the shopping cart back to products
    * Then once I am done with products, I want to be able to easily find the shopping cart, and navigate there.
    * I want to be able to go to checkout, see all the info about my purchase, be able to add billing/shipping details, add my card details, and pay with one-click.
    * Also I want to be able to automatically (during checkout-payment process) add my details and automatically create an account (adding all my data, incl. shipping address).
    * Once the payment is processed, I want to get a confirmation email about the payment, and the order, with all the order details. And be able to login into my account and see the order there.
    * If I don’t purchase anything, I want to be able to create an account, add my details, and add products to my wish list. 
    * If I decide not to create an account, I want to have an option to send a message or ask questions about the products

- Returning visitor (in addition to possibilities described above, except those specific to first time visitors):
    * If I haven’t created a profile yet, to find easily where I can do that, and create one.
    * I want to be able to login into my account, update my data if needed, and see my wish list if I created it.
    * I want to be able to navigate across the website and get info necessary for me to decide about a purchase and purchase a product taking steps described above.

- Website administrator:
    * To have access to all the necessary data to manage products’ display on the web-site, customers’ accounts, and purchase histories, etc. 
    * To be able to easily login and navigate within the admin area of the website.
    * To be able to easily add, modify or delete products listings, with all the necessary info – images, descriptions, technical parameters, etc. 


Visitor vs Administrator:
- Website's visitor can:
    * Look through products (bikes, frames, repair workshops)
    * Check details of an individual product
    * Add a product to a wish list
    * Add a product to shopping cart
    * Go to checkout
    * Order a product/Pay for it
    * Create an account
    * Update user’s details (email, password, phone, shipping address, etc)
    * See one’s wish list
    * See one’s order history
    * See calendar of planned repair workshops
    * Send a message via Contact Us form

- Website's administrator can:
    * Add/delete/update products (info, descriptions, parameters, prices, images)
    * Manage users’ accounts
    * See orders’ list (fulfilled, in progress, ordered)
    * Add/update/delete events (repair workshops)


Logged-in vs unlogged:
- Unlogged user can see/access:
    * Products (all or individual)
    * Events (repair workshops)
    * Create an account form
    * Add to cart
    * Proceed to checkout
    * Order/Pay a product (with or without registration)
    * Warranty & Compensations
    * Return & refund policy

- Logged user can see/access:
    * Everything as above
    * Personal account (user’s details, order history, wish list)
    * Administtrator can acess product management area (inaccessible to other logged in users)
    


### STRUCTURE 


### SKELETON

[Balsamiq](https://balsamiq.com/) wireframes software was used to create wireframes for this project:


### SURFACE 

Design choices:


Colors:

Fonts: 

Images:


## INFORMATION ARCHITECTURE

### DATABASE CHOICE

* During development on a local machine standard sqlite3 databasewill be used, as it is installed with Django.

* After deployment, PostgreSQL database will be used as, it is provided by Heroku where the website will be deployed.  

### DATA MODELLING

#### User
The User model used is provided by Django as a part of defaults `django.contrib.auth.models`.

#### Accounts app
##### Account
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User | user |  on_delete=models.CASCADE | OneToOneField 'User' 
 Full Name | account_full_name | max_length=70 | CharField
 Phone number | account_phone_number | max_length=25 | CharField
 Address Line1 | account_address_line1 | max_length=120 | CharField
 Address Line2 | account_address_line2 | max_length=120, null=True, blank=True | CharField
 Town/City | account_town_or_city | max_length=70 | CharField
 County | account_county | max_length=50, null=True, blank=True | CharField
 Postcode | accountaccount_postcode | max_length=20 | CharField
 Country | account_country | blank_label='Country' | CountryField

#### Products app
##### Product
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Product Type | type | choices=PRODUCT_TYPE | CharField
 Name | name | max_length=80 | CharField
 Frame Type | frame | max_length=80  | CharField
 Title | title | max_length=120  | TextField
 Fork | fork | max_length=80 | CharField
 Wheels | wheels | max_length=80  | CharField
 Tyres | tyres | max_length=80 | CharField
 Max Tyre Size | max_tyre_size | max_length=20  | CharField
 Crankset | crankset | max_length=80 | CharField
 Shift Levers | shift_levers | max_length=80  | CharField
 Derailleurs | derailleurs | max_length=80 | CharField
 Casette/Sprocket | casette_or_sprocket | max_length=80  | CharField
 Chain/Belt | chain_or_belt | max_length=80 | CharField 
 Brakes | brakes | max_length=80  | CharField
 Handlebar | handlerbar | max_length=80  | CharField
 Stem | stem | max_length=100 | CharField
 Saddle | description | max_length=80  | CharField
 Seatpost | description | max_length=80  | CharField
 Seat Clamp | name | max_length=80 | CharField
 Headset | description | max_length=80  | CharField
 Seatpost Diameter | description | max_length=254  | CharField
 Bottom Bracket Type | bottom_bracket | max_length=80 | CharField
 Dropouts | dropouts | max_length=120  | CharField
 Weigth | weight | max_digits=4, decimal_places=2  | DecimalField
 Weight Alloy | weight_alloy | max_digits=4, decimal_places=2 | DecimalField
 Weight Carbon | weight_carbon | max_digits=4, decimal_places=2  | DecimalField
 Price | price | max_digits=6, decimal_places=2  | DecimalField
 Price Alloy | price_alloy | max_digits=6, decimal_places=2 | DecimalField
 Price Carbon | price_carbon | max_digits=6, decimal_places=2  | DecimalField
 Price comment | description | max_length=254  | TextField 
 Image 1 | product_image01 |  | ImageField
 Image 2 | product_image02 | null=True, blank=True | ImageField
