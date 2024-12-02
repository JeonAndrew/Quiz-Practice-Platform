// #define CATCH_CONFIG_MAIN
#include <catch2/catch_test_macros.hpp>
#include "Question.h"
#include "Topic.h"
#include "Course.h"
#include "Quiz.h"
#include "User.h"

// Function(s) to be tested
int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

// Test cases
TEST_CASE("Addition tests", "[add]") {
    REQUIRE(add(2, 2) == 4);
    REQUIRE(add(-1, 1) == 0);
}

TEST_CASE("Subtraction tests", "[subtract]") {
    SECTION("Positive numbers") {
        REQUIRE(subtract(10, 5) == 5);
    }

    SECTION("Negative numbers") {
        REQUIRE(subtract(-5, -5) == 0);
    }
    
    SECTION("Mixed positive and negative numbers") {
        REQUIRE(subtract(5, -5) == 10);
    }
}

TEST_CASE("Questions tests", "[question]") {
    std::vector<std::string> options;
    std::string a = "Hello";
    std::string b = "Hey";
    std::string c = "Hi";
    std::string d = "Goodbye";
    options.push_back(a);
    options.push_back(b);
    options.push_back(c);
    options.push_back(d);
    Question q1 = Question("Which of these is not a greeting?", options, d);
    REQUIRE(q1.isCorrect(a) == false);
    REQUIRE(q1.isCorrect(b) == false);
    REQUIRE(q1.isCorrect(c) == false);
    REQUIRE(q1.isCorrect("") == false);
    REQUIRE(q1.isCorrect(d) == true);
}

TEST_CASE("Topics tests", "[topics]") {
    Topic t1 = Topic("Misc Topic", 001, 10);

    std::vector<std::string> options1;
    options1.push_back("Hello");
    options1.push_back("Hey");
    options1.push_back("Hi");
    options1.push_back("Goodbye");
    Question q1 = Question("Which of these is not a greeting?", options1, "Goodbye");

    std::vector<std::string> options2;
    options2.push_back("1");
    options2.push_back("2");
    options2.push_back("3");
    options2.push_back("4");
    Question q2 = Question("What is 2 + 2?", options2, "4");

    std::vector<std::string> options3;
    options3.push_back("2147483648");
    options3.push_back("123456789");
    options3.push_back("987654321");
    options3.push_back("42");
    Question q3 = Question("what is 2147483647 + 1?", options3, "2147483648");

    t1.addQuestion(q1);
    t1.addQuestion(q2);
    t1.addQuestion(q3);

    SECTION("Constructor and get functions") {
        REQUIRE("Misc Topic" == t1.getName());
        REQUIRE(001 == t1.getTopicID());
        REQUIRE(10 == t1.getProficiency());
    }

    SECTION("increment decrement test") {
        for (int i = 0; i < 3; ++i) {
            t1.increment();
        }
        REQUIRE(13 == t.getProficiency());

        for (int i = 0; i < 10; ++i) {
            t1.increment();
        }
        REQUIRE(20 == t.getProficiency());

        t1.decrement();
        REQUIRE(19 == t.getProficiency());

        for (int i = 0; i < 20; ++i) {
            t1.decrement();
        }
        REQUIRE(0 == t1.getProficiency());

        for (int i = 0; i < 10; ++i) {
            t1.increment();
        }
        REQUIRE(10 == t1.getProficiency());
    }
    
    SECTION("activate deactivate test") {
        t1.activate();
        REQUIRE(10 == t1.getProficiency());
        REQUIRE(t1.isActive == true);

        t.deactivate();
        REQUIRE(t1.isActive == false);

        t.activate();
        REQUIRE(10 == t.getProficiency());
        REQUIRE(t1.isActive == true);
    }
}

TEST_CASE("Quiz tests", "[quiz]") {
    Topic t1 = Topic("Addition", 001, 10);
    
    std::vector<std::string> options1;
    options1.push_back("1");
    options1.push_back("2");
    options1.push_back("3");
    options1.push_back("4");
    Question q1 = Question("1 + 1 = ?", options1, "2");

    std::vector<std::string> options2;
    options2.push_back("1");
    options2.push_back("2");
    options2.push_back("3");
    options2.push_back("4");
    Question q2 = Question("1 + 2 = ?", options2, "3");

    std::vector<std::string> options3;
    options3.push_back("1");
    options3.push_back("2");
    options3.push_back("3");
    options3.push_back("4");
    Question q3 = Question("2 + 2 = ?", options3, "4");

    std::vector<std::string> options4;
    options4.push_back("5");
    options4.push_back("7");
    options4.push_back("8");
    options4.push_back("9");
    Question q4 = Question("2 + 3 = ?", options4, "5");

    std::vector<std::string> options5;
    options5.push_back("5");
    options5.push_back("7");
    options5.push_back("8");
    options5.push_back("9");
    Question q5 = Question("3 + 3 = ?", options5, "6");

    std::vector<std::string> options6;
    options6.push_back("5");
    options6.push_back("7");
    options6.push_back("8");
    options6.push_back("9");
    Question q6 = Question("3 + 4 = ?", options6, "7");

    std::vector<std::string> options7;
    options7.push_back("5");
    options7.push_back("7");
    options7.push_back("8");
    options7.push_back("9");
    Question q7 = Question("4 + 4 = ?", options7, "8");

    std::vector<std::string> options8;
    options8.push_back("5");
    options8.push_back("7");
    options8.push_back("8");
    options8.push_back("9");
    Question q8 = Question("4 + 5 = ?", options8, "9");

    std::vector<std::string> options9;
    options9.push_back("10");
    options9.push_back("11");
    options9.push_back("12");
    options9.push_back("13");
    Question q9 = Question("5 + 5 = ?", options9, "10");

    std::vector<std::string> options10;
    options10.push_back("10");
    options10.push_back("11");
    options10.push_back("12");
    options10.push_back("13");
    Question q10 = Question("5 + 6 = ?", options10, "11");

    std::vector<std::string> options11;
    options11.push_back("10");
    options11.push_back("11");
    options11.push_back("12");
    options11.push_back("13");
    Question q11 = Question("6 + 6 = ?", options11, "12");

    std::vector<std::string> options12;
    options12.push_back("10");
    options12.push_back("11");
    options12.push_back("12");
    options12.push_back("13");
    Question q12 = Question("6 + 7 = ?", options12, "13");

    std::vector<std::string> options13;
    options13.push_back("14");
    options13.push_back("15");
    options13.push_back("16");
    options13.push_back("17");
    Question q13 = Question("7 + 7 = ?", options13, "14");

    std::vector<std::string> options14;
    options14.push_back("14");
    options14.push_back("15");
    options14.push_back("16");
    options14.push_back("17");
    Question q14 = Question("7 + 8 = ?", options14, "15");

    std::vector<std::string> options15;
    options15.push_back("14");
    options15.push_back("15");
    options15.push_back("16");
    options15.push_back("17");
    Question q15 = Question("8 + 8 = ?", options15, "16");

    t1.addQuestion(q1);
    t1.addQuestion(q2);
    t1.addQuestion(q3);
    t1.addQuestion(q4);
    t1.addQuestion(q5);
    t1.addQuestion(q6);
    t1.addQuestion(q7);
    t1.addQuestion(q8);
    t1.addQuestion(q9);
    t1.addQuestion(q10);
    t1.addQuestion(q11);
    t1.addQuestion(q12);
    t1.addQuestion(q13);
    t1.addQuestion(q14);
    t1.addQuestion(q15);

    Topic t2 = Topic("Multiplication", 002, 10);

    std::vector<std::string> options16;
    options16.push_back("1");
    options16.push_back("2");
    options16.push_back("3");
    options16.push_back("4");
    Question q16 = Question("1 * 1 = ?", options16, "1");

    std::vector<std::string> options17;
    options17.push_back("1");
    options17.push_back("2");
    options17.push_back("3");
    options17.push_back("4");
    Question q17 = Question("1 * 2 = ?", options17, "2");

    std::vector<std::string> options18;
    options18.push_back("1");
    options18.push_back("2");
    options18.push_back("3");
    options18.push_back("4");
    Question q18 = Question("1 * 3 = ?", options18, "3");

    std::vector<std::string> options19;
    options19.push_back("1");
    options19.push_back("2");
    options19.push_back("3");
    options19.push_back("4");
    Question q19 = Question("1 * 4 = ?", options19, "4");

    std::vector<std::string> options20;
    options20.push_back("5");
    options20.push_back("6");
    options20.push_back("7");
    options20.push_back("8");
    Question q20 = Question("1 * 5 = ?", options20, "5");
    
    std::vector<std::string> options21;
    options21.push_back("5");
    options21.push_back("6");
    options21.push_back("7");
    options21.push_back("8");
    Question q21 = Question("1 * 6 = ?", options21, "6");

    std::vector<std::string> options22;
    options22.push_back("5");
    options22.push_back("6");
    options22.push_back("7");
    options22.push_back("8");
    Question q22 = Question("1 * 7 = ?", options22, "7");

    std::vector<std::string> options23;
    options23.push_back("5");
    options23.push_back("6");
    options23.push_back("7");
    options23.push_back("8");
    Question q23 = Question("1 * 8 = ?", options23, "8");

    std::vector<std::string> options24;
    options24.push_back("9");
    options24.push_back("10");
    options24.push_back("11");
    options24.push_back("12");
    Question q24 = Question("1 * 9 = ?", options24, "9");

    std::vector<std::string> options25;
    options25.push_back("9");
    options25.push_back("10");
    options25.push_back("11");
    options25.push_back("12");
    Question q25 = Question("1 * 10 = ?", options25, "10");

    std::vector<std::string> options26;
    options26.push_back("9");
    options26.push_back("10");
    options26.push_back("11");
    options26.push_back("12");
    Question q26 = Question("1 * 11 = ?", options26, "11");

    std::vector<std::string> options27;
    options27.push_back("9");
    options27.push_back("10");
    options27.push_back("11");
    options27.push_back("12");
    Question q27 = Question("1 * 12 = ?", options27, "12");

    std::vector<std::string> options28;
    options28.push_back("13");
    options28.push_back("14");
    options28.push_back("15");
    options28.push_back("16");
    Question q28 = Question("1 * 12 = ?", options28, "13");

    std::vector<std::string> options29;
    options29.push_back("13");
    options29.push_back("14");
    options29.push_back("15");
    options29.push_back("16");
    Question q29 = Question("1 * 12 = ?", options29, "14");

    std::vector<std::string> options30;
    options30.push_back("13");
    options30.push_back("14");
    options30.push_back("15");
    options30.push_back("16");
    Question q30 = Question("1 * 12 = ?", options30, "15");

    t2.addQuestion(q16);
    t2.addQuestion(q17);
    t2.addQuestion(q18);
    t2.addQuestion(q19);
    t2.addQuestion(q20);
    t2.addQuestion(q21);
    t2.addQuestion(q22);
    t2.addQuestion(q23);
    t2.addQuestion(q24);
    t2.addQuestion(q25);
    t2.addQuestion(q26);
    t2.addQuestion(q27);
    t2.addQuestion(q28);
    t2.addQuestion(q29);
    t2.addQuestion(q30);

    Course c1("Math", 001);
    c1.addTopic(t1);
    c1.addTopic(t2);

    SECTION("Constructor") {
        Quiz q1(c1.getTopics());
        // Test if the quiz generates the correct amount of questions
        REQUIRE(q1.getQuestions().size() == 15);

        // Test if quiz constructor generates quiz of only activated questions
        t1.deactivate();
        Quiz q2(c1.getTopics());
        for (Question que : q2.getQuestions()) {
            REQUIRE(t1.containsQuestion(que.getQuestion()));
        }
    }

     SECTION("Quiz grader") {
        std::vector<std::string> answers;
        for (unsigned int i = 0; i < q1.getQuestions.size(); i++) {
            if (i % 2 == 0) {
                answers.push_back(q1.getQuestions()[i].getCorrectAnswer());
            } else {
                answers.push_back("-1");
            }
        }
        q1.submission(answers);
        REQUIRE(submissionStatus == true);
        double expectedScore = 7 / 15;
        REQUIRE(q1.getResult() == expectedScore);
     }
}

TEST_CASE("Course tests") {
    Course c = Course("CS225", 1);
    REQUIRE("CS225" == c.getName());
    REQUIRE(1 == c.getCourseID());
}