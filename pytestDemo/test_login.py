import logging

def test_loggingDemo():
    logger= logging.getLogger(__name__)

    fileHandler= logging.FileHandler('logfile.log.')
    formatter= logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #file handler object
    logger.setLevel(logging.CRITICAL)

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happened")
    logger.critical("Critical Issue")