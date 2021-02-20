# FABIKE
## DESIGNED FOR EXPERIENCE

#### E-commerce website for a bicycle brand producing carbon fibre and titanium frames, selling them as well as fully assembled bicycles with high end components. (Full Stack project)

[![Build Status](https://travis-ci.org/OlekSt/Fabike.svg?branch=master)](https://travis-ci.org/github/OlekSt/Fabike)


<img src="" alt="Title image" style="margin: 0 10px;" width="100%"/>

[FABIKE - Heroku link](https://fabike.herokuapp.com/)

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
    - [**Heroku Deployment**](#heroku-deployment)
    - [**Local Deployment**](#local-deployment)

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


##### back to [top](#table-of-contents)


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


##### back to [top](#table-of-contents)


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

##### back to [top](#table-of-contents)


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

##### back to [top](#table-of-contents)

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

##### back to [top](#table-of-contents)


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

##### back to [top](#table-of-contents)

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

##### back to [top](#table-of-contents)

#### Checkout App
##### Order
| **Name** | **Database Key** | **Validation** | **Field Type** | 
--- | --- | --- | --- 
 Order Number | order_number | CharField | max_length=32, null=False, editable=False
 User | account | ForeignKey 'Account' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
 Full Name | account_full_name | max_length=70 | CharField
 Phone number | account_phone_number | max_length=25 | CharField
 Address | address | max_length=254 | TextField, ForeignKey 'Address'
 Town or City | town_or_city | max_length=80 | CharField
 Postcode | postcode | max_length=20 | CharField
 Country | country | blank_label='Country*' | CharField
 Purchase Date | purchase_date | auto_now_add=True | DateTimeField
 Order Total | order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
 Delivery Cost | delivery_cost | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
 Final Total Total | final_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
 Stripe Pid | stripe_pid | max_length=254, null=False, blank=False, default='' | CharField


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
* Colors, Components & Sizes choices will be added via other means, product views, Javascript.

##### back to [top](#table-of-contents)


    **Learning point: Data model for Products done at the beginning of the project didn't take into account some aspects of data manipulation, specifically creating a unique product record with a combination of model, color, size, components, etc. Based on the knowledge & experience I have obtained during the project's implementation, I'd plan a Product data model differently, i.e. each individual combination of a model, color, size, components would be given an individual sku code. This would simplify quite a number of processes within the following apps: cart, checkout.


#### Events/Workshops app
##### Event/Workshop
| **Name** | **Database Key** | **Validation** | **Field Type** | 
--- | --- | --- | --- 
 Title | title | max_length=80 | CharField
 Learning | Learning | max_length=254 | TextFeild
 Date | date | max_length=20 | DateTimeField
 Time | time | max_length=20 | DateTimeField 
 Address | address | max_length=80 | CharField
 Town or City | town_or_city | max_length=80 | CharField
 Price | price | max_digits=3, decimal_places=2  | DecimalField
 Comment | Comment | max_length=120 | CharField
---


##### back to [top](#table-of-contents)

## FEATURES 

### EXISTING FEATURES 

### FEATURES TO BE IMPLEMENTED


##### back to [top](#table-of-contents)

## TECHNOLOGIES USED

### LANGUAGES 
- HTML
- CSS
- Python
- Javascript
- Jinja

### LIBRARIES & FRAMEWORKS 
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://www.bootstrapcdn.com/)
- [Google Fonts](https://fonts.google.com/)
- [FontAwesome](https://fontawesome.com/)  
- [JQuery](https://jquery.com/)
- [Gunicorn](https://pypi.org/project/gunicorn/) - a Python WSGI HTTP Server to enable deployment to Heroku
- [Psycopg2](https://pypi.org/project/psycopg2/) - to enable the PostgreSQL database to function with Django
- [Stripe](https://stripe.com/ie) - for card payment process
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)

### TOOLS
- [GitPod](https://www.gitpod.io/) - IDE for developing this project
- [Git](https://git-scm.com/) - version control
- [GitHub](https://git-scm.com/) - storage of the project's repository
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools
- [Heroku](https://heroku.com/) - to host the project
- [AWS S3 Bucket](https://aws.amazon.com/) -  to store static and media files in prodcution
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for compatibility with AWS
- [Travis](https://travis-ci.org/) - for integration testing
- [Balsamiq](https://balsamiq.com/) - for wireframes
- [ColosSpace](https://mycolor.space/) - to create colour palette
- [Autoprefixer](https://autoprefixer.github.io/) - for adapting css to various browsers

### DATABASES
- [SQlite3](https://www.sqlite.org/index.html) - for development
- [PostgreSQL](https://www.postgresql.org/) - for production

##### back to [top](#table-of-contents)


## TESTING 

You will find all the info related to testing in [Testing.md file](Testing.md)

## DEPLOYMENT 

Gitpod was used as IDE to code this project. It was then committed and pushed to Github using the command line and deployed on Heroku PaaS platform, static and media files were uploaded to AWS S3. 
All versions and branches of the code are stored on [Github repository](https://github.com/OlekSt/Fabike).

### HEROKU DEPLOYMENT

Follow these steps to deploy the project to Heroku:

**In HEROKU:**

1. Create an new app in Heroku dashboard, choose closest region to you
2. Go to `Resources` & provision a new instance of PostgreSQL DB
    - Search for `Heroku Postgres` in ADDONS 
    - Choose Development plan

**In IDE**:

3. Run the following commands to install `dj_database_url` & `psycopg2-binary`:
- pip3 install dj_database_url
- pip3 install psycopg2-binary
4. Update requirements.txt:
- pip3 freeze > requirements.txt

**In settings.py**:

5. add `import dj_database_url` right after `import os`
6. Change Database:
```
DATABASES = {
    'default': dj_database_url.parse('....here goes a link for DB from Heroku Config Variables...')
}
```
**In IDE**:

7. Run migrations:
- python3 manage.py showmigrations
- python3 manage.py migrate

8. Load products & events data:
- python3 manage.py loaddata products
- python3 manage.py loaddata events

9. Create a superuser:
- python3 manage.py createsuperuser

**In settings.py**:

10. Change the Database settings as follows:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL from Heroku'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

```

##### back to [top](#table-of-contents)

**In IDE**:

11. Install gunicorn:
- pip3 install gunicorn”
12. Update requirements.txt:
- pip3 freeze > requirements.txt

**In general project's directory**:

13. Create a Procfile

**In IDE**:

14. Run the following command:
- web gunicorn django_name.wsgi:application
15. To login into heroku run:
- heroku login -i
16. Enter your email & password
17. Run the following command:
- heroku config:set DISABLE_COLLECTSTATIC=1 --app fabike

**In settings.py**:

18. To ALLOWED_HOSTS add ['https://fabike.herokuapp.com', 'localhost']


19.	Generate a new SCRET_KEY on Django Secret Key generator (find online)

**In Heroku**:

19. Add it to `Settings > Config Vars`,
20. Make sure you have other necessesary keys are setup there:
* AWS_ACCESS_KEY_ID	
* AWS_SECRET_ACCESS_KEY
* DATABASE_URL
* EMAIL_HOST_PASS
* EMAIL_HOST_USER
* SECRET_KEY
* STRIPE_PUBLIC_KEY
* STRIPE_SECRET_KEY
* STRIPE_WH_SECRET
* USE_AWS set to `True`

**In settings.py**:

21. Change SECRET_KEY to:
- SECRET_KEY = os.environ.get('SECRET_KEY', ' ')

**In IDE**:

22. Commit changes to Github:
- git push origin master
23. Push to Heroku:
- git push -u heroku master

Additionally 
**In Heroku**:

24. You can setup automatic deployment to Heroku when you commit changes to Githu:
- Go to Deploy
- Set deployment method to GitHub
- Find Fabike and connect
- Enable Automatic Deploys

The deployment has been completed.

##### back to [top](#table-of-contents)

##### Hosting media files with AWS
The static files and media files (product images) are hosted in the AWS S3 Bucket. To host them, you need to create an account in AWS and create your S3 basket with public access. 

##### Senging email with Gmail
To be able to send emails with Gmail, you need to connect it to your Gmail account, setting up your email address in EMAIL_HOST_USER variable and your app password generated by your email provider in EMAIL_HOST_PASS variable.



### Local Deployment
To be able to run this project, the following tools have to be installed:
- An IDE, e.g., [GitPod](https://www.gitpod.io/), or any other 
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python3](https://www.python.org/download/releases/3.0/)    

Besides you need to have/create accounts at:
- [Stripe](https://stripe.com/en-ie)
- [AWS](https://aws.amazon.com/) to setup the [S3 basket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- [Gmail](https://mail.google.com/)

Follow these steps:
1. Copy the repository by entering this in your IDE:
- git clone https://github.com/OlekSt/Fabike
2. Create .env file and add it to .gitignore to protect your sensitive variables
- env. file example:
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret key>"    
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"    
```

**In IDE**:

3. Install all the requirements: 
- pip3 install -r requirements.txt
4. Start the server:
- python3 manage.py runserver
5. Migrate the models for the DB
- python3 manage.py makemigrations
- python3 manage.py migrate
6. Load data using fixtures:
- python3 manage.py loaddata products
- python3 manage.py loaddata events
7. Create a superuser for admin 
- python3 manage.py createsuperuser
8. Start the server:
- python3 manage.py runserver

Now the project should be active on localhost port 8000. 
To access admin you need to add `/admin` at the end of the url.

##### back to [top](#table-of-contents)


## CREDITS
#### CONTENT
The website is created by Alexey Statsenko, using the media described below. 

#### IMAGES
- All product(bikes, frames) & lifestyle photos were taken by the designer of the frames, Fabio Putzolu. All rights belong to FABIKE Design s.r.o. 


#### CODE
- Code for search dropdown menu and search algorithm was copied from CI's Boutique Ado project, and modified according to the current project's needs. Thanks, Chris! ;-)
- HTML/CSS code for color radio buttons on bike.html was taken from https://uicookies.com/bootstrap-radio-button-styles/ and modified according to the needs of the project. 
- HTML/CSS code for size and components selector was taken from https://freefrontend.com/css-radio-buttons/ and modified according to the needs of the project. 
- Code for toasts was copied from CI's Boutique Ado project, and modified according to the current project's needs.
- Code for cart including calc_subtotal templatetags was copied from CI's Boutique Ado project, and modified according to the current project's needs.
- Code for checkout app was partly copied from CI's Boutique Ado project, and modified according to the current project's needs.
- Code for profile was partly copied from I's Boutique Ado project, and modified according to the current project's needs.


#### ACKNOWLEDGMENTS 


##### back to [top](#table-of-contents)