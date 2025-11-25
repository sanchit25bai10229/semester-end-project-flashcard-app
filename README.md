Flashcard Tutor: A Python/Tkinter Study App

The Flashcard Tutor is a simple, customizable desktop application designed to aid in memorization and self-quizzing using a classic flashcard format. It utilizes Python's standard tkinter library for the GUI and reads all study material from a local CSV file, making it highly adaptable for any subject.

✨ Features

Data-Driven: All flashcard content is loaded from a simple cards.csv file, allowing users to easily customize their study decks.

Intuitive Interface: A clean, dark-themed interface built with tkinter focusing on readability.

Spaced Repetition Simulation: Users evaluate their knowledge ("I KNEW IT" or "I MISSED IT") to track progress and score.

Keyboard Shortcuts:

Press R (or r) to Reveal the answer.

Press Y (or y) to mark the card as Known (Yes).

Press N (or n) to mark the card as Missed (No).

Robust Data Loading: Includes error handling for missing files, empty files, or incorrectly formatted headers.

🚀 Setup and Usage

Prerequisites

You only need Python (3.x recommended). No external libraries are required as the app uses tkinter, csv, and random, which are part of the standard library.

1. File Structure

Ensure you have the following two files in the same directory:

flashcard_tutor.py (The main application code)

cards.csv (Your study data)

2. Prepare cards.csv

Your CSV file MUST contain a header row with at least two columns: Question and Answer.

Example cards.csv content:

Question,Answer
What is the capital of France?,Paris
What chemical element has the symbol 'Fe'?,Iron
Who wrote "To Kill a Mockingbird"?,Harper Lee


3. Run the Application

Open your terminal or command prompt in the directory containing the files and run:

python flashcard_tutor.py


The application window will open, and the quiz will start immediately.

4. Taking the Quiz

Read the Question.

Click "REVEAL ANSWER (R)" or press R.

Evaluate your performance by clicking "I KNEW IT (Y)" or "I MISSED IT (N)", or by pressing Y or N.

The app will automatically move to the next card and update your score in the status bar.
