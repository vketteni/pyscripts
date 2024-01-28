import os

def print_directory_tree(path, indent=''):
    print(f"{indent}+ {os.path.basename(path)}/")
    indent += '  '

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print_directory_tree(item_path, indent)
        else:
            print(f"{indent}- {item}")

# Example usage:
directory_path = input("Enter the directory path: ")
print_directory_tree(directory_path)
import os

def print_directory_tree(path, indent=''):
    print(f"{indent}+ {os.path.basename(path)}/")
    indent += '  '

    for item in os.listdir(path):
        if not item.startswith('.'):  # Exclude hidden files and directories
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print_directory_tree(item_path, indent)
            else:
                print(f"{indent}- {item}")

# Example usage:
directory_path = input("Enter the directory path: ")
print_directory_tree(directory_path)
import os

def print_directory_tree(directory_path, indent=""):
    # List all files and directories in the given path
    files_and_directories = os.listdir(directory_path)

    for item in files_and_directories:
        # Exclude hidden files and directories (those starting with a dot)
        if not item.startswith('.'):
            # Construct the full path of the current item
            item_path = os.path.join(directory_path, item)

            # Check if the current item is a directory
            if os.path.isdir(item_path):
                print(indent + "└── " + item)
                # Recursively print the subdirectory tree
                print_directory_tree(item_path, indent + "    ")
            else:
                print(indent + "└── " + item)

# Get the directory path as a command-line argument
directory_path = input("Enter the directory path: ")

# Check if the provided path is a valid directory
if os.path.isdir(directory_path):
    print_directory_tree(directory_path)
else:
    print("Invalid directory path.")

