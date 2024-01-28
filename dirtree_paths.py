import os

def print_directory_tree(directory_path):
    for root, dirs, files in os.walk(directory_path):
        # Filter out hidden directories and files
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        files = [f for f in files if not f.startswith('.')]

        # Print the current directory
        print(root)

        # Print files in the current directory
        for file in files:
            print(os.path.join(root, file))

if __name__ == "__main__":
    # Input directory path
    directory_path = input("Enter the directory path: ")

    # Check if the directory exists
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        # Print the directory tree
        print_directory_tree(directory_path)
    else:
        print("Invalid directory path. Please provide a valid path.")

