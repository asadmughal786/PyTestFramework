import logging

logging.basicConfig(level=logging.DEBUG,filename='./loggers/logs/automation.log',filemode='a')  # Configuring the logging file.

logging.debug('this is debug logging')  #it dont print
logging.debug('this is debug logging')  #it dont print
logging.info('this is info Log') # it dont print generally
logging.warning("This is warning log")
logging.error('This is error log')
logging.critical('this is critical logging')

