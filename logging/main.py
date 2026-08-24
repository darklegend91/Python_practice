import logging
import os
os.makedirs('logging', exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    filename='logging/app.log',
    encoding='utf-8',
    filemode='a',
    format="{levelname} - {name} - {message}-{asctime}",
    style="{",
    datefmt='%Y-%m-%d %H:%M:%S'
)
user_name = 'Samara'
logging.debug("This is a debug log")
logging.info("Application Started")
logging.warning("Check the CPU Usage")
logging.error("Printer Not compatible")
logging.critical("Database crashed due to high load")
logging.debug(f"The user name is {user_name}")
# donuts = 5
# guests = 0

# try:
#     donuts_per_guest = donuts/guests
    
# except ZeroDivisionError as err:
#     #only logs error as {  2026-08-20 09:53:44 - ERROR - root - division by zero made by Samara }
#     # logging.error(f"{err} made by {user_name}")
#     """
#         Logs full stack of error as { Traceback (most recent call last):
#         File "/Users/adityapathania/Codes/bz/Python_practice/logging/main.py", line 26, in <module>
#             donuts_per_guest = donuts/guests
#                             ~~~~~~^~~~~~~
#         ZeroDivisionError: division by zero }
#     """
#     # logging.exception(f"{err} made by {user_name}")
#     ## as same as 
#     #  logging.error(exc_info = True , msg =f"{err} made by {user_name}")
    
    
#     # =================Creating a Custom Logger=================
#     # While you could use any string as the name, it’s good practice to pass __name__ as the name parameter. That way, your logger’s name is always the module’s name in the Python package namespace.
    
#     logging.basicConfig(level=0)
#     logger = logging.getLogger(__name__)
#     # logger.warning("Look at my logger")
#     conosle_handler = logging.StreamHandler()
#     logger.addHandler(conosle_handler)
#     # logger.addHandler(file_handler)
#     logger.handlers
#     file_handler = logging.FileHandler(
#         "app.log",
#         mode = 'a',
#         encoding = 'utf-8'
#         )
#     print(logger.getEffectiveLevel())


# import logging
# import sys

# def get_custom_logger(name: str) -> logging.Logger:
#     """Create and return a fully configured custom logger."""
    
#     # 1. Get the logger instance
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.DEBUG)  # Capture everything

#     # 2. Create formatters
#     detailed_format = logging.Formatter(
#         '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#     )
#     simple_format = logging.Formatter(
#         '%(levelname)s: %(message)s'
#     )

#     # 3. Create Console Handler (Stream)
#     console_handler = logging.StreamHandler(sys.stdout)
#     console_handler.setLevel(logging.INFO)
#     console_handler.setFormatter(simple_format)

#     # 4. Create File Handler
#     file_handler = logging.FileHandler('app.log')
#     file_handler.setLevel(logging.DEBUG)
#     file_handler.setFormatter(detailed_format)

#     # 5. Add handlers to the logger
#     # (Avoid duplicate logs if this function is called multiple times)
#     if not logger.handlers:
#         logger.addHandler(console_handler)
#         logger.addHandler(file_handler)

#     return logger

# # Usage in your app
# app_logger = get_custom_logger("my_awesome_app")
# app_logger.debug("This goes ONLY to the file (with timestamp)")
# app_logger.info("This goes to console and file")