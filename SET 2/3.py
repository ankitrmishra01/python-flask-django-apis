#A program that reads a text file and counts the number of words in it
def count(path):
    try:
        with open(path, 'r') as file:
            file_content = file.read()
            print(f"File content: {repr(file_content)}")  # Debugging line
            return f"data = {file_content.split()}\nlength of the words: {len(file_content.split())}"
    except FileNotFoundError:
        return "Please Provide valid file path."

path = "example.txt"
print(count(path))
