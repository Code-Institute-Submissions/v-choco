![V-Choco](media/v-choco-logo-readme.png)
# *V-Choco* - Fourth Milestone Project for Code Institute
*V-Choco* is a webshop that offers dairy-free chocolate for people who are either allergic to dairy or choose to avoid it. It was created using all of the knowledge gained during the Full Stack Web Development course. 

A live preview of the website can be found here: [V-Choco](https://vchoco.herokuapp.com/)

To test the payment functionality on the website page, use the following details:

Address: Any address\
Card number: 4242 4242 4242 4242\
CVC: Any 3 digit digits\
Postcode: Any 5 digits\
Expiration Date: Any future date

## Table of Contents

1. [UX Design](#ux-design)
    * [User Stories](#user-stories)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
1. [Database Structure](#database-structure)
1. [Features](#features)
1. [Technologies Used](#technologies-used)
1. [Testing](#testing)
1. [Deployment](#deployment)
1. [Credits](#credits)
1. [Acknowledgements](#acknowledgements)

## UX Design

### User Stories

**Site Visitors**

I want to... | So that I can ...
------------ | -----------------
View all products | choose what I want to purchase
View product details | decide whether I want to purchase this item
View my shopping cart total at any time | make sure I spend the amount I want to spend
Checkout securely | complete my order
Register for an account | easily purchase again in the future
Log in and log out | access my account details and order history
Reset my password if I lost it | access my account again
Receive email confirmations | confirm that I have been registered or that my order was placed
See my order history | reorder products I liked in the past
Post reviews on products I have purchased | share my opinion with others
Sort products by categories | easily select the product I want to purchase
Subscribe to the newsletter | hear about the latest deals

**Site Admin**

I want to... | So that I can ...
------------ | -----------------
Add new products | sell them on the website
Edit product details | keep the website up-to-date
Delete products | remove items from the website that are not in stock
View a list of email subscribers | send emails with the latest news and remove people when asked

### Strategy

The primary goal of this website is to offer users a pleasant and straightforward shopping experience so that they will continue to order from *V-Choco* in the future. In order to accomplish this, the website has a navigation bar with links to all the different products and an overal layout that is common for webshops. The website will also feature a **Account Details** page for customers who have saved their shipping details, making future orders quicker to complete.

### Scope

The users need the following from the website:

* A landing page that is easy to navigate.
* A navigation bar with a shopping cart and user section that changes depending on whether the user is logged in or not.
* A register and login form for users to either create a new account or to sign in.
* An *Account Details* page for users to view their previous orders and default details.
* A *Sign Out* button that is easy to find on every page (preferably in the navigation bar).
* A *Product Details* page for potential customers to decide whether or not they want to purchase the product.
* A reviews section on each *Product Details* page in order to see what previous buyers think about the product.
* A way to sort products by category when viewing all products.
* An option to search the entire site for a specific product.
* An option to add products to the cart.
* A page for viewing/updating/removing the contents of the shopping cart and with a button to go to the checkout page.
* A secure checkout form to complete orders.
* A confirmation page and email when an order has been placed.
* The ability to review products when signed in.

### Structure

Django was used for this project in order to make an interactive full-stack website that shows users different content depending on their activity.

A traditional navigation bar was implemented at the top of each page with the common "Tree Structure". This menu changes depending on whether a user is currently logged in. If so, it includes links to the Home, Products, Account Details, Cart, and Sign Out pages. If not, it includes links to the Home, Products, Sign In, Sign Up, and Cart pages.

Color Scheme: The background of the website and navigation bar are both white. This neutral base is needed as the other colors on the website are quite bright. Dark grey is used for all of the font on the website. All of the buttons are white and light grey when hovered over. The free shipping banner, reviews carousel on the homepage, and product cards on the products page, are all pink. The navbar font and logo font are a light sea-green and a darker sea-green when hovered over. The alert messages are the standard bootstrap info, danger and success colors (blue, red and green).

![Website Colors](media/website-colors.png)

**Typography:** [Karla](https://fonts.google.com/specimen/Karla) was used for the entire website.

**Icons:** Icons from [FontAwesome](https://fontawesome.com/) were used in the navigation bar for the user account and shopping cart links to minimize text used. Buttons across the site also have FontAwesome icons. 

### Skeleton

[Click here](static/wireframes) to see all wireframes for this project.

*Please note that the wireframes show the initial design ideas for the website and therefore may not match the current version.*

[Back to Top](#table-of-contents)

## Database Structure

### Marketing App

The model in this app allows users to sign up to the newsletter on the website.

**Newsletter Signups Model**

Name | Database Key | Field Type | Validation
---- | ------------ | ---------- | -----------
Email | email | EmailField | unique=True
Time Added | timestamp | DateTimeField | auto_now_add=True

### Profiles App

The model in this app allows users to create an account and save their default shipping address.

**User Profile Model**

Name | Database Key | Field Type | Validation
---- | ------------ | ---------- | -----------
User | user | OneToOneField | User, on_delete=models.CASCADE
Full Name | default_full_name | CharField | max_length=50, null=True, blank=True
Address 1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
Address 2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
Town or City | default_town_or_city | CharField | max_length=40, null=True, blank=True
Postcode | default_postcode | CharField | max_length=20, null=True, blank=True
County | default_county | CharField | max_length=80, null=True, blank=True
Country | default_country | CountryField | blank_label="Country", null=True, blank=True
Phone Number | default_phone_number | CharField | max_length=20, null=True, blank=True

### Products App

The models in this app store all the products and their reviews on the website.

**Category Model**

Name | Database Key | Field Type | Validation
---- | ------------ | ---------- | -----------
Name | name | CharField | max_length=254
Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True

**Product Model**

Name | Database Key | Field Type | Validation
---- | ------------ | ---------- | -----------
Category | category | ForeignKey | 'Category', null=True, blank=True, on_delete=models.SET_NULL
SKU | sku | CharField | max_length=254, null=True, blank=True
Name | name | CharField | max_length=254
Description | description | TextField | 
Price | price | DecimalField | max_digits=4, decimal_places=2
Image URL | image_url | CharField | max_length=1024, null=True, blank=True
Image | image | ImageField | null=False, blank=False

**Product Review Model**

Name | Database Key | Field Type | Validation
---- | ------------ | ---------- | -----------
Product | product | ForeignKey | Product, related_name="reviews", on_delete=models.CASCADE
User | user | ForeignKey | User, related_name="reviews", on_delete=models.CASCADE
Content | content | CharField | max_length=254, null=True, blank=True
Rating | rating | IntegerField | 
Date Added | timestamp | DateTimeField | auto_now_add=True

### Checkout App

The models in this app allow users to add products to their cart and create an order.

**Order Line Item Model**

Name | Database Key | Field Type | Validation
---- | ------------ | ---------- | -----------
Order Number | order | ForeignKey | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product | product | ForeignKey | Product, null=False, blank=False, on_delete=models.CASCADE
Quantity | quantity | IntegerField | null=False, blank=False, default=0
Line Item Total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False

**Order**

Name | Database Key | Field Type | Validation
---- | ------------ | ---------- | -----------
Order Number | order_number | CharField | max_length=32, null=False, editable=False
User Profile | user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL,null=True, blank=True, related_name='orders'
Full Name | full_name | CharField | max_length=50, null=False, blank=False
Email | email | EmailField | max_length=254, null=False, blank=False
Phone Number | phone_number | CharField | max_length=20, null=False, blank=False
Country | country | CountryField | blank_label="Country *", null=False, blank=False
Postcode | postcode | CharField | max_length=20, null=True, blank=True
Town or City | town_or_city | CharField | max_length=40, null=False, blank=False
Address 1 | street_address2 | CharField | max_length=80, null=False, blank=False
Address 2 | street_address2 | CharField | max_length=80, null=True, blank=True
County | county | CharField | max_length=80, null=True, blank=True
Date | date | DateTimeField | auto_now_add=True
Shipping Cost | shipping_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
Subtotal | total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Grand Total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
Original Cart | original_cart | TextField | null=False, blank=False, default=''
Stripe ID | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

[Back to Top](#table-of-contents)

## Features

### Existing Features

#### Navigation Bar

The navbar stays the same on all pages, making navigating the website straightforward. It collapses to the popular hamburger icon on smaller devices in order to save screen space.

There is a banner above the navbar that lets the user know whether they have qualified for free shipping. If they haven't, it will show how much more they need to spend.  

If the user is not authenticated, they will see links to the Home, All Products, Seasonal Selection, Sign Up, Sign In, and Shopping Cart pages. 

If the user is authenticated but not a superuser, they will see links to the Home, All Products, Seasonal Selection, Account Details, Sign Out, and Shopping Cart pages. If the user is a superuser, they will see all the same options plus a link to Add Product, which will allow them to add a product.

There is also a search icon that allows users to search for specific keywords.

When hovering over the links their color will change to a darker color in order to give feedback to the user.

#### Home Page

The landing page of the website. At the top of the page is a carousel with different images that link to the different products pages. This carousel is meant to be updated with new deals or products as the time goes on.

Below the carousel is an infographic explaining why people should choose for plant-based chocolate. Next to the infographic are a reviews carousel which shows the latest feedback given by customers, and a form that allows users to sign up to the newsletter. If a new user signs up to the newsletter a message will pop up letting them know they have been subscribed. If a person tries to subscribe twice an error message will appear.

At the bottom of the page is another newsletter signup form that does the same as the one next to the infographic.

#### Sign Up Form

This allows new visitors to create an account. If an account with the entered email or username already exists, the user will get an error message asking to try again.

In case users already have an account and want to sign in instead, there are links at the top and bottom of the form that will take them to the Sign In page.

#### Sign In Form

This form allows existing users to sign in using their username and password. An error message will appear if an invalid username/password is entered.

There is an option at the top of the form to go to the sign up page if they don't have an account yet. 

At the bottom of the form is a tick box to "remember me" for the future, and a "forgot password" link. 

#### Account Detail Page

This page is only available to authenticated users. It shows the default shipping address if they have saved it in the past, and the ability to edit/update this address. It also shows any past orders if the user has made any and if the user clicks on the order number it will take them to the complete order summary.

#### Products Pages

There are three different products pages. One that shows all the products, one that shows the seasonal items, and one that shows all the bonbons. 

When on the All Products page, there are two buttons on the top of the page that allow users to go to specific categories. When viewing one of the categories, there is a button at the top which can take them back to the All Products page.

In the top left corner it shows how many products are on the page.

Each product listed has an image, a price, a title and reviews if applicable.

If a user uses the search bar at the top of the page they will be redirected to the products page with any relevant search results.

To see more details of a product, the user will need to hover over the image and click on the plus.

If the user is a superuser, there will be the options to edit and delete the product right underneath each product card.

#### Product Detail Page

This page has all the product information on it for users to view before choosing whether or not to purchase the product. These include the product image, name, price, rating and description.

The user has the ability to add the specified amount to their cart by first selecting the amount they want in the quantity input field and then pressing the add to cart button. When they press this a message will pop up confirming that the product has been added to the cart, and will show a summary of their cart with the option to either view their cart or go to the checkout page.

If the user is a superuser, there will be the options to edit and delete the product right underneath the Add to Cart button.

At the bottom of the page is the reviews section. If the product has any reviews they will appear here. If the user is authenticated they will be able to add a review to the page as well. If not, they will have the option to sign in. 

#### Add a Product Page
A page only available to superusers. It has a simple layout with only a form including the following input fields: Category, SKU, Name*, Description*, Price*, Image url, Image*. Filling this form out will add a new product to the database and website.

#### Edit a Product Page

Similar to the Add a Product page. Only difference is that the current values of each input field are filled in by default. 

#### Shopping Cart

The page to view all the items that have been added to the shopping cart. If the shopping cart is empty it will say "Your cart is empty" with a button to "Start Shopping". 

If there are items in the cart, there will be a table showing a summary of all the products, the amount in the cart, and the price of each. There is also the ability to update the quantity of each item or remove them completely from the cart. If anything is updated, the page will be reloaded and a success message will appear letting the user know that their cart has been updated. 

At the bottom of the page are the subtotal, the shipping costs and the grand total. There is also a sentence letting the user know if they don't qualify for free shipping and how much more they need to spend to qualify. Below that there are two buttons, one to keep shopping and one to go to the checkout page.

#### Checkout Page

This page includes an order summary table and a form. The order summary table is very similar to the Shopping Cart page, but without the options to edit/remove any products. The form includes input fields for contact information, a shipping address, and payment details.

If the user is not authenticated it will give the user the option to sign in or create an account to save the details for future orders. If the user is authenticated they will simply be able to select the box at the bottom of the page to save the information. 

Once the submit order button is pressed, it will be disabled and replaced with a loading button while the payment processes. As soon as it has been processed the user will be sent a confirmation email and taken to the order confirmation page.

#### Order Confirmation Page

This page once again shows a summary of the order and lets the user know that their order has been successful and that they will receive a confirmation email. 

If the user is authenticated they will have an option to go to their account.

### Hopeful Future Features

* The ability to log in using social media
* More payment options (Paypal etc.)
* The ability to "delete your account" and "unsubscribe from the newsletter" on the My Account page
* A Contact Us page
* The option for users to "create their own box" and choose which bonbons they specifically want
* A pop-up to confirm whether the superused wants to delete a product when pressing the Delete option on the Products/Product Details pages
* The ability to manage stock and remove items from the website if they are out of stock

[Back to Top](#table-of-contents)

## Technologies Used

### Languages

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Javascript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/)

### Libraries/Frameworks

* [Django](https://www.djangoproject.com/) : Main web framework used.
* [Bootstrap](https://www.getbootstrap.com/) : Used for initial styling and in order to create a uniform website that renders well on all screen sizes. Also used for some basic Javascript additions.
* [Jquery](https://jquery.com/) : Used in a lot of the bootstrap styling and additional Javascript on the website.
* [Google Fonts](https://fonts.google.com/) : Used for the font on the website.
* [Font Awesome](https://fontawesome.com/) : Used for social media icons.

### Tools

* [Visual Studio Code](https://code.visualstudio.com/) : The code editor used for this project.
* [Git](https://git-scm.com/) : Installed on VS Code to allow version control.
* [Balsamiq Mockups](https://balsamiq.com/) : Used to create the wireframes during the UX Design process.
* Chrome Developer Tools: Used to test the website while developing.
* [W3C Markup Validation Jigsaw](https://jigsaw.w3.org/css-validator/) : To validate the CSS code.
* [W3C Markup Validation](https://validator.w3.org/) : To validate the HTML code.
* Github : Used to host the repositories for this project.
* [Canva](https://www.canva.com/) : Used to resize images and create logo.
* [Heroku](https://heroku.com/) : Used to host the website.
* [AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html): Used for user registration and authentication. 
* [Crispy-Forms](https://django-crispy-forms.readthedocs.io/en/latest/) : Used to build the forms on the website
* [Gunicorn](https://gunicorn.org/) : A Python WSGI HTTP server required for deploying to Heroku
* [Boto3](https://pypi.org/project/boto3/) : Required to set up and manage AWS services, like S3.
* [Psycopg2](https://pypi.org/project/psycopg2-binary/) : Needed for the Postgres database
* [Pillow](https://pillow.readthedocs.io/en/stable/) : Required for images with Python interpreter 
* [AWS S3 Bucket](https://aws.amazon.com/s3/) : Used to store the media and static files
* [Stripe](https://stripe.com/) : Used to process payments and webhooks on the checkout page

### Databases

* [SQlite3](https://www.sqlite.org/index.html) - The database used when in development
* [PostgreSQL](https://www.postgresql.org/) - The database used when deployed to Heroku

[Back to Top](#table-of-contents)

## Testing

Chrome Developer Tools was used the entirety of my project to test out how the website rendered on different viewports/devices. By using the device selector I went through each screen size to confirm that everything looked correct each time I changed anything.

The website has been tested on Google Chrome, and Safari for mobile and web. 

[Am I Responsive]() was used throughout the process to ensure that the website rendered well on different screen sizes.

### Validation Testing

* HTML: W3C Markup Validation Service was used to validate. There were many errors due the program not accepting Jinja.
* CSS: W3C CSS Validation Service was used to validate. No errors were found.
* Python: Flake8 was used to validate. There were initially a lot of errors about lines being too long so those were fixed. There is only one line that I wasn't able to shorten without breaking the code.

### User Stories Testing

**Site User**

* I want to view all products
    * Head to the home page of the website
    * Select All Products on the navigation bar

* I want to view product details
    * Head to the home page of the website
    * Select All Products on the navigation bar, or search for a specific product/category
    * Click on a product image

* I want to view my shopping cart total at any time
    * If the shopping cart total isn't 0 it will appear next to the cart icon on the navbar
    * This can be tested by adding any product to the cart

* I want to check out securely
    * Head to the products page and add a product to the cart
    * View cart and select Secure Checkout
    * Fill in shipping details and payment details (powered by stripe)
    * Submit order and receive a confirmation email

* I want to register for an account
    * Head to the home page
    * On the navigation bar, click on the user icon and select sign up
    * Fill in the form correctly and press the sign up button
    * Get redirected to a page saying a confirmation email has been sent
    * Check email and click on the confirmation link in the email

* I want to log in and log out
    * Head to the home page
    * Select the user icon on the navigation bar
    * Select Sign In
    * Fill in username and password
    * Get redirected to the home page with a message saying that the sign in was successful
    * To sign out, select the same user icon as before
    * Select the Sign Out option
    * Get redirected to a confirmation page and select Sign Out again

* I want to reset my password if I lost it
    * Head to the home page
    * Select the user icon
    * Select sign in 
    * Select the Forgot Password option
    * Fill in email address
    * Select Reset My Password
    * Follow the instructions in the email

* I want to receive email confirmations
    * When an order has been confirmed or a new account has been created the user will receive email confirmations

* I want to see my order history
    * Head to the home page
    * If not already signed in, select the user icon and sign in
    * If signed in, select the user icon
    * Select Account Details
    * Order history will appear on the right on larger screens

* I want to post reviews on products that I have purchased
    * Head to the product details page of the product
    * Scroll to the reviews section
    * If not already signed in, press the option to sign in first
    * If signed in, fill out the review form and select Add Review 

* I want to sort products by categories
    * Head the products page
    * Underneath the title All Products, there are two buttons - one for each category
    * Press either button and get redirected to a page with all the products in that category

* I want to subscribe to a newsletter to hear about the latest deals:
    * Head to the homepage of the website
    * Scroll to the very bottom
    * In the newsletter signup form, enter an email and select the subscribe button
    * Page refreshes with a success message saying the user has been registered


**Site Admin**

* I want to add new products
    * Head to the home page
    * Select the user icon and sign in
    * Sign in as a superuser and get redirected to the home page
    * Select the user icon again and select Add Product
    * Fill in all the required fields and select the Add Product button

* I want to edit product details
    * Head to the products page
    * Click on the edit option below the product
    * Change the details that need to be updated in the edit form
    * Select the Update button

* I want to delete a product
    * Head to the products page
    * Click on the delete option below the product

* I want to view a list of email subscribers
    * Head to the admin of the site: https://vchoco.herokuapp.com/admin/
    * Click on Newsletter Signups under Marketing

### Manual Testing

✔️ Navigation links when not logged in/logged in/logged in as superuser: All redirect to the correct pages

✔️ Misc. links on website: All links are working correctly and not throwing any errors.

✔️ Try loading My Account page when not logged in: Get redirected to sign in page.

✔️ Try loading Add Product page when not logged in: Get redirected to sign in page.

✔️ Submit registration form with a user/email that already exists in database: An error message appears.

✔️ Submit registration form with one of the fields not filled in: An error message appears asking user to fill in the field.

✔️ Submit registration form with a new user/email that doesn't exist in database: Successfully sends user data to Django and sends a confirmation email.

✔️ Click on the confirm registration link in email: Get sent to a page asking to confirm the account. Once confirmed the sign in page appears.

✔️ Submit Log In form if no username exists in database that matches entered username: Error message appears and asks user to try again.

✔️ Submit Log In form if username is correct but password doesn't match: Error message appears and asks user to try again.

✔️ Submit Log In form with one of the fields not filled in: An error message appears asking user to fill in the field.

✔️ Submit Log In form with correct username and password: Starts session and takes user to Home Page with a success message appearing.

✔️ Press the Sign Out button when logged in: Takes user to confirmation sign out page. Once confirmed it ends the session and sends user back to the home page

✔️ Try adding a product when logged in as superuser: Successfully creates a product and redirects user to the product page only if all the fields are filled in correctly. If not, an error message appears.

✔️ Try editing a product on the products page when logged in as superuser: Successfully updates product and redirects user to the product page only if all the fields are filled in correctly. If not, an error message appears.

✔️ Try deleting a post while on the products page: Product immediately gets deleted from database

✔️ Try navigating to Log In page when already logged in: Get redirected to Home page.

✔️ Try navigating to Register page when already logged in: Get redirected to Home page.

✔️ Select different categories buttons on products page: Get redirected to a page showing only the products in that category with a buttom at the top to view all products.

✔️ Try searching for a term that doesn't exist in products: Receive 0 results and a button to go back to all products.

✔️ Try searching for a term that does exist (ie bonbon): Get redirected to a page with all products that have that term in their title or description.

✔️ Try going to the shopping cart with no products added: Page says that there are no products in shopping cart and includes a button to start shopping.

✔️ Try going to the checkout page with an empty cart: Get an error message saying the cart is empty.

✔️ Try adding a product to the cart by going to the product details page and selecting the add to cart button: Get a message showing cart summary and that the product has been added. 

✔️ Try removing an item from the cart in the message that pops up when adding an item: Get a message saying the product has been removed from the cart.

✔️ Try removing an item from the cart on the shopping cart page: Get a message saying the product has been removed from the cart. 

✔️ Try updating the total quantity  of the items in the cart: Get a message saying the product has been updated and the total/grand total is updated at the bottom as well.

✔️ Try submitting an order using the Stripe test details: Successful only if all the fields are filled in properly, otherwise an error appears. Get redirected to an order confirmation page and have the email forwarded. 

✔️ Try closing the checkout page while the order is being processed: Still receive a confirmation email as the webhook handled the order successfully.

✔️ Select "Save this information for next time" on checkout page while signed in: Head to the My Account page after successfully completing the order and the address has been saved.

✔️ Try editing the default shipping information on the My Account Page: Successfully updates the information

✔️ Try making another order after having the default information saved: The form on the checkout page is filled out with the default address.

✔️ Try subscribing to the newsletter on the homepage with a new email: Get a success message that the user has been subscribed.

✔️ Try subscribing to the newsletter on the homepage with a email that has already been subscribed in the past: Get an error message letting the user know that they are already subscribed.

[Back to Top](#table-of-contents)

## Deployment

*V-Choco* has been built with the help of Visual Studio Code, a desktop code editor. It has been committed to Git and Pushed to GitHub using the terminal in Visual Studio Code. the website is hosted on Heroku.

### Cloning

**Clone the repository and run locally:**

1. Navigate to the repository from the Github Dashboard
1. Select the green button in the top right of the screen that says "Clone or download"
1. Click on the clipboard icon to the right of the URL to copy it
1. Open an Integrated Development Environment (IDE) and head over to the terminal
1. Change the directory to where you want to clone the repository to
1. Execute the following command by pasting in the URL you copied in step 3: git clone https://github.com/debrawolford/v-choco.git
1. Press Enter
1. The site will then be cloned
1. Install all the project dependencies by typing pip install -r requirements.txt
1. Create an env.py file in your root directory.
1. Add env.py file to the.gitignore file.
1. Add the following to your env.py file with the applicable variables:

KEY | VALUE
--- | -----
DATABASE_URL | Your database url
SECRET_KEY | Your secret key that you used for your Django project
STRIPE_PUBLIC_KEY | Obtained from Stripe
STRIPE_SECRET_KEY | Obtained from Stripe
STRIPE_WH_SECRET | Obtained from Stripe

### Deploying on Heroku

1. Follow the steps above to clone your project.
1. Go to your Dashboard in Heroku and select New -> Create New App.
1. Give your app a name and select your region.
1. Go to the Resources tab and search for Postgres, select it as a free add-on.
1. Add the following Config Vars in the settings tab:

KEY | VALUE
--- | -----
DATABASE_URL | Your Postgres database url
SECRET_KEY | Your secret key that you used for your Django project
STRIPE_PUBLIC_KEY | Obtained from Stripe
STRIPE_SECRET_KEY | Obtained from Stripe
STRIPE_WH_SECRET | Obtained from Stripe

1. Go to the Deploy tab and select GitHub as your Deployment method.
1. Follow the instructions to connect to the correct Github repository.
1. Enable Automatic Deploys. This will deploy the website each time the master branch is updated.
1. If you prefer to deploy manually, head to the Manual Deployment section, choose the master branch, and select Deploy.
Your website should now be live.

### Sending Confirmation Email through Gmail

To send the registration and order confirmation emails, you will need to set up a gmail account and enable two-step authentication in your security settings and set up an app password. Once you have these you will need to set the following in your Heroku config vars:

KEY | VALUE
--- | -----
EMAIL_HOST_PASS | The password you created in App Passwords
EMAIL_HOST_USER | Your Gmail account (...@gmail.com)

### Hosting your files on AWS

The static and media files for this website are saved in an AWS S3 Bucket. In order to deploy this project, you will need to create an AWS account and then set up your AWS S3 Bucket, making sure you allow public access. Once you have done this, you will need to add the following to your Heroku config vars:

KEY | VALUE
--- | -----
AWS_ACCESS_KEY_ID | Given to you while setting up your bucket
AWS_SECRET_ACCESS_KEY | Given to you while setting up your bucket
USE_AWS | True


[Back to Top](#table-of-contents)

## Credits

### Content

I initially followed along with the Boutique Ado mini project from Code Institute to create the first few models of my site.

I roughly followed the tutorial by [Yuksel CELIK, PhD](https://www.youtube.com/watch?v=OvTs8BMLb7o) for setting up the product reviews models. It was later adapted to suit my project.

### Media

All the images on this website were created using [Canva](https://www.canva.com/), a website that lets you create content with a library of stock images.

[Back to Top](#table-of-contents)

## Acknowledgements

Thanks to my mentor, Dick Vlaanderen for providing helpful feedback throughout the project.

Thanks to the Slack community for helping me resolve some errors while deploying to Heroku.

[Back to Top](#table-of-contents)