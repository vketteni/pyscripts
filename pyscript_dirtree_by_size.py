import os
import sys

def get_size(path):
    """Get the size of a file or directory."""
    if os.path.isfile(path):
        return os.path.getsize(path)
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def format_size(size):
    """Format the size to a readable format."""
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} TB"

def print_dir_tree(startpath, limit=100):
    """Print the directory tree sorted by size, limited to the first 'limit' entries."""
    dir_tree = {}
    for root, dirs, files in os.walk(startpath):
        for name in files + dirs:
            full_path = os.path.join(root, name)
            size = get_size(full_path)
            dir_tree[full_path] = size

    # Sorting the dictionary by size
    sorted_tree = dict(sorted(dir_tree.items(), key=lambda item: item[1], reverse=True))

    # Print only the first 'limit' entries
    for i, (path, size) in enumerate(sorted_tree.items()):
        if i >= limit:
            break
        formatted_size = format_size(size)
        print(f"{path} - {formatted_size}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py [directory_path]")
        sys.exit(1)

    directory_path = sys.argv[1]
    print_dir_tree(directory_path)
