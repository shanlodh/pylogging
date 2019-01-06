import logging
import logging.config
from app1 import myprint

logging.config.fileConfig(fname='logging.config', disable_existing_loggers=False)

myprint()

# Get the logger specified in the file
logger = logging.getLogger('testLogger')

logger.error('This is a debug message')