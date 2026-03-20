Basic Python Calculator
A simple, interactive command-line calculator written in Python. This script allows users to perform fundamental arithmetic operations on two integers, complete with basic error handling for invalid operations and division by zero.

Features
Interactive Prompts: Takes user input directly from the command line.

Core Arithmetic: Supports addition (+), subtraction (-), multiplication (*), and division (/).

Error Handling: * Prevents program crashes by explicitly checking for division by zero.

Catches invalid operator inputs and alerts the user.

Prerequisites
You only need Python installed on your system to run this script.

Python 3.x is recommended.

How to Run
Open your terminal or command prompt.

Navigate to the directory where calculator.py is saved.

Execute the script using the following command:

Bash
python calculator.py
Usage Examples
Example 1: Standard Multiplication

Plaintext
Enter first number: 128
Enter second number: 4
Enter operation (+, -, *, /): *

--- Result ---
128 * 4 = 512
Example 2: Division by Zero Handling

Plaintext
Enter first number: 256
Enter second number: 0
Enter operation (+, -, *, /): /

--- Result ---
Division by zero is not allowed ❌
Example 3: Invalid Operation

Plaintext
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): ^

--- Result ---
Invalid operation ❌
