
## Table of Contents

1. [Testing Overview](#testing-overview)  
   - [Testing Methods](#testing-methods)  

2. [Automated Testing](#automated-testing)  
   - [Test Files & Purpose](#test-files--purpose)  

3. [Manual Testing](#manual-testing)  
   - [User Story Testing](#user-story-testing)  
   - [Test Environment](#test-environment)  
   - [Testing Procedure](#testing-procedure)  
   - [Results](#results)  

4. [Accessibility Testing](#accessibility-testing)  
   - [Tools Used](#tools-used)  
   - [Key Findings & Fixes](#key-findings--fixes)  

5. [Validation Testing](#validation-testing)  
   - [Tools & Validators](#tools--validators)  
   - [Results](#results-1)  

6. [Performance Testing](#performance-testing)  
   - [Lighthouse Performance Scores](#lighthouse-performance-scores)  
   - [Key Findings & Improvements](#key-findings--improvements)  

7. [Bug Fixes & Summary](#bug-fixes--summary)  


## Testing Overview

This document outlines the testing process undertaken for the Perfect Paws Dog Grooming Salon Booking Website. The website allows users to book grooming appointments, manage their profiles and contact the business through a form. The testing ensures functionality, usability, performance, accessibility and security.

### Testing Methods
The testing process included:
- **Automated Testing**: Unit tests for core functionalities, executed using Django TestCase.
- **Manual Testing**: Comprehensive checks across different devices and browsers, covering all links, forms and JavaScript functionalities.
- **User Story Testing**: Verification of user stories to ensure that all project requirements were met.
- **Accessibility Testing**: Evaluating compliance with WCAG 2.1 AA standards.
- **Validation Testing**: Ensuring correct HTML, CSS, JavaScript and Python code formatting and structure.
- **Performance Testing**: Assessing site speed and optimising performance based on Lighthouse reports.
- **Bug Fixes & Summary**: Documenting issues encountered and their resolutions.


## Automated Testing

The following automated tests were implemented to ensure the core functionality of the site:

| App / Test File | Purpose |
|-----------|---------|
| `booking/test_views.py` | Tests views related to the booking system, including successful bookings and validation errors. |
| `core/test_views.py` | Tests core site functionality, ensuring pages load correctly and expected redirects occur. |
| `enquiries/test_forms.py` | Tests enquiry form submissions, including valid and invalid input handling. |
| `enquiries/test_views.py` | Tests views related to enquiries, ensuring correct form rendering and submissions. |
| `users/test_views.py` | Tests user authentication, including login, logout, registration and profile updates. |

## Manual Testing

Manual testing was conducted to verify that all core functionalities of the website operated correctly across different devices and browsers. The testing process involved checking all navigation links, forms, user authentication flows, JavaScript interactions and general site responsiveness.

### User Story Testing

The table below outlines the user stories defined for the project, along with the corresponding testing outcomes.

| User Story ID | As a/an | I want to be able to ... | So that I can... | Acceptance Criteria | Testing Outcome |
|--------------|--------|------------------------|----------------|--------------------|----------------|
| **VIEWING & NAVIGATION** |
| 1 | User | Easily navigate the site | Find information and book services that I need | * Navbar is stuck to top of the browser window<br>* Links are clearly labelled and easy to click | ✅ Passed (Manual & Automated) |
| 2 | User | View what dog grooming services are offered | Find information about specific services I may need | * Services page lists all available services | ✅ Passed (Manual & Automated) |
| 3 | User | Find out more information about the business | Find out how much experience the groomer has and their qualifications | * Home page has information about Perfect Paws | ✅ Passed (Manual & Automated) |
| 4 | User | Find out how to contact the business | In case I want to ask a question, change or cancel an appointment | * Contact Us page has business email, phone number and a location map | ✅ Passed (Manual & Automated) |
| 5 | User | Submit an enquiry | Ask a question | * Contact Us page has a Send a message form<br>* Form won’t submit without required fields filled | ✅ Passed (Manual & Automated) |
| 6 | User | Determine where the business is located | Know where to bring my dog for the appointment or visit the business in person | * Contact Us page has address and map | ✅ Passed (Manual & Automated) |
| 7 | User | See Perfect Paws’s social media sites | Follow the business on social media, read their announcements or see past grooms | * Footer has links to social media profiles | ✅ Passed (Manual & Automated) |
| 8 | User | See a register or login button if I am not logged in | Know if I need to log in or register | * Navbar has Register and Login buttons for logged-out users | ✅ Passed (Manual & Automated) |
| 9 | User | See a logout button when I’m logged in | Logout of the site | * Navbar has a Logout button for logged-in users | ✅ Passed (Manual & Automated) |
| 10 | Site owner | See an admin button when logged in | Access the admin panel | * Admin users see an Admin button in the navbar | ✅ Passed (Manual & Automated) |
| **REGISTRATION & USER ACCOUNTS** |
| 11 | User | Register for an account | Have an account to book services | * Non-logged-in users can register via sign-up page | ✅ Passed (Manual & Automated) |
| 12 | User | Log in and out | Book appointments and keep personal details secure | * Login page allows users to sign in<br>* Logout option available for signed-in users | ✅ Passed (Manual & Automated) |
| 13 | User | Reset my password | Recover my account or change my password | * Users can request a password reset from login page | ✅ Passed (Manual & Automated) |
| 14 | User | Login or register if I try to book while not logged in | Create an account and book a service | * Non-logged-in users trying to book are redirected to login page | ✅ Passed (Manual & Automated) |
| 15 | User | View my profile page | Update my information | * Profile page displays user details<br>* Users can update email, names and phone number | ✅ Passed (Manual & Automated) |
| 16 | User | Delete my account | No longer make bookings | * Profile page has Delete Account button with confirmation prompt | ✅ Passed (Manual & Automated) |
| **BOOKING & CONFIRMATION** |
| 17 | User | Select the service I want to book | Get an appointment for my dog | * Booking page has a booking form with required fields | ✅ Passed (Manual & Automated) |
| 18 | User | Check available dates and times | Choose a convenient appointment slot | * Date picker only shows available slots | ✅ Passed (Manual & Automated) |
| 19 | User | Only see time slots available for the service I want to book | Avoid booking unavailable times | * Time slots update based on selected service | ✅ Passed (Manual & Automated) |
| 20 | User | Complete my booking | Confirm my appointment | * Booking form does not submit without required details | ✅ Passed (Manual & Automated) |
| 21 | User | See a booking confirmation message | Ensure my booking went through | * Success message appears after booking | ✅ Passed (Manual & Automated) |
| 22 | User | Receive an email confirmation after booking | Keep a record of my booking | * Confirmation email sent with appointment details | ✅ Passed (Manual & Automated) |
| **ADMIN & SITE MANAGEMENT** |
| 23 | Site owner | Add a dog grooming service | Offer new services | * Admin panel allows adding new services | ✅ Passed (Manual & Automated) |
| 24 | Site owner | Edit or update a service | Change prices, descriptions and promotions | * Admin panel allows editing services | ✅ Passed (Manual & Automated) |
| 25 | Site owner | Suspend a service | Temporarily remove services | * Admin can mark services as inactive | ✅ Passed (Manual & Automated) |
| 26 | Site owner | View enquiries | Respond to customer queries | * Admin panel displays customer enquiries | ✅ Passed (Manual & Automated) |
| 27 | Site owner | Mark an enquiry as responded to | Track which queries are answered | * Admin can mark enquiries as read | ✅ Passed (Manual & Automated) |
| 28 | Site owner | View bookings | Keep track of appointments | * Admin can see all bookings in the admin panel | ✅ Passed (Manual & Automated) |
| 29 | Site owner | Modify bookings | Make changes when necessary | * Admin can edit bookings in the admin panel | ✅ Passed (Manual & Automated) |
| 30 | Site owner | Mark a booking as cancelled | Record cancelled appointments | * Admin can cancel bookings and record the date of cancellation | ✅ Passed (Manual & Automated) |

#### Results
All user stories were tested successfully and the core functionality of the website was confirmed to be working as intended.


### Test Environment

| Device        | Browser   |
|--------------|----------|
| MacBook Pro  | Chrome, Firefox, Safari |
| iPad Pro     | Chrome, Firefox, Safari |
| iPhone 15 Pro | Chrome, Firefox, Safari |

### Testing Procedure
1. **Navigation**
   - Verified that all links direct to the correct pages.
   - Ensured the navbar remains fixed and responsive across devices.
   - Checked footer links for accuracy and proper redirection.

2. **Forms**
   - Tested the registration, login, contact and booking forms.
   - Checked validation errors for incorrect inputs.
   - Confirmed successful submission and appropriate redirection or confirmation messages.

3. **User Authentication**
   - Registered a new user and confirmed account creation.
   - Logged in and verified access to the user profile.
   - Updated profile information and checked for successful changes.
   - Tested password reset functionality.
   - Logged out and ensured the session ended correctly.
   - Tested user account deletion correctly deleted the user record.

4. **Booking System**
   - Created a new booking and checked confirmation messages.
   - Attempted to create another booking for the same time and was unable to.
   - Confirmed that day and time availability was reflected in the booking form.
   - Marked a booking as canceled through the admin panel and confirmed timeslot became available for booking again.

5. **Enquiry System**
   - Submitted an enquiry via the contact form.
   - Ensured correct form validation for required fields.
   - Verified that the enquiry appears in the admin panel.

6. **JavaScript Functionality**
   - Checked client-side form validation messages.
   - Tested interactive elements such as date pickers and modals.
   - Ensured dynamic content updates correctly.

7. **Responsive Design**
   - Assessed layout and styling on different screen sizes.
   - Ensured touch interactions function properly on mobile devices.

### Results
All manual tests were successfully completed, with no major issues encountered. Minor styling inconsistencies were identified and corrected during testing.

## Accessibility Testing

Accessibility testing was performed to ensure compliance with WCAG 2.1 AA standards and to improve usability for all users, including those with disabilities. The following tools and methods were used:

### Tools Used
- **Lighthouse (Chrome DevTools)** – Checked accessibility scores and identified potential issues.
- **Keyboard Navigation Testing** – Verified all interactive elements were accessible via the keyboard.

### Key Findings & Fixes
| Issue | Resolution |
|-------|-----------|
| Missing alt attributes on some images | Added appropriate alt text to all images |
| Focus states not always visible | Improved focus indicators for better keyboard accessibility |
| Social links in footer lack label | Added `aria-label` attributes describing the links


---

## Validation Testing

Validation testing was conducted to ensure proper syntax and compliance with web standards. The following validators were used:

- **HTML Validation** – [W3C Markup Validator](https://validator.w3.org/)
- **CSS Validation** – [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- **JavaScript Validation** – [JSHint](https://jshint.com/)
- **Python Code Validation** – [CI Python Linter](https://pep8ci.herokuapp.com/) for PEP8 compliance

### Results
| Test | Outcome |
|------|---------|
| HTML | No major errors found. Minor warnings related to redundant attributes were fixed. |
| CSS | No validation errors detected. Improved styling consistency. |
| JavaScript | Fixed a few console warnings and improved error handling. |
| Python | All scripts passed PEP8 compliance, ensuring clean, maintainable code. |

All validation checks passed successfully, ensuring code quality and compliance with best practices.

## Performance Testing

Performance testing was conducted using **Lighthouse** in Chrome DevTools to evaluate page load times, responsiveness and overall efficiency.

### Lighthouse Performance Scores
The following are the Lighthouse performance scores for the website:

| Metric | Score |
|--------|-------|
| Performance | X |
| Accessibility | X |
| Best Practices | X |
| SEO | X |

### Key Findings & Improvements
| Issue | Resolution |
|-------|-----------|
| Images not optimised for performance | Utilised Cloudinary dynamic resizing to retrieve appropriately sized images for services |
| Some accessibility issues | see above

Following these optimisations, performance scores improved, resulting in faster page loads and a better user experience.

## Bug Fixes & Summary

During testing, several issues were identified and subsequently fixed. Below is a summary of the most notable fixes:

| Issue | Resolution |
|-------|-----------|
| User registration page was missing some user fields | Updated `settings.py` to ensure AllAuth used the custom form correctly |
| Booking form service listings were not sizing properly when more than two were present | Added `flex-wrap` to their parent container to allow correct wrapping |
| Datepicker was excluding incorrect days (Saturday & Sunday instead of Sunday & Monday) | Adjusted JavaScript logic to correctly exclude Sunday and Monday, accounting for different weekday indexing in JavaScript vs Python |

All significant bugs were resolved, improving the usability and functionality of the site.
