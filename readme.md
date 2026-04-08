# Royal Oak Restaurant Booking System

Royal Oak is a full-stack Django restaurant booking application for a traditional pub and restaurant. Users can browse the site, register, log in, create a booking, view their own bookings, edit them, and cancel them. Staff can manage bookings through the Django admin.

## Live Project
- Live app: https://royal-oak-app-dfc55386b7fe.herokuapp.com/
- Repository: https://github.com/HollieMorrison/Royal-Oak
![Home Page](assets/readme/testing/home.png)

## Project Purpose
The aim of this project is to provide a simple online booking system for a restaurant. It solves the problem of customers needing to phone or message the venue to make reservations, while also giving the site owner a central place to manage bookings.

## Target Users
- Customers who want to reserve a restaurant table online
- Returning customers who want to manage existing bookings
- Restaurant staff who need to view and manage bookings

## User Experience (UX)
The project was designed to be:
- simple to navigate
- readable on desktop, tablet, and mobile
- focused on a clear booking flow
- consistent in colour, spacing, and feedback messaging

## Agile Planning
Development was managed with GitHub Issues and milestone planning.
User stories were broken down into tasks and implemented feature by feature.
![Agile Planning Board](assets/readme/agile/agile-board.png)

### Example User Stories
- As a visitor, I want to view the menu before booking.
- As a user, I want to create an account so I can make bookings.
- As a logged-in user, I want to create a reservation.
- As a logged-in user, I want to edit or cancel my reservation.
- As staff, I want to review bookings in the admin area.
![User Stories](assets/readme/agile/user-stories.png)

## Features

### Existing Features
- Home page with call to action
- Menu page
- User registration and login
- Logout functionality
- Booking create functionality
- My Bookings page for logged-in users
- Booking edit functionality
- Booking delete functionality
- Django messages for booking feedback

### Authentication and Permissions
- Anonymous users can only access public pages
- Logged-in users can create and manage their own bookings
- Users cannot edit or delete another user's booking
- Staff users can manage bookings through the admin panel

## Data Model

![Data Model](assets/readme/testing/Data-Model.png)

### Table model
- `name`
- `seats`

### Booking model
- `user` (ForeignKey to User)
- `date`
- `time`
- `party_size`
- `table` (ForeignKey to Table)
- `created_at`

### Validation and Business Logic
- users cannot book in the past
- users cannot exceed table capacity
- the same table cannot be double-booked for the same date and time

## CRUD Functionality
- Create: users can create bookings
- Read: users can view their own bookings
- Update: users can edit their own bookings
- Delete: users can cancel their own bookings

## Technologies Used
- HTML5
- CSS3
- JavaScript
- Python
- Django
- SQLite for development
- PostgreSQL for production
- Heroku for deployment
- Git and GitHub for version control

## Testing

### Manual Testing

- Home page loads correctly
![Home Page](assets/readme/testing/home.png)

- Menu page loads correctly
![Menu Page](assets/readme/testing/menu.png)

- Signup accepts valid details
![Logged-in Account Page](assets/readme/testing/login-validation.png)

- Login accepts valid details
![Login Accepts Valid Credentials](assets/readme/testing/login-accepts-valid-credentials.png)

- Booking form creates a booking
![Booking Form Screenshots](assets/readme/testing/booking.png)

![Booking Success](assets/readme/testing/booking-success.png)

![Booking Form](assets/readme/testing/booking-selections.png)

- Booking form rejects invalid input
![Booking Past Date error](assets/readme/testing/validation-error.png)
![Booking Too Many Guests Error](assets/readme/testing/too-many-guests-validation-error.png)

- My Bookings shows only the logged-in user's bookings
![My Bookings Page](assets/readme/testing/my-bookings.png)

- Edit updates the booking in the UI
![When Clicking Edit Page](assets/readme/testing/edit-booking.png)

- Delete removes the booking in the UI
![Delete Booking Page](assets/readme/testing/delete-booking.png)

![Delete Booking Confirmed](assets/readme/testing/booking-deleted-successfully.png)

- Responsive layout works on desktop, tablet, and mobile

![Mobile](assets/readme/testing/responsive-mobile.png)
![Tablet](assets/readme/testing/responsive-ipad.png)

-Admin Panel 
![Admin](assets/readme/testing/admin-access.png)

### Automated Testing
The project includes Django tests for:
- model validation
- form validation
- login protection
- create booking
- view own bookings
- edit own booking
- delete own booking


![Pytest Results](assets/readme/validation/pytest.png)
![Pycodestyle](assets/readme/validation/pycodestyle.png)

## Validation
Add screenshots or notes for:
- HTML validation
![HTML Results](assets/readme/validation/html.png)
- CSS validation
![CSS Results](assets/readme/validation/css.png)
- Python linting / PEP8
![Python Results](assets/readme/validation/pytest.png)
![Pycodestyle](assets/readme/validation/pycodestyle.png)
- browser testing
![Browser Testing](assets/readme/testing/browser-testing.png)

## Bugs
### Fixed Bugs
- empty table dropdown on deployed site
- booking ownership issue
- broken booking routes
- missing templates for reserve and bookings pages

### Remaining Bugs
- none that i can find currently.

## Deployment

### Local Development
1. Clone the repository
2. Create a virtual environment
3. Activate the virtual environment
4. Install requirements with `pip install -r requirements.txt`
5. Create a `.env` file with:
   - `SECRET_KEY`
   - `DEBUG=True`
   - `ALLOWED_HOSTS=127.0.0.1,localhost`
6. Run migrations
7. Create a superuser if needed
8. Run the development server

### Heroku Deployment
1. Create a Heroku app
2. Set config vars:
   - `SECRET_KEY`
   - `DEBUG=False`
   - `ALLOWED_HOSTS`
   - `DATABASE_URL`
3. Connect the GitHub repository or deploy from Git
4. Run migrations on Heroku
5. Create a superuser on Heroku
6. Add initial `Table` data in production
7. Confirm the deployed site matches the development version

## Security
- SECRET_KEY is stored in environment variables
- DEBUG is disabled in production
- sensitive values are not stored in the repository
- authenticated routes are protected with `login_required`

## Future Improvements
- email confirmations
- improved table availability logic
- mobile nav menu
- booking status field
- staff dashboard enhancements

## Credits
- Django documentation
- Code Institute project guidance
- Testing support from friends/family

## Acknowledgements
Thanks to my mentor, tutors, and peers for feedback throughout development.
