import os
import sys
import re

def replace_content_with_dereference(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regular expression to find occurrences of `some_name->content` within specific boundaries
    pattern = r'(?<=\W)(\w+->content)(?=\W)'
    matches = re.findall(pattern, content)

    # Replace each occurrence with `*(int *)(some_name->content)`
    for match in matches:
        replacement = f'*(int *)({match})'
        content = content.replace(match, replacement)

    with open(file_path, 'w') as file:
        file.write(content)

# Replace content in a specific file (replace 'your_file.c' with your actual file name)
replace_content_with_dereference(sys.argv[1])

