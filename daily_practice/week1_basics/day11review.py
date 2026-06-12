import logging
logging.basicConfig(level=logging.INFO) 

with open("results.txt","w") as f:
    f.write("erode\n")
    f.write("tirupur\n")
    f.write("uthukuli\n")

with open("results.txt","r")as f:
    content=f.read()
    print(content)

logging.info("File written successfully!")    