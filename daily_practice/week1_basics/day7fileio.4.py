with open("story.txt", "w") as f:
    f.write("Dharun is a future CISO. ")
    f.write("He loves coding in Python. ")
    f.write("He will work at Google one day. ")
    f.write("His father Jaganathan supports him always.")

with open("story.txt","r")as f:
    content = f.read()
    words = content.split()
    unique = set(words)

    print("Total words:",len(words))
    print("Unique words:",len(unique))
