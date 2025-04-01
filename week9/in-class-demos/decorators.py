# import logging

# Setup basic config for logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Our decorator
def logger(func):
    # *args any number of positional arguments as a tuple
    # **kwargs any number of keyword arguments as a dictionary
    def wrapper(*args, **kwargs):

        print('Args: ',args)
        print('Kwargs: ',kwargs)
        # logging.info(f"Running function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logger
def greet(name, key):
    print(f"Hi, {name}")

greet("Robbo", 'firstname')
greet(name="Robbo", key="firstname")