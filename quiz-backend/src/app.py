# app.py

from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from models.Course import Course
from models.Topic import Topic
from models.Question import Question
from models.Quiz import Quiz
from models.User import User
import firebase_admin
from firebase_admin import credentials, firestore, auth as firebase_auth
from functools import wraps
from flask_cors import CORS
import os
import logging
import json

app = Flask(__name__)

# Use environment variable for secret key or fallback to a default (not recommended for production)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your-default-secret-key')  # Replace with a secure key

# Enable CORS for all routes
CORS(app, supports_credentials=True)

# Adjust the template and static folder paths
app.template_folder = os.path.abspath('../../quiz-frontend/templates')
app.static_folder = os.path.abspath('../../quiz-frontend/static')

# Initialize Firebase Admin SDK for Firestore and Authentication
service_account_path = '/Users/aummaneni/Quiz-Practice-Platform-1/quiz-backend/src/cs222-quiz-proj-firebase-adminsdk-k0qc4-685f7d0bee.json'  # Replace with your service account key path
if not os.path.exists(service_account_path):
    raise FileNotFoundError(f"Service account key file not found at: {service_account_path}")
if not os.path.exists(service_account_path):
    raise FileNotFoundError(f"Service account key file not found at: {service_account_path}")

cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture all levels of logs
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Initialize global variables
courses = []
topics = []

# Sample data initialization
def initialize_sample_data():
    logger.info("Initializing sample data...")
    # Create sample topics
    topic1 = Topic(name="Math", t_id=1, proficiency=10)
    topic2 = Topic(name="Science", t_id=2, proficiency=10)
    topic3 = Topic(name="History", t_id=3, proficiency=10)

    # Add sample questions to topics
    math_questions = [
        Question("What is 2+2?", ["3", "4", "5"], "4"),
        Question("What is 5x5?", ["20", "25", "30"], "25"),
        Question("What is the square root of 16?", ["4", "5", "6"], "4"),
        Question("What is 10/2?", ["4", "5", "6"], "5"),
        Question("What is 7-3?", ["3", "4", "5"], "4"),
    ]
    for q in math_questions:
        topic1.add_question(q)

    science_questions = [
        Question("What is H2O?", ["Water", "Oxygen", "Hydrogen"], "Water"),
        Question("What planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter"], "Mars"),
        Question("What gas do plants absorb?", ["Oxygen", "Carbon Dioxide", "Nitrogen"], "Carbon Dioxide"),
        Question("What is the chemical symbol for Gold?", ["Au", "Ag", "Gd"], "Au"),
        Question("What force keeps us on the ground?", ["Magnetism", "Gravity", "Friction"], "Gravity"),
    ]
    for q in science_questions:
        topic2.add_question(q)

    history_questions = [
        Question("Who was the first President of the USA?", ["George Washington", "Abraham Lincoln", "Thomas Jefferson"], "George Washington"),
        Question("In which year did World War II end?", ["1945", "1939", "1918"], "1945"),
        Question("Who discovered America?", ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan"], "Christopher Columbus"),
        Question("What was the ancient Egyptian writing system?", ["Cuneiform", "Hieroglyphics", "Latin"], "Hieroglyphics"),
        Question("The Great Wall is located in which country?", ["India", "China", "Japan"], "China"),
    ]
    for q in history_questions:
        topic3.add_question(q)

    topics.extend([topic1, topic2, topic3])

    # Create a course and add topics
    course = Course(name="General Knowledge", c_id=1)
    course.add_topic(topic1)
    course.add_topic(topic2)
    course.add_topic(topic3)
    courses.append(course)
    logger.info("Sample data initialization complete.")

# Helper functions
def get_topic_by_id(tid):
    logger.debug(f"Fetching topic with ID: {tid}")
    for topic in topics:
        if topic.get_topic_id() == tid:
            logger.debug(f"Found topic: {topic.get_name()}")
            return topic
    logger.warning(f"No topic found with ID: {tid}")
    return None

def get_all_active_topics():
    active_topics = [topic for topic in topics if topic.is_active()]
    logger.debug(f"Active topics count: {len(active_topics)}")
    return active_topics

def save_user_to_firestore(user):
    try:
        logger.debug(f"Saving user {user.get_user_id()} to Firestore.")
        user_ref = db.collection('users').document(user.get_user_id())
        user_ref.set(user.to_dict())
        logger.info(f"User {user.get_user_id()} saved successfully.")
    except Exception as e:
        logger.error(f"Error saving user {user.get_user_id()} to Firestore: {e}")

# app.py

def get_user_from_firestore(user_id):
    try:
        logger.debug(f"Retrieving user {user_id} from Firestore.")
        user_ref = db.collection('users').document(user_id)
        doc = user_ref.get()
        if doc.exists:
            user_data = doc.to_dict()
            logger.debug(f"User {user_id} found in Firestore.")
            user = User.from_dict(user_data, topics)
            return user
        else:
            logger.info(f"User {user_id} does not exist in Firestore.")
            return None
    except Exception as e:
        logger.error(f"Error retrieving user {user_id} from Firestore: {e}")
        return None

def get_user(user_id):
    user = get_user_from_firestore(user_id)
    if user is None:
        logger.info(f"Creating new user with ID: {user_id}")
        user = User(u_id=user_id)
        save_user_to_firestore(user)
    return user

initialize_sample_data()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            logger.info("Unauthorized access attempt to protected route.")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    logger.info("Rendering index page.")
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        logger.info("Received POST request on /signup.")
        try:
            data = request.get_json()
            logger.debug(f"Signup data received: {data}")
            if not data:
                logger.warning("No data provided in signup request.")
                return jsonify({'success': False, 'message': 'No data provided.'}), 400
            id_token = data.get('idToken')
            if not id_token:
                logger.warning("No ID token provided in signup request.")
                return jsonify({'success': False, 'message': 'No ID token provided.'}), 400
            try:
                decoded_token = firebase_auth.verify_id_token(id_token)
                logger.debug(f"Decoded token: {decoded_token}")
                user_id = decoded_token['uid']
                email = decoded_token.get('email')
                if not email:
                    logger.warning("Email not available in decoded token.")
                    return jsonify({'success': False, 'message': 'Email not available.'}), 400
                user = get_user_from_firestore(user_id)
                if user is not None:
                    # User already exists
                    logger.info(f"User {user_id} already exists.")
                    return jsonify({'success': False, 'message': 'User already exists.'}), 400
                # Create new user
                user = User(u_id=user_id, email=email)
                save_user_to_firestore(user)
                session['user_id'] = user.get_user_id()
                session['email'] = email
                logger.info(f"User {user_id} signed up successfully.")
                return jsonify({'success': True})
            except firebase_admin.exceptions.InvalidIdTokenError:
                logger.error("Invalid ID token provided during signup.")
                return jsonify({'success': False, 'message': 'Invalid ID token.'}), 401
            except firebase_admin.exceptions.ExpiredIdTokenError:
                logger.error("Expired ID token provided during signup.")
                return jsonify({'success': False, 'message': 'Expired ID token.'}), 401
            except Exception as e:
                logger.error(f"Unexpected error during signup: {e}")
                return jsonify({'success': False, 'message': 'An error occurred during signup.'}), 500
        except Exception as e:
            logger.error(f"Error processing signup request: {e}")
            return jsonify({'success': False, 'message': 'Internal server error.'}), 500
    else:
        logger.info("Rendering signup page.")
        return render_template('signup.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        logger.info("Received POST request on /login.")
        try:
            data = request.get_json()
            logger.debug(f"Login data received: {data}")
            if not data:
                logger.warning("No data provided in login request.")
                return jsonify({'success': False, 'message': 'No data provided.'}), 400
            id_token = data.get('idToken')
            if not id_token:
                logger.warning("No ID token provided in login request.")
                return jsonify({'success': False, 'message': 'No ID token provided.'}), 400
            try:
                decoded_token = firebase_auth.verify_id_token(id_token)
                logger.debug(f"Decoded token: {decoded_token}")
                user_id = decoded_token['uid']
                email = decoded_token.get('email')
                user = get_user_from_firestore(user_id)
                if user is None:
                    logger.info(f"User {user_id} not found. Creating new user.")
                    user = User(u_id=user_id, email=email)
                    save_user_to_firestore(user)
                session['user_id'] = user.get_user_id()
                session['email'] = email
                logger.info(f"User {user_id} logged in successfully.")
                return jsonify({'success': True})
            except firebase_admin.exceptions.InvalidIdTokenError:
                logger.error("Invalid ID token provided during login.")
                return jsonify({'success': False, 'message': 'Invalid ID token.'}), 401
            except firebase_admin.exceptions.ExpiredIdTokenError:
                logger.error("Expired ID token provided during login.")
                return jsonify({'success': False, 'message': 'Expired ID token.'}), 401
            except Exception as e:
                logger.error(f"Unexpected error during login: {e}")
                return jsonify({'success': False, 'message': 'An error occurred during login.'}), 500
        except Exception as e:
            logger.error(f"Error processing login request: {e}")
            return jsonify({'success': False, 'message': 'Internal server error.'}), 500
    else:
        logger.info("Rendering login page.")
        return render_template('login.html')

@app.route('/logout')
def logout():
    logger.info("User logged out.")
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/select_topics', methods=['GET', 'POST'])
@login_required
def select_topics():
    logger.info("Accessing /select_topics route.")
    user_id = session.get('user_id')
    user = get_user(user_id)
    if request.method == 'POST':
        logger.info("Received POST request on /select_topics.")
        selected_topics_ids = request.form.getlist('topics')
        logger.debug(f"Selected topics IDs: {selected_topics_ids}")
        selected_topics = []
        for tid in selected_topics_ids:
            try:
                tid_int = int(tid)
                topic = get_topic_by_id(tid_int)
                if topic:
                    selected_topics.append(topic)
            except ValueError:
                logger.warning(f"Invalid topic ID received: {tid}")
                continue
        if not selected_topics:
            logger.warning("No valid topics selected.")
            return render_template('select_topics.html', topics=get_all_active_topics(), error="Please select at least one topic.")
        # Generate quiz
        logger.info("Generating quiz based on selected topics.")
        quiz = Quiz(selected_topics)
        user.set_quiz(quiz)
        save_user_to_firestore(user)
        logger.info("Quiz generated and saved to user profile.")
        return redirect(url_for('take_quiz'))
    else:
        logger.info("Rendering select_topics page.")
        return render_template('select_topics.html', topics=get_all_active_topics())

@app.route('/quiz', methods=['GET', 'POST'])
@login_required
def take_quiz():
    logger.info("Accessing /quiz route.")
    user_id = session.get('user_id')
    user = get_user(user_id)
    quiz = user.get_quiz()
    if not quiz:
        logger.warning("No quiz found for user.")
        flash('No quiz found. Please select topics to start a quiz.', 'danger')
        return redirect(url_for('select_topics'))
    if request.method == 'POST':
        logger.info("Received POST request on /quiz.")
        user_answers = []
        for i in range(len(quiz.questions)):
            answer = request.form.get(f'question_{i}')
            if answer is None:
                # Handle unanswered questions
                user_answers.append('')
                logger.debug(f"Question {i} unanswered.")
            else:
                user_answers.append(answer)
                logger.debug(f"Question {i} answered with: {answer}")
        logger.info("Submitting user answers.")
        quiz.submission(user_answers)
        logger.info("Quiz submitted. Updating user performance.")
        user.set_latest_performance()
        save_user_to_firestore(user)
        logger.info("User performance updated.")
        return redirect(url_for('quiz_result'))
    else:
        logger.info("Rendering quiz page.")
        return render_template('quiz.html', quiz=quiz)

@app.route('/quiz_result')
@login_required
def quiz_result():
    logger.info("Accessing /quiz_result route.")
    user_id = session.get('user_id')
    user = get_user(user_id)
    quiz = user.get_quiz()
    if not quiz or not quiz.has_submitted():
        logger.warning("No quiz result available for user.")
        flash('No quiz result available.', 'danger')
        return redirect(url_for('select_topics'))
    result = quiz.get_result()
    logger.info(f"Rendering quiz result for user: {user_id}")
    return render_template('result.html', result=result)

if __name__ == '__main__':
    logger.info("Starting Flask application.")
    app.run(debug=True)