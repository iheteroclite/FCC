# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger


#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

print(arithmetic_arranger(['1 + 2', '1 - 9380', '1567 +888', '687- 8'], True))

# Run unit tests automatically
main(['-vv'])
