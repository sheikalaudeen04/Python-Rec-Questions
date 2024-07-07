def copy_file(sou_f, desti_f):
    try:
        with open(sou_f,'r') as source:
            with open(desti_f, 'w') as dest:
                dest.write(source.read())
        print("File copied successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

sou_p =input("Enter source file path: ").strip('"')
desti_p = input("Enter destination file: ").strip('"')
copy_file(sou_p, desti_p)
