a=str(input("Enter text to write to the file: "))
try:
    file_handler="output.txt"
    with open(file_handler,"wt") as fh:
        fh.write(a)
        print("Data successfully written to output.txt")
except FileNotFoundError:
    print("File not found")

b=str(input("Enter additional text to append: "))
try:
    file_handler="output.txt"
    with open(file_handler,"a") as fh:
        fh.write("\n"+b)
        print("Data successfully appended to output.txt")

except FileNotFoundError:
    print("File not found")

finally:
    file_handler="output.txt"
    with open(file_handler,"r") as fh:
        print("Final content of output.txt")
        print(fh.read())