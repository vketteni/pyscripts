import sys

# Collect arguments, excluding the script name
numbers = sys.argv[1:]

# Map the numbers to strings enclosed in double quotes
quoted_numbers = [f'"{number}"' for number in numbers]

# Join the quoted numbers with a comma
result = ",".join(quoted_numbers)

print(result)
