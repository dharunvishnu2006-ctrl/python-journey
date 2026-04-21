import logging

logging.basicConfig( 
    level=logging.DEBUG,
    format='%(levelname)s - %(message)s'
)

logging.debug("program started")
logging.warning("low battery")
logging.critical("system failure")