try:
    file_handler = "sample.txt"
    with open(file_handler, "r") as fh:
        data = fh.read()
        print("Reading file content")
        print(data)
except FileNotFoundError:
    print("File not found")