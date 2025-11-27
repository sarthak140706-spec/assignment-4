📘 Python File Handling – Assignment README
Task 1: Read a File and Handle Errors
📌 Problem Statement

Write a Python program that:

Opens and reads a text file named sample.txt

Prints its content line by line

Handles errors gracefully if the file does not exist

📝 Program Description

This program checks for the presence of the file sample.txt and reads its contents one line at a time.
If the file is missing, the program displays a clear, user-friendly error message instead of crashing.
The goal of the task is to demonstrate safe file handling using exception management.

✅ Expected Output
✔ If the file exists:

The program will display:

A message indicating that file reading has begun

Each line of the file printed sequentially

❌ If the file does not exist:

The program will display the message:
"File not found"

Task 2: Write and Append Data to a File
📌 Problem Statement

Write a Python program that:

Takes user input and writes it to a file named output.txt

Appends additional user input to the same file

Reads and displays the final content of the file

📝 Program Description

This program collects text input from the user and writes it to output.txt.
It then accepts more input and appends it to the same file without overwriting the existing content.
Finally, the program reads and displays everything stored in the file, showing both the original and appended text.

💬 Example Expected Output

If the user enters:

First input: 25

Second input: Hello

Then the final output displayed to the user will be:

25
Hello


Along with messages confirming that data was successfully written and appended to the file.
