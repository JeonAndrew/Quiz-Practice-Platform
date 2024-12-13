from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
import firebase_admin
from firebase_admin import credentials, firestore, auth as firebase_auth
from functools import wraps
from flask_cors import CORS
import os
import logging
from models.Course import Course
from models.Topic import Topic
from models.Question import Question
from models.Quiz import Quiz
from models.User import User

app = Flask(__name__)

app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your-default-secret-key')
CORS(app, supports_credentials=True)

app.template_folder = os.path.abspath('../../quiz-frontend/templates')
app.static_folder = os.path.abspath('../../quiz-frontend/static')

service_account_path = '/Users/aummaneni/Quiz-Practice-Platform-1/quiz-backend/src/cs222-quiz-proj-firebase-adminsdk-k0qc4-0ab5ea04f1.json'
if not os.path.exists(service_account_path):
    raise FileNotFoundError(f"Service account key file not found at: {service_account_path}")

cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'danger')
            logger.info("Unauthorized access attempt to protected route.")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def save_user_to_firestore(user):
    try:
        logger.debug(f"Saving user {user.get_user_id()} to Firestore.")
        user_ref = db.collection('users').document(user.get_user_id())
        user_ref.set(user.to_dict())
        logger.info(f"User {user.get_user_id()} saved successfully.")
    except Exception as e:
        logger.error(f"Error saving user {user.get_user_id()} to Firestore: {e}")

def get_user_from_firestore(user_id):
    try:
        logger.debug(f"Retrieving user {user_id} from Firestore.")
        user_ref = db.collection('users').document(user_id)
        doc = user_ref.get()
        if doc.exists:
            user_data = doc.to_dict()
            user = User.from_dict(user_data, topics=None)
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

def get_all_courses():
    courses_list = []
    courses_ref = db.collection('courses').stream()
    for c_doc in courses_ref:
        c_data = c_doc.to_dict()
        course = {
            'course_id': c_doc.id,
            'name': c_data.get('name', '')
        }
        courses_list.append(course)
    return courses_list

def get_active_topics_for_course(course_id):
    topics_list = []
    topics_ref = db.collection('courses').document(str(course_id)).collection('topics').stream()
    for topic_doc in topics_ref:
        data = topic_doc.to_dict()
        if data.get('active', True):
            topic_obj = Topic(
                name=data.get('name'),
                t_id=int(topic_doc.id),
                proficiency=data.get('proficiency', 10),
                active=data.get('active', True)
            )
            topics_list.append(topic_obj)
    return topics_list

def get_topic_from_firestore(course_id, topic_id):
    topic_ref = db.collection('courses').document(str(course_id)).collection('topics').document(str(topic_id))
    doc = topic_ref.get()
    if doc.exists:
        data = doc.to_dict()
        topic = Topic(
            name=data.get('name'),
            t_id=int(topic_id),
            proficiency=data.get('proficiency', 10),
            active=data.get('active', True)
        )
        questions_ref = topic_ref.collection('questions').stream()
        for q_doc in questions_ref:
            q_data = q_doc.to_dict()
            question = Question(
                question=q_data.get('question'),
                options=q_data.get('options', []),
                correct_answer=q_data.get('correct_answer')
            )
            topic.add_question(question)
        return topic
    else:
        return None

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
            if not data:
                return jsonify({'success': False, 'message': 'No data provided.'}), 400
            id_token = data.get('idToken')
            if not id_token:
                return jsonify({'success': False, 'message': 'No ID token provided.'}), 400
            try:
                decoded_token = firebase_auth.verify_id_token(id_token)
                user_id = decoded_token['uid']
                email = decoded_token.get('email')
                if not email:
                    return jsonify({'success': False, 'message': 'Email not available.'}), 400
                user = get_user_from_firestore(user_id)
                if user is not None:
                    return jsonify({'success': False, 'message': 'User already exists.'}), 400
                user = User(u_id=user_id, email=email)
                save_user_to_firestore(user)
                session['user_id'] = user.get_user_id()
                session['email'] = email
                return jsonify({'success': True})
            except firebase_admin.exceptions.InvalidIdTokenError:
                return jsonify({'success': False, 'message': 'Invalid ID token.'}), 401
            except firebase_admin.exceptions.ExpiredIdTokenError:
                return jsonify({'success': False, 'message': 'Expired ID token.'}), 401
            except Exception as e:
                return jsonify({'success': False, 'message': 'An error occurred during signup.'}), 500
        except Exception as e:
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
            if not data:
                return jsonify({'success': False, 'message': 'No data provided.'}), 400
            id_token = data.get('idToken')
            if not id_token:
                return jsonify({'success': False, 'message': 'No ID token provided.'}), 400
            try:
                decoded_token = firebase_auth.verify_id_token(id_token)
                user_id = decoded_token['uid']
                email = decoded_token.get('email')
                user = get_user_from_firestore(user_id)
                if user is None:
                    user = User(u_id=user_id, email=email)
                    save_user_to_firestore(user)
                session['user_id'] = user.get_user_id()
                session['email'] = email
                return jsonify({'success': True})
            except firebase_admin.exceptions.InvalidIdTokenError:
                return jsonify({'success': False, 'message': 'Invalid ID token.'}), 401
            except firebase_admin.exceptions.ExpiredIdTokenError:
                return jsonify({'success': False, 'message': 'Expired ID token.'}), 401
            except Exception as e:
                return jsonify({'success': False, 'message': 'An error occurred during login.'}), 500
        except Exception as e:
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

@app.route('/select_course', methods=['GET', 'POST'])
@login_required
def select_course():
    if request.method == 'POST':
        selected_course_id = request.form.get('course')
        if not selected_course_id:
            flash('Please select a course.', 'danger')
            return redirect(url_for('select_course'))
        session['selected_course_id'] = selected_course_id
        return redirect(url_for('select_topics'))
    else:
        courses = get_all_courses()
        return render_template('select_course.html', courses=courses)

@app.route('/select_topics', methods=['GET', 'POST'])
@login_required
def select_topics():
    logger.info("Accessing /select_topics route.")
    user_id = session.get('user_id')
    user = get_user(user_id)

    course_id = session.get('selected_course_id')
    if not course_id:
        return redirect(url_for('select_course'))

    if request.method == 'POST':
        logger.info("Received POST request on /select_topics.")
        selected_topics_ids = request.form.getlist('topics')

        found_topics = []
        for tid_str in selected_topics_ids:
            topic = get_topic_from_firestore(course_id, tid_str)
            if topic and topic.is_active():
                found_topics.append(topic)

        if not found_topics:
            return render_template('select_topics.html', 
                                   topics=get_active_topics_for_course(course_id),
                                   error="Please select at least one topic.")

        logger.info("Generating quiz based on selected topics.")
        quiz = Quiz(found_topics)
        session['current_quiz'] = quiz.to_dict()
        # Initialize user answers array with empty strings
        session['user_answers'] = [""] * len(quiz.questions)
        session['current_question_index'] = 0  # Start at first question

        save_user_to_firestore(user)
        logger.info("Quiz generated. Redirecting to quiz.")
        return redirect(url_for('take_quiz'))
    else:
        logger.info("Rendering select_topics page.")
        return render_template('select_topics.html', topics=get_active_topics_for_course(course_id))

@app.route('/quiz', methods=['GET', 'POST'])
@login_required
def take_quiz():
    logger.info("Accessing /quiz route.")
    user_id = session.get('user_id')
    user = get_user(user_id)

    quiz_data = session.get('current_quiz')
    if not quiz_data:
        logger.warning("No quiz found for user.")
        flash('No quiz found. Please select topics to start a quiz.', 'danger')
        return redirect(url_for('select_topics'))

    topic_ids = quiz_data.get('question_topics', [])
    course_id = session.get('selected_course_id')
    reconstructed_topics = {}
    for t_id in set(topic_ids):
        t = get_topic_from_firestore(course_id, t_id)
        if t:
            reconstructed_topics[int(t_id)] = t

    from models.Question import Question
    reconstructed_questions = []
    for qd in quiz_data.get('questions', []):
        q = Question.from_dict(qd)
        reconstructed_questions.append(q)

    quiz = Quiz(topics=[])
    quiz.questions = reconstructed_questions
    quiz.question_topics = [reconstructed_topics[int(tid)] for tid in topic_ids if int(tid) in reconstructed_topics]
    quiz.question_correct = quiz_data.get('question_correct', [False]*len(quiz.questions))
    quiz.result = quiz_data.get('result', None)
    quiz.submission_status = quiz_data.get('submission_status', False)

    current_index = session.get('current_question_index', 0)
    user_answers = session.get('user_answers', [""] * len(quiz.questions))
    feedback_mode = session.get('feedback_mode', False)

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'check':
            # User pressed 'Check'
            selected_answer = request.form.get('answer_choice', None)
            if selected_answer is None:
                # No answer selected means user didn't pick any option, count as wrong
                user_answers[current_index] = ""
            else:
                user_answers[current_index] = selected_answer

            feedback_mode = True

        elif action == 'skip':
            # User pressed 'Skip'
            # No chosen answer, mark as wrong
            user_answers[current_index] = ""
            feedback_mode = True

        elif action == 'next':
            # User pressed 'Next' in feedback mode
            feedback_mode = False
            if current_index == len(quiz.questions) - 1:
                # Last question, finalize quiz
                quiz.submission(user_answers)

                # Update topic proficiencies in Firestore
                for t in set(quiz.question_topics):
                    topic_ref = db.collection('courses').document(str(course_id)).collection('topics').document(str(t.get_topic_id()))
                    topic_ref.update({'proficiency': t.get_proficiency()})

                user.set_latest_performance()

                quiz_ref = db.collection('users').document(user_id).collection('quizzes').document()
                quiz_data_for_save = {
                    'result': quiz.get_result(),
                    'timestamp': firestore.SERVER_TIMESTAMP,
                    'selected_topic_ids': [t.get_topic_id() for t in quiz.question_topics]
                }
                quiz_ref.set(quiz_data_for_save)

                save_user_to_firestore(user)

                session['last_quiz_result'] = quiz.get_result()
                # Clear quiz from session
                session.pop('current_quiz', None)
                session.pop('user_answers', None)
                session.pop('current_question_index', None)
                session.pop('feedback_mode', None)

                return redirect(url_for('quiz_result'))
            else:
                # Move to next question
                current_index += 1

        # Update session
        session['current_question_index'] = current_index
        session['user_answers'] = user_answers
        session['feedback_mode'] = feedback_mode

        return redirect(url_for('take_quiz'))
    else:
        # GET request - display current question
        current_question = quiz.questions[current_index]
        selected_answer = user_answers[current_index]

        correct_answer = current_question.get_correct_answer()
        is_correct = (selected_answer == correct_answer and selected_answer != "")
        is_skipped = (selected_answer == "" and feedback_mode)

        return render_template('quiz.html', 
                               question=current_question, 
                               question_number=current_index + 1, 
                               total_questions=len(quiz.questions),
                               feedback_mode=feedback_mode,
                               selected_answer=selected_answer,
                               correct_answer=correct_answer,
                               is_correct=is_correct,
                               is_skipped=is_skipped)
@app.route('/quiz_result')
@login_required
def quiz_result():
    logger.info("Accessing /quiz_result route.")
    result = session.get('last_quiz_result', None)
    if result is None:
        flash('No quiz result available.', 'danger')
        return redirect(url_for('select_topics'))

    logger.info(f"Rendering quiz result for user: {session.get('user_id')} with result {result}")
    return render_template('result.html', result=result)

if __name__ == '__main__':
    logger.info("Starting Flask application.")
    app.run(debug=True)

    