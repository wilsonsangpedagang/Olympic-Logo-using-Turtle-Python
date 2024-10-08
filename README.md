Overview
This program creates a graphical representation of the Olympic logo and a colorful chessboard using Python's turtle graphics library. 
Users can customize the number of rows and the size of the chessboard squares through prompts.

Features
Olympic Logo: Draws the five interlocking circles of the Olympic logo in blue, yellow, black, green, and red.
Customizable Chessboard: Allows users to specify the number of rows and the size of each square, generating a chessboard filled with randomly colored squares.
Interactive User Input: Uses turtle.numinput() to gather user preferences for the chessboard dimensions.
Colorful Graphics: Generates vibrant and randomly colored squares for an engaging visual experience.

Requirements
Python 3.x
Turtle Graphics Library (included with standard Python installation)

Installation
Ensure you have Python installed on your system.
Copy the provided code into a Python file (e.g., olympic_logo_chessboard.py).
Run the script using a Python interpreter.

Usage
When you run the program, two prompts will appear:
Rows: Enter the number of rows for the chessboard (between 2 and 25).
Size: Enter the size of each square (between 0 and 50).
The program will then draw the Olympic logo followed by a colorful chessboard based on the input provided.
Click anywhere on the turtle graphics window to exit the program.

Code Structure

Imports:
tkinter.messagebox: For displaying prompts.
turtle: For drawing graphics.
random: For generating random colors.
Color Definitions: RGB tuples for the Olympic logo colors.
User Input: Uses turtle.numinput() to gather the number of rows and the size of the chessboard squares.
Drawing Functions:
Draws the Olympic logo by positioning the turtle and using turtle.circle().
Constructs the chessboard by using nested loops to create squares and filling them with random colors.

License
This program is open-source and can be modified or distributed freely. For personal use and educational purposes.

Acknowledgments
This program leverages the turtle graphics library, which is a popular tool for introducing programming concepts and creating visual projects in Python.
