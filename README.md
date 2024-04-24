# Calculator
A simple desktop calculator built with Python and PyQt6. It features a clean user interface and basic arithmetic functionalities.

<br>
<p align="center"><img width="403" src="https://github.com/NakerTheFirst/Calculator/blob/main/screenshot.png" alt="Image of an interface of a calculator app"></p>
<p align="center">Calculator's Graphical User Interface</p>

## Features
- Basic Arithmetic Operations: Allows addition, subtraction, multiplication, and division
- User-friendly Interface: Features a clear layout with large, easily clickable buttons and a display area for input and results
- Responsive Design: Automatically handles user input errors such as division by zero (and calls you a moron!)

## Structure
- **MainApp** class serves as an engine, which boots the whole app up
- **UI** class is responsible for rendering interactible GUI
- **Logic** class handles the business logic of the app
- **Button** class in a template for Button objects rendered in the interface

This structure promotes modularity, reusability and single responsibility design principles.

## Dependencies
To run the app, ensure you have the following:
- Python 3.6 or higher
- PyQt6

## Installation
1. Install PyQt6 if not already installed
2. Clone or download this repository to your local machine

## How to Run
1. Navigate to the directory containing the calculator code
2. Run the script using Python: `python main.py`

**Ensure the name of the file is main.py** - the app will not work otherwise
