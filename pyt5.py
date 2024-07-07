def capitalize_words(sou_f, desti_f):
    try:
        with open(sou_f, 'r') as source:
            modified_content = ' '.join(word.capitalize() for word in source.read().split())
            with open(desti_f, 'w') as dest:
                dest.write(modified_content)
        print("First letter of each word capitalized and written to the destination file!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

sou_p =input("Enter source file path: ").strip('"')
desti_p = input("Enter destination file: ").strip('"')
capitalize_words(sou_p, desti_p)
