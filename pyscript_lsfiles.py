import os
import sys

def list_c_files(directory_path):
    try:
        # Get the list of files in the specified directory
        files = os.listdir(directory_path)
        
        # Filter files with '.c' extension
        c_files = [file for file in files if file.endswith('.c')]
        
        # Print the filenames on separate lines
        for c_file in c_files:
            print(c_file)
    
    except FileNotFoundError:
        print(f"Error: Directory not found - {directory_path}")
    except PermissionError:
        print(f"Error: Permission denied for directory - {directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the directory path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        list_c_files(directory_path)
