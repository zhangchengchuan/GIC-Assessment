import logging

def getLogger():
    logging.basicConfig(filename='logs.txt', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()

    return None