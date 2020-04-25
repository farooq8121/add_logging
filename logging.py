import os
from logging.handlers import RotatingFileHandler
path=os.getcwd()


def getLogger(name):


    logger = logging.Logger(name)
    logger.setLevel(logging.DEBUG)

    #handler = logging.FileHandler(os.path.join(path, name + '.log'), 'a')
    # Create the rotating file handler. Limit the size to 10000000Bytes ~ 10MB .
    logfilename=os.path.join(path, name + '.log')
    handler = RotatingFileHandler(logfilename, mode='a', maxBytes=10000000, backupCount=10, encoding=None, delay=0)
    
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s, %(levelname)s,%(message)s,%(name)s',"%Y-%m-%d %H:%M:%S" )
    handler.setFormatter(formatter)

    # add the handlers to the logger   
    logger.addHandler(handler)

            
    return logger
    
    
    
    ####  getLogger('umar').warning("access_token generated")
    
    ###This will create a new log file with the name as input
    ### 2020-04-24 08:00:27, WARNING ,access_token generated,umar
    
    ### logger.info("access_token generated",extra={'txnid': access_token,'code':'success','client_id':client_id,'client_ip': request.remote_addr}) 

    
    
    
    
