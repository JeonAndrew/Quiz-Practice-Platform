# Summary of presentation introduction
The Quiz Practice Platform is a web application that students can use to study and practice for exams of numerous courses. The web application tailors its quizzes to the needs of the student. It allows students to choose what course they would like to practice for, and students may select topics within each course they would like to focus on. Quizzes will give students a multiple choice question that they can answer or choose to skip; the correct answer will be revealed after each problem regardless of their choice.

# Technical Architecture

## Frontend

### JavaScript

We use JavaScript to send REST requests to our backend which eventually connects to our firebase database. We also use JS to ensure that we can dynamically change elements on our website when we load them in from our database. 

### HTML
 
As a basic scripting language for websites, we use HTML to implement the user interface for logging in, quizzes, and course selections.

### CSS 

We implement CSS in our website to style our HTML components to ensure they look appealing and carry a smooth flow throughout our website.


## Backend

### Python Flask Server

Serves as the framework for our REST API that we use to communicate with the frontend. This Flask server also allows our application to talk with the firebase database where user information along with course information is stored.

### Python Classes

Python classes for users, courses, topics, quizzes, and questions are used as models for the data we receive from our firebase database. We test the logic of these classes unit the native unit tests python package. 

### Firebase Database

We use firebase as our cloud database. The database stores our users, courses, topics, and questions. As a cloud database it is also easier to collaborate with others as the database can have multiple connections at once. The firebase database is easy to provision and access as well which makes it a good choice for our application.

# Reproducible installation instructions
Clone the Quiz Practice Platform from the main branch into your code editor (i.e. Visual Studio Code). From here, the folder should have a dockerfile, so open the folder in a docker container, which should have all of the python dependencies to start running the code. If they are not all present, just use pip install to install the remaining dependencies. From here, download the secret key file used to access the firebase backend / database. Place that file in quiz-backend/src, and change the file path in app.py in the same folder to reflect the path of this file with the secret key. After doing so, running python app.py in this directory should start up the flask server and accessing the localhost / ip should provide access to the website. 

Note: The secret key is vital to running the website since the app.py which the app runs on requires it to have access to the database. This cannot be committed since it throws flags / errors and is disabled by Google which will prompt the need for a new secret key.

# Group members and their roles
Steven Uruchima: frontend development and testing
Atul Ummaneni: backend/database development
Charles Huang: backend development
Andrew Jeon: backend development
