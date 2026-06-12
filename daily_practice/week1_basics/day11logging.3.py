import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

logging.debug("App started")
logging.info("User logged in")
logging.warning("Low memory!")
logging.error("File not found!")
logging.critical("System crash!")