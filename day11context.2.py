import logging
logging.basicConfig(level=logging.DEBUG)

with open("log.txt","w")as f:
    f.write("app started\n")
    f.write("user logged in\n")
    f.write("app closed\n")
with open("log.txt","r")as f:
    content = f.read()
    print(content)

logging.info("File operation successful!")    