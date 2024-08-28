# FlashCards

## Overview

The Flashcard Quiz App is a simple command-line application that allows users to create, store, and study flashcards. You can add flashcards with questions and answers, and then quiz yourself to test your knowledge.

## Features

- Add new flashcards with questions and answers.
- Take a quiz to test your knowledge with the flashcards.
- View your score after the quiz.

## Installation

To run the Flashcard Quiz App, you need to have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/).

### Clone the Repository

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/alebora/flashcards.git

2. Navigate into the project directory:

    ```bash
    cd flashcards

## Usage

1. **Run the application**:
   - Open a terminal in the project directory.
   - Run the `main.py` file with Python.

2. **Follow the on-screen menu** to add flashcards or take a quiz.

## Menu Options

- Add Flashcard: Add a new flashcard with a question and answer.
- Take Quiz: Start a quiz with the existing flashcards and view your score.
- Exit: Close the application. 

## File Format

`flashcards.json`: This file stores the flashcards in JSON format. The app reads from and writes to this file to persist flashcards between sessions.

Example content of `flashcards.json`:

    ```bash
    [
        {
            "question": "What is the capital of France?",
            "answer": "Paris"
        }
    ] 

## Example 

    ```bash
    Flashcard Quiz App
    1. Add Flashcard
    2. Take Quiz
    3. Exit
    Enter your choice: 1
    Enter the question: What is the largest planet in our solar system?
    Enter the answer: Jupiter
    Flashcard added!

    Flashcard Quiz App
    1. Add Flashcard
    2. Take Quiz
    3. Exit
    Enter your choice: 1
    Enter the question: What is the smallest planet in our solar system?   
    Enter the answer: Mercury
    Flashcard added!

    Flashcard Quiz App
    1. Add Flashcard
    2. Take Quiz
    3. Exit
    Enter your choice: 2
    Q: What is the largest planet in our solar system? Jupiter 
    Correct!:)
    Q: What is the smallest planet in our solar system?  Mars
    Incorrect, the correct answer is: Mercury
    Your final score is: 1/2

    Flashcard Quiz App
    1. Add Flashcard
    2. Take Quiz
    3. Exit
    Enter your choice: 3
    Thank you, keep studying hard! Byebye!