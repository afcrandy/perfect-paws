# Perfect Paws Dog Grooming Salon

Perfect Paws Dog Grooming Salon is a full stack B2C website built using Python (Django), HTML, CSS and JavaScript, where customers can view and book dog grooming services.

This project was created as my fourth milestone project for my Level 5 Diploma in Full Stack Software Development with the Code Institute.

[Live site here](https://perfect-paws-project-4-eff4ed411622.herokuapp.com/)

![amiresponsive screenshot](documentation/perfect_paws_amiresponsive.png)

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)

---

## User Experience (UX)

### Project Goals
Edinburgh has been recently identified as one of the UK’s most dog friendly cities, with an estimated 24% of the population owning dogs. Because of this, dog grooming services are in high demand, and Perfect Paws Dog Grooming Salon aims to address this growing market. The core purpose of the website is to provide information to prospective and returning clients about what dog grooming services are offered and how much they cost, to allow customers to book in grooming services online, provide information about where to find and how to contact the business, offering a streamlined service.

#### Key information for the site

- What dog grooming services are offered and what they cost.
- Find out more about the business.
- Find out how to book an appointment.
- What dates and times are available for the selected service.
- How to contact the business to ask a question.
- Where to find the business.

#### Client goals

- To be able to view and access the site on a variety of device sizes.
- To streamline the booking process by allowing clients to book online.
- To clarify what services are offered and how much they cost.
- To provide available times and dates for selected services.
- To provide information about where the business is located.
- To allow people to contact the business to ask a question or modify appointments.

#### First time user

- I want to find out more about Perfect Paws and what services are offered.
- I want the site to be easy to navigate and make it clear where to find information.
- I want to find out how to book an appointment.
- I want to book an appointment and find out what dates and times are available.
- I want to contact the business and ask a question.
- I want to find out where the business is located.

#### Returning user

- I want to find out up-to-date information about services and pricing.
- I want to book another appointment for my dog and find out what times and dates are available.

#### Frequent user

- I want to book repeat appointments for dog grooming.
- I want to stay up to date on any changes to services offered or promotions.

### User Stories

| User Story ID | As a/an | I want to be able to ... | So that I can... | Acceptance Criteria |
|--------------|--------|------------------------|----------------|--------------------|
| **VIEWING & NAVIGATION** |
| 1 | User | Easily navigate the site | Find information and book services that I need | * Navbar is stuck to top of the browser window<br>* Links are clearly labelled and easy to click |
| 2 | User | View what dog grooming services are offered | Find information about specific services I may need | * Services page lists all available services |
| 3 | User | Find out more information about the business | Find out how much experience the groomer has and their qualifications | * Home page has information about Perfect Paws |
| 4 | User | Find out how to contact the business | In case I want to ask a question, change or cancel an appointment | * Contact Us page has business email, phone number and a location map |
| 5 | User | Submit an enquiry | Ask a question | * Contact Us page has a Send a message form<br>* Form won’t submit without required fields filled |
| 6 | User | Determine where the business is located | Know where to bring my dog for the appointment or visit the business in person | * Contact Us page has address and map |
| 7 | User | See Perfect Paws’s social media sites | Follow the business on social media, read their announcements or see past grooms | * Footer has links to social media profiles |
| 8 | User | See a register or login button if I am not logged in | Know if I need to log in or register | * Navbar has Register and Login buttons for logged-out users |
| 9 | User | See a logout button when I’m logged in | Logout of the site | * Navbar has a Logout button for logged-in users |
| 10 | Site owner | See an admin button when logged in | Access the admin panel | * Admin users see an Admin button in the navbar |
| **REGISTRATION & USER ACCOUNTS** |
| 11 | User | Register for an account | Have an account to book services | * Non-logged-in users can register via sign-up page |
| 12 | User | Log in and out | Book appointments and keep personal details secure | * Login page allows users to sign in<br>* Logout option available for signed-in users |
| 13 | User | Reset my password | Recover my account or change my password | * Users can request a password reset from login page |
| 14 | User | Login or register if I try to book while not logged in | Create an account and book a service | * Non-logged-in users trying to book are redirected to login page |
| 15 | User | View my profile page | Update my information | * Profile page displays user details<br>* Users can update email, names and phone number |
| 16 | User | Delete my account | No longer make bookings | * Profile page has Delete Account button with confirmation prompt |
| **BOOKING & CONFIRMATION** |
| 17 | User | Select the service I want to book | Get an appointment for my dog | * Booking page has a booking form with required fields |
| 18 | User | Check available dates and times | Choose a convenient appointment slot | * Date picker only shows available slots |
| 19 | User | Only see time slots available for the service I want to book | Avoid booking unavailable times | * Time slots update based on selected service |
| 20 | User | Complete my booking | Confirm my appointment | * Booking form does not submit without required details |
| 21 | User | See a booking confirmation message | Ensure my booking went through | * Success message appears after booking |
| 22 | User | Receive an email confirmation after booking | Keep a record of my booking | * Confirmation email sent with appointment details |
| **ADMIN & SITE MANAGEMENT** |
| 23 | Site owner | Add a dog grooming service | Offer new services | * Admin panel allows adding new services |
| 24 | Site owner | Edit or update a service | Change prices, descriptions and promotions | * Admin panel allows editing services |
| 25 | Site owner | Suspend a service | Temporarily remove services | * Admin can mark services as inactive |
| 26 | Site owner | View enquiries | Respond to customer queries | * Admin panel displays customer enquiries |
| 27 | Site owner | Mark an enquiry as responded to | Track which queries are answered | * Admin can mark enquiries as read |
| 28 | Site owner | View bookings | Keep track of appointments | * Admin can see all bookings in the admin panel |
| 29 | Site owner | Modify bookings | Make changes when necessary | * Admin can edit bookings in the admin panel |
| 30 | Site owner | Mark a booking as cancelled | Record cancelled appointments | * Admin can cancel bookings and record the date of cancellation |

## Design

### Colour Scheme

The colour palette for the site is based around the hero image found on the home page. This image includes a lavender pink (Hex code EDA6CE) background, which provides a bright pop of colour. The lighter pink (FEDBF0) utilised as a background for the main page element is a less saturated version of this pink to remain cohesive with the hero image. Pink as a colour is often associated with beauty products and fits with the ‘salon’ theme of the site. The site also utilises a white (FFFFFF) background to add white space and balance the site design. Prussian blue (0E273F) text and buttons used throughout provide a dark contrast for the bright pink and white tones.

![Colour Palette](documentation/colour_palette.png)

### Typography

Google fonts and Dafont were used to source the chosen fonts for the website. The Dafont font was downloaded and stored in an appropriate assets/fonts directory, the Google Fonts were implemented via CDN.

- Within the home page, I used Dogma Script from dafont for the Perfect Paws logo. This font is in a modern calligraphy style and stands out from the other fonts used within the site to draw attention and provide contrast.
![Dogma Script sample](documentation/dogma_script_sample.png)

- Libre Baskerville from Google Fonts was used for headings throughout the site. This font is a classic serif font, which contrasts with the fonts used for both the business name and body text and provides an upscale and classic look.
![Libre Baskerville sample](documentation/libre_baskerville_sample.png)

- Lato from Google Fonts has been used for the main text throughout the site. This is a simple and clean-lined sans serif font, which is ideal for displaying larger pieces of information such as the welcome message on the home page and the service descriptions.
![Lato sample](documentation/lato_sample.png)

### Imagery

As the site is for a dog grooming business, the imagery chosen was related to dog grooming. This includes a hero image on the home page of a dog being brushed, as well as five icon images of the different services offered by the salon. There is also a paw imaged used within the business logo.

The hero image was chosen as it depicts a dog enjoying the grooming process which reminds owners that grooming keeps their dogs happy and healthy and is good for their wellbeing. This has a pink background as pink is frequently associated with salons and beauty products. This image is from Adobe Stock.
![Home Page - hero image](documentation/hero_image.png)

The five icon images representing the grooming services include an icon for the service ‘Full Groom’. This is a simple vector graphic depicting a happy dog wearing a bandana. This reflects the service offered, as the grooming process is meant to leave the dog feeling happy and refreshed, and each dog is given a bandana at the end of the groom. All of the icon images are the same dark blue (0E273F) as the website text.
![Full Groom Icon](documentation/full_groom.png)

Another icon image used depicts a man with a puppy, with star/shine symbols around it. This represents the service ‘Puppy Groom’. As this service is aimed at puppies 3-6 months of age, the dog featured is smaller. The shine symbols around the puppy represent cleanliness after being groomed.
![Puppy Groom Icon](documentation/puppy_groom.png)

The next icon used is another simple vector image of a dog having a bath. This is to represent the salon service ‘Bath, Brush & Blow dry’, as a main feature of this service is that the dog will be bathed.
![Bath Brush and Blow Dry Icon](documentation/bath.png)

Another icon imaged used is a vector graphic showing a dog having its nails clipped. This is to represent the service ‘Pawdicure’ which is essentially a pedicure for dogs.
![Pawdicure Icon](documentation/pawdicure.png)

The final icon image used depicts a dog having its teeth cleaned. This represents the grooming service ‘Teeth Cleaning’.
![Teeth Cleaning Icon](documentation/teeth_clean.png)

Another icon has been selected as a placeholder; in case the site owner decides to upload a service for which they do not yet have an image. This icon features a dog wearing a bowtie and smiling alongside the groomer to indicate that it is feeling happy and handsome after having a salon treatment.
![Service Icon Placholder](documentation/service_placeholder.png)

Finally, a similarly styled vector graphic of paw prints is used within the business logo. This is to reflect the business name Perfect Paws and is in the same blue colour as the logo and the website text (0E273F). This image is also used as the favicon for the website.
![Logo](documentation/logo.png)

### Wireframes

Having decided the colour scheme and tpography of the site, I put together wireframes in Balsamiq for how the pages should flow starting with the mobile design and then building around it for the larger screen sizes.

#### Base Template
This shows the basic layout of all the pages on the site including navbar and footer
![Base Template](documentation/wireframes/base_template.png)

#### Logged-in Template
This shows how the base template changes for a logged-in user
![Logged-in Template](documentation/wireframes/logged_In_template.png)

#### Home page
![Home page](documentation/wireframes/home.png)

#### User Profile page
![User Profile page](documentation/wireframes/user_profile.png)

#### Services page
![Services page](documentation/wireframes/services.png)

#### Contact Us page
![Contact Us page](documentation/wireframes/contact_us.png)

#### Register page
![Register page](documentation/wireframes/register.png)

#### Login page
![Login page](documentation/wireframes/login.png)

#### Make Booking page
![Make Booking page](documentation/wireframes/make_booking.png)

### Schema

This is the ERD for the project. The site doesn't need users to have a username and it made sense to store a phone number too, so I created a custom User model that inherited from AbstractUser so as to still be able to use the built in Django and AllAuth machinery.

![Perfect Paws ERD](documentation/perfect_paws_erd.png)

## Features

### General features of the site

- Favicon: Favicon.io was used to create the favicon for the Perfect Paws site. The favicon is the same paw prints image used in the business logo to keep the site looking consistent. It is also in the same dark blue colour as the website text and buttons (0E273F).
![Favicon](documentation/features/favicon.png)

- Navigation: Each page has a fixed-top navbar which stays position at the very top of the webpage, regardless of how far down the user scrolls, ‘fixing’ it in place so that it is always visible to the user. This allows for easy access to the navigation links, improving usability in the UX design. The navbar contains the paw prints logo image and links to the Home, Services, Contact Us, Login/Logout, Register and Book Here pages. The current page is highlighted within the navigation to indicate what page the user is on. If the user covers over a navbar link, this will highlight that link. The fixed-top navbar is fully responsive and will adjust to a hamburger menu toggle on smaller screens.
![Fixed Navbar](documentation/features/navbar.png)

- Footer: Every page also has a fixed footer, which remains visible at the bottom of the browser window no matter how far the user scrolls down the page, sticking to the bottom of the viewpoint. This ensures information such as the social media links, where users can connect with the business, are always accessible. This differs from a standard footer which only appears when the user scrolls to the bottom of the page.
![Fixed Footer](documentation/features/footer.png)

- Notifications system: When a user interacts with the site, they get feedback provided instantly as to success or otherwise. For example, the user will receive a notification when they have successfully logged in or out, booked a service or submitted the enquiry form.
![Notifications](documentation/features/notification.png)

### Specific pages

#### Home page

- Hero image: The home page contains a hero image which is a large and eye-catching image at the top of the home page. As this is often the first ting a user sees when coming to the site, I selected a colourful image that is relevant to the purpose of the business. This is an image of a happy dog being groomed with a bright lavender pink background, cohesive with the colour scheme of the overall site. 
- Welcome message: The home page also contains a welcome message which welcomes the user to the site and gives background information about the business, including what the business does, features of treatments and how long the business has been in operation.
- Book Now and Services buttons: The Book Now and Services buttons allow the user to go directly to the Booking or Services pages to quickly view and select a service. These are a call to action for the user and are particularly useful for returning users who want to quickly navigate to these pages.
![Home page](documentation/features/home_page.png)

#### Services page

- List and description of services: The services page provides a list and descriptions of the services offered by the salon. This automatically reflects the list of services defined by the site owner.  This allows the user to find out more information about exactly what is included in every treatment offered by the salon as well as pricing.
![Services page](documentation/features/services_page.png)

#### Book Now page

- Booking form: The Book Now page contains a booking form where users can select the salon service that they want to book. Each salon services appears at the top of the page within a tile with the appropriate name and icon, and the user selects the service by clicking on it. The user can also select the date and time of their desired service and input information about their dog within the form.
![Book Now page](documentation/features/booking_page.png)

- Datepicker: The booking form contains a jQuery UI datepicker, where the user can see what dates are available for the treatment they have selected. Dates which are not available are greyed out in the datepicker, and the user is unable to select the unavailable dates.
![Datepicker in Booking Form](documentation/features/booking_form_datepicker.png)

- Time slots: Next, the user is prompted to select a time slot for the service. Available slots will appear in the drop-down menu for the user to choose from. Times which are not available on the selected date will not appear as an option.
![Time Selector in Booking Form](documentation/features/booking_form_time_selector.png)

- Dog information: Finally, users are also prompted to input information about their dog, such as size, breed and name, as well as any notes for the groomer. There is a submit button below where users can submit their booking.
![Dog Information in Booking Form](documentation/features/booking_form_dog_information.png)

#### Contact Us page

- Contact form: The Contact Us page contains a contact form where users can send a message to the business. It contains a field for name, email, phone and the message. There is a send button at the bottom of the form that the user can click to send the message.
![Contact Form in Contact Us page](documentation/features/contact_form.png)

- Contact details: The page also contains a section with contact details, including the address of the business, the phone number and email. There is also a message letting customers know that they should send a message or leave a voicemail if the phone is not answered due to all of the groomers being busy with dogs.
![Business Information in Contact Us page](documentation/features/business_details.png)

- Map of location: The page includes an interactive map which allows the user to zoom in and out and includes a location marker for the business.
![Map of Location in Contact Us page](documentation/features/business_map.png)

#### Login page

- Register/login: This feature allows the user to sign into an existing account or register for an account. There is a link at the top for the user to register, and fields below (including a field for email and password) for them to use to sign in if they already have an account. There is a Sign In button for the user to click when the fields are completed.
![Login page](documentation/features/login_page.png)

#### Logout page

- Logout of the site: This page allows the user to logout of the site. The user is asked to confirm that they wish to sign out by clicking the Sign Out button. Once signed out, they will be redirected to the home page.
![Logout page](documentation/features/logout_page.png)

#### Profile Page

- Profile information: The profile page allows the user to edit their information, such as their name, email and phone number. The page contains a button to save any changes to information as well as delete the account. The user will be asked to confirm before they delete the account.
![User Profile page](documentation/features/user_profile.png)

### Other features

- Booking confirmation email: When the user books a service at the solon they are sent a confirmation email. This email contains the details of the booking, including the service booked, time and date for the user’s records.
![Booking Confirmation Email](documentation/features/booking_confirmation_email.jpg)

- Admin panel for site owner: The admin panel gives full CRUD access to all objects to site owner. Utilises built-in Django feature.
![Admin Panel](documentation/features/admin_panel.png)

### Future features to implement

- Allow users to view their current and past bookings within their profile or the site generally. 
- Add customer testimonials.
- Add a gallery of images of past grooms.

## Technologies Used

### Languages Used

HTML, CSS, JavaScript and Python were used to create this website.

### Frameworks, Libraries & Programs Used

#### Programs
- [Balsamiq](https://balsamiq.com/) - used to create wireframes

- [Git](https://git-scm.com/) - for version control

- [Github](https://github.com/) - to host the files for the website

- [LucidChart](https://www.lucidchart.com/pages/) - to create the ERD for my database

- [Google Fonts](https://fonts.google.com/) - to serve up site fonts

- [Cloudinary](https://cloudinary.com/) - a web service to enable image upload, host images and serve them

- [Favicon.io](https://favicon.io/) - to produce the favicon for the site

#### Frameworks
- [Django](https://www.djangoproject.com/) - v4.2, a high-level Python web framework

- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - v5.0.3, a framework for building responsive websites

- [jQuery UI](https://jqueryui.com/) - for the datepicker widget in the booking form

#### Libraries and packages
- [jQuery](https://jquery.com/) - a JavaScript library

- [Django AllAuth](https://docs.allauth.org/en/latest/) - to implement production-standard user authentication

- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/) - combined with Bootstrap to produce responsive forms

- [gunicorn](https://gunicorn.org/) - a production-level web server

- [psycopg2](https://www.psycopg.org/docs/) - to connect to the Postgres database

## Deployment & Local Development

### Deployment

This project is hosted on Github and the website on Heroku using a PostgresQL database.

1. From the Heroku dashboard create a new app

2. In the Settings pane add environment variables as Config Vars, including the database URL

3. In the Deploy tab connect the Heroku app to the Github repository

4. Either Enable Automatic Deploys, or click Deploy Branch

5. If needed, add your Heroku app's url to the `ALLOWED_HOSTS` in the project `settings.py`

### Local Development

The local development section gives instructions on how someone else could make a copy of your project to play with on their local machine. This section will get more complex in the later projects, and can be a great reference to yourself if you forget how to do this.

#### How to Fork

To fork the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [perfect-paws]().

3. Click on the fork button in the top right of the page.

#### How to Clone

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [perfect-paws]().

3. Click the Code button, select whether you would like to clone with HTTPS, SSH or the GitHub CLI and copy the link given.

4. Open the terminal in your chosen IDE and change the current working directory to the location you would like to use for the cloned repository.

5. Type `git clone <link from step 3>` into the terminal.

6. Set up a virtual environment.

7. Install the packages from the requirements.txt file by running `pip3 install -r requirements.txt` in the terminal

## Testing

Please refer to the [TESTING.md](README.md) file for all testing performed.

## Credits

### Code Used

This project was created using methods taught in the Code Institute’s walkthrough project for Django Blog.

The AJAX call functionality was adapted from [this article](https://testdriven.io/blog/django-ajax-xhr/) on testdriven.io on Working with AJAX in Django

### Content

Content for the site was written by Andrew Reid, with service descriptions based on services listed within existing dog grooming websites.

### Media

The images used for the site, including the hero image, favicon image and icons were licensed from Adobe Stock.

The fonts used within the site came from Google Fonts and dafont.
