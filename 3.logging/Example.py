import logging

#  Basic logging settings

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
    handlers = [
        logging.FileHandler("example.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arithmeticapp")

def add(a,b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def sub(a,b):
    result = a - b
    logger.debug(f"subtraction of  {a} - {b} = {result}")
    return result

def mul(a,b):
    result = a * b
    logger.debug(f"multiplying {a} * {b} = {result}")
    return result

def div(a,b):
    try:
        result = a / b
        logger.debug(f"Division of {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.warning("Enter the denominator other than zero..")
        return None
    
add(10,10)
sub(10,10)
mul(10,10)
div(10,0)
