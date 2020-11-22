![V-Choco](media/v-choco-logo-readme.png)
# *V-Choco* - Fourth Milestone Project for Code Institute
*V-Choco* is a webshop that offers dairy-free chocolate for people who are either allergic to dairy or choose to avoid it.

A live preview of the website can be found here: [V-Choco](https://vchoco.herokuapp.com/)

## Table of Contents

1. [UX Design](#ux-design)
    * [User Stories](#user-stories)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
1. Database Structure
1. Features
1. Technologies Used
1. Testing
1. Deployment
1. Credits

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

**Site Admin**
I want to... | So that I can ...
Add new products | sell them on the website
Edit product details | keep the website up-to-date
Delete products | remove items from the website that are not in stock
View a list of email subscribers | send emails with the latest news and remove people when asked

### Strategy
The primary goal of this website is to offer users a pleasant and straightforward shipping experience so that they will continue to order from *V-Choco* in the future. In order to accomplish this, the website has a navigation bar with links to all the different products and an overal layout that is common for webshops. The website will also feature a **My Account** section for customers who have registered their details, making future orders quicker to complete.

### Scope
The users need the following from the website:

* A Landing Page that is easy to navigate.
* A navigation bar with a shopping cart and user section that changes depending on whether the user is logged in or not.
* A register and login form for users to either create a new account or to log in.
* A My Account Page for users to view their previous orders and default details.
* A Sign Out button that is easy to find on every page (preferably in the navigation bar).
* A Product Details page for potential customers to decide whether or not they want to purchase the product.
* A reviews section on each Product Details page in order to see what previous buyers think about the product.
* A way to sort products by category when viewing all products.
* An option to search the entire site for a specific product.
* An option to add products to the cart.
* A page for viewing/updating/removing the contents of the shopping cart and with a button to go to the checkout page.
* A secure checkout form to complete orders.
* A confirmation page and email when an order has been placed.
* The ability to review products when signed in.

### Structure

Django was used for this project in order to make an interactive full-stack website that shows users different content depending on their activity.

A traditional navigation bar was implemented at the top of each page with the common "Tree Structure". This bar changes depending on whether a user is currently logged in. If so, it includes links to the Home, Products, My Account, Cart, and Log Out pages. If not, it includes links to the Home, Products, Log In, Register, and Cart pages.

Color Scheme: The background of the website and navigation bar are both white. This neutral base is needed as the other colors on the website are quite bright. Dark grey is used for all of the font on the website. All of the buttons are white and light grey when hovered over. The free shipping banner, reviews carousel on the homepage, and product cards on the products page, are all pink. The navbar font and logo font are a light sea-green and a darker sea-green when hovered over. The alert messages are the standard bootstrap info, danger and success colors (blue, red and green).

![Website Colors](media/website-colors.png)

Typography: [Karla](https://fonts.google.com/specimen/Karla) was used for the entire website.

Icons: Icons from [FontAwesome](https://fontawesome.com/) were used in the navigation bar for User Account and Shopping Cart to minimize text used. Buttons across the site also have FontAwesome icons. 

### Skeleton
[Click here](static/wireframes) to see all wireframes for this project.

*Please note that the wireframes show the initial design ideas for the website and therefore may not match the current version.*

[Back to Top](#table-of-contents)

