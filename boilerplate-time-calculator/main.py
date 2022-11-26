# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

inexT = "11:06 AM"
inexD = "25:02"
print ('input ', inexT, ' ', inexD)
print(add_time(inexT, inexD))


# Run unit tests automatically
main(module='test_module', exit=False)