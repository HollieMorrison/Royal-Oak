# Royal Oak Restaurant Booking System

Royal Oak is a full-stack restaurant booking application for a traditional pub/restaurant.

Guests can browse the menu and opening hours, create an account, and reserve a table for a specific date, time and party size. Logged-in users can view and manage their own bookings, while staff can manage all bookings via the Django admin.

![Am I Responsive screenshot](./assets/readme/am-i-responsive.png)

[View the live Royal Oak project here](https://royal-oak-app-dfc55386b7fe.herokuapp.com/)  
[View the GitHub repository here](https://github.com/HollieMorrison/Royal-Oak)

---

## Table of contents :

### [User Experience (UX)](#user-experience-ux-1)
* [User Stories](#user-stories)
* [Agile Methodology](#agile-methodology)
### [Features](#features-1)
* [Existing Features](#existing-features)
* [Role-based Access & Authentication](#role-based-access--authentication)
### [Features Left To Implement](#features-left-to-implement-1)
### [Design](#design-1)
### [Data Model](#data-model-1)
### [Technologies Used](#technologies-used-1)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
* [Validation Results](#validation-results)
* [Manual Testing](#manual-testing)
* [Future Testing Improvements](#future-testing-improvements)
### [Deployment and Local Development](#deployment-and-local-development-1)
* [Local Development](#local-development)
* [Heroku Deployment](#heroku-deployment)
### [Security & Environment Variables](#security--environment-variables)
### [Credits](#credits-1)
### [Acknowledgements](#acknowledgements-1)

---

## User Experience (UX)

The goal of Royal Oak is to provide a simple, friendly way for customers to:

* Discover the Royal Oak pub/restaurant.
* View the menu and key information (location, contact, opening times).
* Quickly reserve a table for a specific date, time and party size.
* Manage their own bookings without needing to phone the venue.

For the site owner / restaurant staff, the app:

* Collects online bookings in a central database.
* Ensures only authenticated users can create and manage bookings.
* Provides staff access via the Django admin to review, edit or cancel bookings.

The layout focuses on clear navigation, readable text, and mobile-friendly pages so users can easily book a table on any device.

### User Stories

**First-time visitor goals**
* As a first-time visitor, I want to understand what the Royal Oak is and what it offers.
* As a first-time visitor, I want to view the menu and opening hours before I decide to book.
* As a first-time visitor, I want to sign up for an account so I can make a booking online.

**Returning visitor goals**
* As a returning user, I want to log in quickly so I can see my existing bookings.
* As a returning user, I want to edit or cancel a booking if my plans change.
* As a returning user, I want to see a confirmation message when I create or update a booking.

**Site owner / staff goals**
* As the site owner, I want bookings to be stored in a database so they are not lost.
* As staff, I want to see all bookings in the admin area so I can manage the restaurant floor.
* As the site owner, I want only logged-in users to be able to create bookings so I can reduce spam and fake entries.

### Agile Methodology

Agile principles were followed using:

* **GitHub Issues** – used to create user stories and track bugs and enhancements.
* **Labels** such as “feature”, “bug”, and priority tags (must-have, should-have, etc.) to organise work.
* **Milestones / project board** – used to group issues into deliverable phases (MVP, additional features, polish).

Each user story typically followed:

1. Create issue with a clear user story and acceptance criteria.
2. Implement the feature in a dedicated branch.
3. Test locally (and on the deployed app where needed).
4. Merge changes into the main branch.

---

## Features

### Existing Features

**Home Page**
* Introduction to the Royal Oak pub/restaurant.
* Clear navigation bar: Home, Menu, Bookings, Login/Signup.
* Call-to-action button for **Reserve a Table**.

**Menu Page**
* Static menu preview with example dishes.
* Clean and accessible layout.

**Signup / Login**
* Custom signup page using Django Authentication.
* Login page for existing users.
* Validation for both forms.

**Booking Form**
* Login-protected reservation page.
* Form fields include:
  * Name
  * Email
  * Phone
  * Date
  * Time
  * Number of guests
  * Special requests (optional)
* Server-side validation and confirmation messages.

**Bookings List**
* Authenticated users can view their own bookings.
* List shows date, time, party size and status.

**Responsive Layout**
* Works across desktop, tablet, and mobile screens.
* Tested using DevTools responsive view.

### Role-based Access & Authentication

* **Anonymous users**  
  * Can browse public pages only.  
  * Are redirected to login when attempting restricted actions.

* **Authenticated users**  
  * Can reserve tables.  
  * Can view/manage their bookings.

* **Superusers / staff**  
  * Access the Django admin interface.  
  * Can view, edit, delete any booking.

---

## Features Left To Implement

* Email confirmation for bookings.
* Realistic table-capacity handling.
* Staff dashboard for today’s bookings.
* User profile editing.
* More advanced JavaScript validation.

---

## Design

* Warm and inviting colour palette inspired by traditional pubs.
* Clean, readable fonts for headings and body text.
* Consistent spacing and simple structure.
* Logical navigation links on every page.
* Clear feedback via Django messages.

---

## Data Model

The project includes a custom **Booking** model with fields for:

* `name`
* `email`
* `phone`
* `date`
* `time`
* `guests`
* `special_requests`
* `user` (ForeignKey to authenticated User)
* `created_at` / `updated_at`

This supports relational storage, filtering by user, and admin management.

---

## Technologies Used

* HTML5  
* CSS3  
* JavaScript  
* Python 3  
* Django  
* SQLite (development)  
* PostgreSQL (production)  

---

## Frameworks, Libraries & Programs Used

* **Django** – main framework
* **Gunicorn** – production server
* **WhiteNoise** – static file serving
* **dj-database-url** – database configuration
* **Git** – version control
* **GitHub** – remote repository & Agile tools
* **Heroku** – hosting
* **VS Code** – code editor
* **Chrome DevTools** – debugging & testing

---

## Testing

### Validation Results

**HTML**  
Checked with W3C Validator. Minor fixes applied.

**CSS**  
Checked with W3C CSS Validator. Validated successfully.

**Python (PEP8)**  
Checked with PEP8 tools. Code formatted to standards.

**JavaScript**  
Console error inspection and manual behaviour testing.

---

### Manual Testing

| Feature | Test | Result |
|--------|------|--------|
| Home page loads | Visit `/` | Pass |
| Menu page | Visit `/menu/` | Pass |
| Signup | Valid/Invalid form inputs | Pass |
| Login | Valid/Invalid login | Pass |
| Auth protection | Restricted pages redirect | Pass |
| Create booking | Submit booking | Pass |
| View bookings | Shows user-specific bookings | Pass |
| Admin | View/edit bookings | Pass |
| Responsive layout | Mobile/Tablet tests | Pass |

### Future Testing Improvements

* Add Django unit tests for models, forms and views.
* Add JS tests using Jest.
* Add automated CI pipeline.

---

## Deployment and Local Development

### Local Development

1. Clone repo:  
   ```bash
   git clone https://github.com/HollieMorrison/Royal-Oak.git

### Create virtual environment 

1. python -m venv .venv

### Activate:

Windows PowerShell: .venv\Scripts\Activate

Git Bash/Mac: source .venv/bin/activate

Install requirements:

pip install -r requirements.txt


### Create .env file:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1


### Migrate:

python manage.py migrate


### Run:

python manage.py runserver

### Heroku Deployment

Create app in Heroku dashboard.
Add Heroku Postgres add-on.
Add config vars:
SECRET_KEY
DEBUG=False
ALLOWED_HOSTS
DATABASE_URL (auto-added)
Connect GitHub repo or push via Git.

### Run migrations:

heroku run python manage.py migrate


### Create superuser:

heroku run python manage.py createsuperuser
Security & Environment Variables
SECRET_KEY kept in .env and Heroku config vars.
DEBUG disabled on production.
No secrets stored in GitHub.
Database credentials stored securely via DATABASE_URL.


### Credits

Django documentation

Code Institute sample README template

Tutorials on Django forms, authentication, and deployment

Content

Menu items and wording adapted for a fictional restaurant.

Media

Images from free stock sites.

Responsive mockups via “Am I Responsive”.

Acknowledgements

Code Institute mentor Mitko for guidance.

Slack community for support.

Friends/family who helped test the app.


