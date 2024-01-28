# random_list_generator.py

import sys
import random

def generate_random_list(length, size):
    if length > size + 1:
        raise ValueError("Length cannot be greater than size + 1 when requiring unique elements.")
    random_list = random.sample(range(size + 1), length)
    return random_list

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python random_list_generator.py <length> <size>")
        sys.exit(1)

    try:
        length = int(sys.argv[1])
        size = int(sys.argv[2])
    except ValueError:
        print("Error: Both length and size must be integers.")
        sys.exit(1)

    try:
        random_list = generate_random_list(length, size)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print(" ".join(str(num) for num in random_list))
