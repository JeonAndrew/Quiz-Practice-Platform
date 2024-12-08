import React, { useState } from "react";
import "./QuestionPanel.css";

const QuestionPanel = ({ question, options }) => {

  const [selectedOption, setSelectedOption] = useState(null);
  const [submittedOption, setSubmittedOption] = useState(null);

  const handleOptionClick = (index) => {
    setSelectedOption(index);

  };

// we should probably implement calls to the backend on these handlers

// handle user using check answer button
  const handleAnswerSubmit = () => {
    if (selectedOption !== null) {
      setSubmittedOption(selectedOption);
    }
  };

//handle user using skip buttom
  const handleSkipSubmit = () => {
    if (selectedOption !== null) {
      setSubmittedOption(selectedOption);
    }
  };

  return (
    <div className="question-container">
      <h2 className="question">{question}</h2>
      <div className="options-container">
        {/* display the answer choices as buttons */}
        {options.map((option, index) => (
          <button
            key={index}
            onClick={() => handleOptionClick(index)}
            className={`option-button ${
              selectedOption === index ? "selected" : ""
            }`}
          >
            <h3>{option}</h3>
          </button>
        ))}
      </div>
      {/* skip button if user doesn't know answere */}
      <button
        onClick={handleSkipSubmit}
        className="skip-button"
      >
        <h4>Skip</h4>
      </button>
      {/* submit button to check against answer */}
      <button
        onClick={handleAnswerSubmit}
        className="submit-button"
        disabled={selectedOption === null}
      >
        <h4>Check</h4>
      </button>
      {/* show submitted choice after click
        this can also be a point to call the backend */}
      {submittedOption !== null && (
        <p className="submitted-option">
            submitted choice: {options[submittedOption]}
        </p>
      )}
    </div>
  );
};

export default QuestionPanel;
