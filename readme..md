
researched:
1. http and the client/server relationship and how server-side projects function
2. how we use REST and HTTP to communicate from client to server
0. what does request and response mean in a api.2
3. What is an api.
4. How does django render html to the user.
5. what is a web api.
6. how can the client get data from the server.

  http request ( header and the body )
     - header - where we cookies/auth ids 
     - body   - where we transmit data. 
    fetch library - wrapper of http that allows us to send this data easier.

  rest ( architecture / how do we communicate between client server )
    requests to our server must contain a resource ( url endpoint ) 
        the resource must be formatted in GET, POST, PUT, DELETE.
        the resource must handle a request and return with a response of json  / string. 

  client
      fetch('/getData' , bodyData , headerData )
        ... ( async terminology )

  js async ( asyncrounous operation )
      - syncrounous / asyncrounous 
--- 

covered so far...
1. setting up project using pipenv. 
2. activating the virtual environment for our project,
3. scaffolding a new django project.
4. creating a new app for that project.

5. connecting the app to our project through the settings.
6. creating views that are essentially our pages or api routes.
7. connecting those views to urls in both the app and project.
8. rendering a html file in a view. 
9. using template portions
10. loading data from the server into a html page.
11. getting a database working and creating the models.
  creating a superuser
    - python manage.py createsuperuser 
    - holli / 12345

  - setup a new table called Reservation in our schema in myapp/models.
  - we made a migration of this database and migrated.
      - python manage.py makemigrations
      - python manage.py mirate
  
  - we then registred our Reservation table to the admin in admin.py 

  - we navigated to the admin so that we could view our new Reservation table + add data to to it.

  - fetching data from the Model within a view and passing that data to the html.


whats left...

3. set up a form in a reservation html and send this data to our api using fetch or 
   form posting.
 
4. creating views that get, post, delete and update data in a db table.
5. using our server api from our HTML pages.

6. setting up auth and user + protected pages / views.

7. status codes.

db
   - we're already connected to a sqlite db ( relational ) if we want mongodb or mysql/postgres then we need to configure that.
   - define the tables we'll be storing data in. 
   - viewing those tables in gui just to observe.
   - fetch and store data in there.

  restarting the project packages
    - pipenv shell 

  
  to do :
  - understand how we connect template partials into a html file.
  - how to header links understand the correct pathing using the url (plug / variable )
  - how we create an array variable and pass it to the html file we are rendering.
  - how to take that array in our html file and render as html using the for loop 




---------
day
    20 tables

        

-------------