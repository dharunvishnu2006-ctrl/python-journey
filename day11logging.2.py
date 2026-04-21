import logging 
logging.basicConfig(
    level=logging.DEBUG
)
num = int(input("Enter a number:"))
if num < 0:
    logging.warning("you entered a negative number!")
elif num == 0:
    logging.error("you entered zero!")
else:
    logging.info("you entered a positive number!")        