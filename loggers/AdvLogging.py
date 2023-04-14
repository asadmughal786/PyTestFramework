
import logging

class AdvLoggerDemo:
    def logger_conf(self):
        # creat logger 
        logger = logging.getLogger("Demolog")
        logger.setLevel(logging.DEBUG)

        # create console handler or file handler and set the log level
        ch = logging.StreamHandler()
        fh = logging.FileHandler('demoLogger.log')

        # create formatter - how you want to show the logs to be formatted
        formatter = logging.Formatter(format='%(asctime)s -%(levelname)s -%(name)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        # add handler to the file or console
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        #add console handler to the file.
        logger.addHandler(ch)
        logger.addHandler(fh)