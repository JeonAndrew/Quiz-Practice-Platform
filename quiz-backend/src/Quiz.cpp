#include "Quiz.h"
#include "User.h"
#include <utility>
#include "Question.h"

void Quiz::setResult(double score) {
    result_ = score;
}

double Quiz::getResult() {
    return result_;
}

void Quiz::generateQuestions(std::map<std::string, int> profs) {
    // First step is to sum all of the proficiency scores to calculate the percentages
    int sum = 0;
    for (const auto & [key, value] : profs) {
        sum += value;
    }
    // Passing each percentage interval into a vector with the topic name linked to the percentage
    // If there were 5 topics with the same proficiency, we would have a vector of: [0.20, 0.40, 0.60, 0.80, 1.00]
    std::vector<std::pair<std::string, double>> percents;
    double nextVal = 0.0;
    for (const auto & [key, value] : profs) {
        std::pair<std::string, double> topicOdds;
        topicOdds.first = key;
        topicOdds.second = (nextVal + (20 - value) / sum);
        percents.push_back(topicOdds); // maybe change if we dont want 0% chance for mastered topic
        nextVal++;
    }
    // Generating a random number and seeing where it lies on the percentage vector and generating a question of that topic
    // Then passing a quesion with that topic to the questions_ vector
    for (unsigned int i = 0; i < 15; i++) {
        double random = static_cast <double> (rand()) / ( static_cast <double> (RAND_MAX)); 
        for (unsigned int j = 0; j  < percents.size(); j++) {
            if (random <= percents[j].second) {
                questions_.push_back(Question(percents[j].first));
            }
        }
    }
}

std::vector<Question> Quiz::getQuestions() {
    return questions_;
}