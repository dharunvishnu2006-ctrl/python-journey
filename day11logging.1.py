import logging
logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.warning("This is a WARNING message")
logging.info("This is an INFO message")
logging.debug("This is a DEBUG message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")