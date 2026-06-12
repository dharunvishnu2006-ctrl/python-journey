def read_file(filename):
    try:
        with open(filename,"r")as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("Error:File not found!")
    except PermissionError:
        print("Error: no permission to read file!")
    except Exception as e:
        print("unknown error:",e)                

read_file("students.csv")
read_file("unknown.txt")        