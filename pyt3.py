def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            return num_words
    except FileNotFoundError:
        print("File not found!")

file_path = input("Enter the file path: ").strip('"')  
word_count = count_words(file_path)
if word_count:
    print("The number of words in the file is:",word_count)
