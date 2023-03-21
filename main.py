"""write a python script that adds all the numbers entered in the command line as arguments. Throw an error if user enters something other than number"""

import sys

sum = 0

for arg in sys.argv[1:]:
    try:
        sum += int(arg)
    except ValueError:
        print("Error: invalid input, please enter a number")
        sys.exit(1)

print("The sum of the numbers is:", sum)

# """Logging exercise with logging.conf"""

# import logging
# import logging.config

# logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)

# # Get the logger specified in the file
# logger = logging.getLogger("sLogger")

# logger.debug('This is a debug message')
