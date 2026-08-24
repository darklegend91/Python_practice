import sys , time
from loguru import logger


# logger.remove(0)
# logger.add(sys.stderr , level = 5) # Double print

# logger.add(sys.stderr,
#     format = "{time} | {level} | {message} | {extra} "
#     )
# logger.add(sys.stderr , format = "this is {message}")

# #By default it shows all messages from dedug (10) to above
# logger.trace("This is a tarce message") # 5
# logger.debug("This is a debug message") # 10
# logger.info("This is a info message")   #20
# logger.success("This is a success message")   #25
# logger.warning("This is a warning message") #30
# logger.error("This is a error message") # 40
# logger.critical("This is a critical message") # 50
# logger.critical("This is a critical message" , user_id = 1234567) # Pass a extra parameter in the logger

# logger.info("This is info message")

# logger.add(
#     sys.stderr,
#     format=(
#         "[<red>{time:HH:mm:ss}</red>] >> "
#         "<yellow>{level}</yellow>: "
#         "<cyan>{message}</cyan>"
#     )
# )
# logger.info("Database connection established")


# user_logger = logger.bind(user_id = 1234567890)
# user_logger.info("User Logged in")


# with logger.contextualize(request_id = '#2345GH'):
#     logger.info("User Request processing")
#     logger.info("Request Completed")

# logger.info("All requests Processed")

# with user_logger.contextualize(request_id = '#2345GH'):
#     user_logger.info("User Request processing")
#     user_logger.info("Request Completed")

# user_logger.info("All requests Processed")

# ======================== Logging File ========================
#Rotation and Retention

logger.add("app.log" , rotation='4 KB' , retention= "1 minute")

for i in range(100):
    logger.info(f"Processing item #{i}")
    time.sleep(2)
logger.info("This is a info message and goes to app.log")