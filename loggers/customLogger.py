import inspect
import logging

class CustLogger:
    def custlogger(self,logLevel = logging.DEBUG):
        # set the class/method name from where it's called
        logger_name = inspect.stack()[1][3]
        # creat logger 
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        # create console handler or file handler and set the log level
        fh = logging.FileHandler("automation.log")
        # creat formatter - how to you want you logs to be look like 
        formatter = logging.Formatter(format='%(asctime)s -%(levelname)s -%(name)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        # Add formatter to the console or file
        fh.setFormatter(formatter)
        # Add console handler to the logger 
        logger.handlers(fh)
        return logger
        
