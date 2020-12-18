# FABIKE
## DESIGNED FOR EXPERIENCE

#### E-commerce website for a bicycle brand producing carbon fibre and titanium frames, selling them as well as fully assembled bicycles with high end components. (Full Stack project)

<img src="" alt="Title image" style="margin: 0 10px;" width="100%"/>

[FABIKE - Heroku link](website will be here)

************************************************************

<img src="static/readme/t2x_rohloff_drop_lr.jpg" alt="Title image" style="margin: 0 10px;" width="100%"/>

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
- Cycling enthusiast, semi- & professionals, who value high quality products for sports, who are very knowledgeable about the industry, and want to purchase a high end customizable frame or fully assembled bicycle for their sports or recreational cycling.

Main goal of this site: 
- Build a full cycle e-shop to present the brand's products to potential buyers, and enable the latter with an easy way to choose a product, get all necessary info about the products on the web or additional info by contacting the website's onwer, quickly and easily purchase one, or save it for buying later.

Organizational Goals:
- Present products in way to make a purchase easy
- Enable convenient & quick way of buying products via its e-shop
- Sell frames & bicyckles
- Promote & provide educational support on how to service and take care of bicycles
- Strengthen the brand's image

User Goals:
- Browse through products & get all necessary info about them, and all related info (e.g., components, shipping)
- Quickly and easily purchase a product
- Get answers from the producers in case any 
- Attend educational workshops

##### back to [top](#table-of-contents)



### STRATEGY
Create an e-shop which is easy to navigate, with a simple & convenient order-payment process. The website will be built on Python-Django, with PostgreSQL database, and Stripe payment system. 



### SCOPE 

##### User Stories

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
    * Administtrator can access product management area (inaccessible to other logged in users)
    


### STRUCTURE 

The website will consist of the following pages/sections:

**Unlogged users' view**:
- HOME 
- ABOUT 
- BIKES 
- URBAN BIKES 
- ALL-ROAD BIKES
- ROAD BIKES
- FRAMES
- Individual PRODUCT pages
- EVNETS
- Individual EVENT pages
- SHOPPING CART
- CHECKOUT

**Logged users' view**:
*In addition to the pages mentioned above*
- ACCOUNT
- ORDER HISTORY
- PRODUCT MANAGEMENT (for super-user)

*For more details on what pages will contain check out the wireframes below.*



### SKELETON

[Balsamiq](https://balsamiq.com/) wireframes software was used to create wireframes for this project.

Each wireframe below contains mobile, pad & laptop/desktop view:
* [HOME](static/wireframes/home.png)
* [SIGN UP/IN](static/wireframes/sign_up_in.png)
* [ABOUT](static/wireframes/about.png)
* [BIKES](static/wireframes/bikes.png)
* [Section URBAN BIKES](static/wireframes/urban_bikes.png)
* [FRAMES](static/wireframes/frames.png)
* [PRODUCT page](static/wireframes/product_details.png)
* [SHOPPING CART](static/wireframes/shopping_cart.png)
* [CHECKOUT](static/wireframes/checkout.png)
* [ACCOUNT](static/wireframes/account.png)
* [ORDER HISTORY](static/wireframes/order_history.png)
* [PRODUCT MANAGEMENT](static/wireframes/product_management.png)
* [EVENTS](static/wireframes/events.png)
* [EVENT page](static/wireframes/event_details.png)



### SURFACE 

Design choices:
* General guidelines are taken from the existing website www.fabike.it, and approved by the main designed of the company, Fabio Putzolu. 
* The overall strucutre of existing pages(www.fabik.it) will be re-created in this project, but will be coded from scratch, and all the non-existing pages/features will be added during the development of the project.

Colors:
* All the colors & color combination will be derived from the 4 main colors used for the frames/bikes: black, blue, yellow, & red.

For the purpose of the project the following colors (matching or related) will be used:

**Greys-Blacks**

<img src="static/readme/palette/pallete_black_grey.jpg" alt="Color Picking" style="margin: 0 10px; align-self: left;"/>


**Blues**

<img src="static/readme/palette/pallete_blue.jpg" alt="Color Picking" style="margin: 0 10px; align-self: left;"/>


**Yellows**

<img src="static/readme/palette/pallete_yellow.jpg" alt="Color Picking" style="margin: 0 10px; align-self: left;"/>


**Reds**

<img src="static/readme/palette/pallete_red.jpg" alt="Color Picking" style="margin: 0 10px; align-self: left;"/>



Fonts: 
* The original web-site is using DINPro font, Bold and Light. For the purpose of the project, i will use a very similar Google font - **Noto Sans KR**. 


Images:
* All product(bikes, frames) & lifestyle photos were taken by the designer of the frames, Fabio Putzolu.
---



## INFORMATION ARCHITECTURE

### DATABASE CHOICE

* During development on a local machine standard sqlite3 databasewill be used, as it is installed with Django.

* After deployment, PostgreSQL database will be used as, it is provided by Heroku where the website will be deployed.  

### DATA MODELLING

<img src="static/readme/db_schema_diagram.png" alt="DB Schema Diagram" style="margin: 0 10px;" width="100%"/>


#### User
The User model used is provided by Django as a part of defaults `django.contrib.auth.models`.

#### Accounts app
##### Account
| **Name** | **Database Key** | **Validation** | **Field Type** | 
--- | --- | --- | --- 
 User | user |  on_delete=models.CASCADE | OneToOneField 'User' 
 Full Name | account_full_name | max_length=70 | CharField
 Phone number | account_phone_number | max_length=25 | CharField
 Address | account_address | max_length=120 | TextField, ForeignKey 'Address'

##### Address
| **Name** | **Database Key** | **Validation** | **Field Type** | 
--- | --- | --- | --- 
 Address Line1 | account_address_line1 | max_length=120 | CharField
 Address Line2 | account_address_line2 | max_length=120, null=True, blank=True | CharField
 Town/City | account_town_or_city | max_length=70 | CharField
 County | account_county | max_length=50, null=True, blank=True | CharField
 Postcode | accountaccount_postcode | max_length=20 | CharField
 Country | account_country | blank_label='Country' | CountryField

#### Products app
##### Product
| **Name** | **Database Key** | **Validation** | **Field Type** | 
--- | --- | --- | --- 
 Product Type | product_type | choices=PRODUCT_TYPE | CharField
 Product Group | product_group | choices=PRODUCT_GROUP | CharField
 Name | name | max_length=80 | CharField
 Frame Type | frame | max_length=80  | CharField
 Title | title | max_length=120  | TextField
 Fork | fork | max_length=80 | CharField
 Wheels | wheels | max_length=80, null=True, blank=True  | CharField
 Tyres | tyres | max_length=80, null=True, blank=True | CharField
 Max Tyre Size | max_tyre_size | max_length=80, null=True, blank=True   | CharField
 Crankset | crankset | max_length=80, null=True, blank=True | CharField
 Shift Levers | shift_levers | max_length=80, null=True, blank=True  | CharField
 Derailleurs | derailleurs | max_length=80, null=True, blank=True | CharField
 Casette/Sprocket | casette_or_sprocket | max_length=80, null=True, blank=True  | CharField
 Chain/Belt | chain_or_belt | max_length=80, null=True, blank=True | CharField 
 Brakes | brakes | max_length=80, null=True, blank=True  | CharField
 Handlebar | handlebar | max_length=80, null=True, blank=True  | CharField
 Stem | stem | max_length=100, null=True, blank=True | CharField
 Saddle | saddle | max_length=80, null=True, blank=True  | CharField
 Seatpost | seatpost | max_length=80, null=True, blank=True  | CharField
 Seat Clamp | seat_clamp | max_length=80, null=True, blank=True | CharField
 Headset | headset | max_length=80, null=True, blank=True  | CharField
 Seatpost Diameter | seatpost_diameter | max_length=20  | CharField
 Bottom Bracket Type | bottom_bracket | max_length=80 | CharField
 Dropouts | dropouts | max_length=120  | CharField
 Weigth | weight | max_digits=4, decimal_places=2  | DecimalField
 Weight Alloy | weight_alloy | max_digits=4, decimal_places=2 | DecimalField
 Weight Carbon | weight_carbon | max_digits=4, decimal_places=2  | DecimalField
 Price | price | max_digits=6, decimal_places=2  | DecimalField
 Price Alloy | price_alloy | max_digits=6, decimal_places=2 | DecimalField
 Price Carbon | price_carbon | max_digits=6, decimal_places=2  | DecimalField
 Price comment | price_comment | max_length=120  | CharField 
 Image 1 | product_image01 |  | ImageField
 Image 2 | product_image02 | null=True, blank=True | ImageField

* Product Types/choices are defined within the Product model.


#### Checkout App
##### Order
| **Name** | **Database Key** | **Validation** | **Field Type** | 
--- | --- | --- | --- 
 Order Number | order_number | CharField | max_length=32, null=False, editable=False
 User | account | ForeignKey 'Account' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
 Full Name | account_full_name | max_length=70 | CharField
 Phone number | account_phone_number | max_length=25 | CharField
 Address | delivery_address | max_length=254 | TextField, ForeignKey 'Address'
 Purchase Date | purchase_date | auto_now_add=True | DateTimeField
 Order Total | order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
 Stripe Pid | stripe_pid | max_length=254, null=False, blank=False, default='' | CharField
 Comment | comment | TextField | max_length=254, null=True, blank=True
 Shipped | shipped | default=False | BooleanField


 ##### Order Item Details 
| **Name** | **Database Key** | **Validation** | **Field Type** | 
--- | --- | --- | --- 
 Order | order | null=False, blank=False, on_delete=models.CASCADE, related_name='orderitems' | ForeignKey 'Order'
 Product | product | null=False, blank=False, on_delete=models.PROTECT | ForeignKey 'Product' or 'Event'
 Quantity | quantity | null=False, blank=False, default=0 | IntegerField
 Color | color | choices=COLORS | CharField
 Size | size | choices=SIZES | CharField
 Components | alloy_or_carbon | choices=COMPONENTS | CharField
 Item Total | item_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | DecimalField

* Colors, Components & Sizes choices are defined within the Product model.


#### Events app
##### Event
| **Name** | **Database Key** | **Validation** | **Field Type** | 
--- | --- | --- | --- 
 Name | name | max_length=80 | CharField
 Description | description | max_length=254 | TextFeild
 Date | date | max_length=20 | DateTimeField
 Time | time | max_length=20 | DateTimeField 
 Price | price | max_digits=3, decimal_places=2  | DecimalField
 Price Comment | price_comment | max_length=120 | CharField
---



## CREDITS
#### CONTENT
The website is created by Alexey Statsenko, using the media described below. 

#### IMAGES
- All product(bikes, frames) & lifestyle photos were taken by the designer of the frames, Fabio Putzolu. All rights belong to FABIKE Design s.r.o. 


#### CODE
- Code for search dropdown menu was copied from CI's Boutique Ado project, and modified according to the current project's needs. Thanks Chris! ;-)



#### ACKNOWLEDGMENTS 


##### back to [top](#table-of-contents)