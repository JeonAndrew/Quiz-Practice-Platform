# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify, request

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# Sample question data
QUESTION_DATA = {
    "question": "What is your favorite programming language?",
    "options": ["JavaScript", "Python", "Java", "C++", "Ruby"],
    "answer": "Python"
}

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

@app.route('/api/question', methods=['GET'])
def get_question():
    """
    Returns the question and its options.
    """
    # this just returns the declared question data
    return jsonify(QUESTION_DATA)

@app.route('/api/submit', methods=['POST'])
def submit_answer():
    """
    Accepts the selected option from the user.
    """
    # get the selected answer option from frontend
    data = request.get_json()
    # ensure that there is data and that the "selected_option" field is there
    if not data or 'selected_option' not in data:
        return jsonify({"error": "Invalid input"}), 400

    selected_option = data['selected_option']

    # we should check if the answer is correct right here

    # return the selected option in this format to the frontend
    return jsonify({"message": "Answer submitted successfully!", "selected_option": selected_option}), 200

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server
    app.run(debug=True)
