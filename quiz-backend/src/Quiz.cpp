#include <utility>
#include "Quiz.h"

Quiz::Quiz(std::vector<Topic>& topics) {
    // First step is to sum all of the proficiency scores for active topics
    int sum = 0;
    for (Topic t : topics) {
        if (t.isActive()) {
            sum += t.getProficiency();
        }
    }
    // Passing each percentage interval into a vector with the topic name linked to the percentage
    // If there were 5 topics with the same proficiency, we would have a vector of: [0.20, 0.40, 0.60, 0.80, 1.00]
    std::vector<std::pair<std::Topic, double>> percents;
    double nextVal = 0.0;
    for (Topic t : topics) {
        std::pair<Topic, double> topicOdds;
        if (t.isActive()) {
            topicOdds.first = t;
            topicOdds.second = (nextVal + (kMaxProficiency - t.getProficiency()) / sum);
            percents.push_back(topicOdds); // maybe change if we dont want 0% chance for mastered topic
            nextVal += (kMaxProficiency - t.getProficiency()) / sum;
        }
    }
    // Generating a random number and seeing where it lies on the percentage vector to 
    // see what type of topic this question is and then taking a random question from that topic
    for (unsigned int i = 0; i < kNumQuestions; i++) {
        std::srand(static_cast<unsigned int>(time(0))); // Might need review on this line
        double random = static_cast <double> (rand()) / ( static_cast <double> (RAND_MAX)); 
        for (unsigned int j = 0; j  < percents.size(); j++) {
            if (random <= percents[j].second) {
                questions_.push_back(percents[j].first.getRandomQuestion());
            }
        }
    }
}

double Quiz::getResult() const {
    return result_;
}

std::vector<Question> Quiz::getQuestions() const {
    return questions_;
}

bool hasSubmitted() const {
    return submissionStatus;
}

// Receives the User's answers in the order they are given to them and checks how many answers match the correct
// answer and then sets the result
void Quiz::submission(std::vector<std::string>& answers) {
    int countCorrect = 0;
    for (unsigned int i = 0; i < questions_.size(); i++) {
        if (questions_[i].isCorrect(userAnswers_[i])) {
            questionCorrect[i] == true;
            countCorrect++;
        } else {
            questionCorrect[i] == false;
        }
    }
    result_ = countCorrect / questions_.size();
    submissionStatus = true;
}