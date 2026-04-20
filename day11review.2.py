import logging
logging.basicConfig(level=logging.DEBUG)
name =str(input("enter a name:"))
with open("greeting.txt","w") as f:
    f.write(f"Hello {name}!")
with open("greeting.txt","r") as f:
    content=f.read()
    print(content) 

if name == '':
    logging.warning("the name is empty!")  
else:
    logging.info("the name is valid!")
