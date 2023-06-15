import os
cat = "cat"

def list_directory_contents(directory):
    # Get the contents of the directory
    contents = os.listdir(directory)

    # Iterate over the contents
    for item in contents:
        item_path = directory + '/' + item  # Construct the item path
        if item == "VERSION":
            print(os.system(cat + " " + item_path))
            break
        # Check if the item is a directory
        is_directory = False
        try:
            # In some MicroPython implementations, this may need to be adjusted
            is_directory = os.stat(item_path)[0] & 0x4000 == 0x4000
        except Exception as e:
            pass

        # If the item is a directory, recursively call the function
        if is_directory:
            list_directory_contents(item_path)

# Provide the starting directory here
starting_directory = '/ram/pckg'

# Call the function with the starting directory
list_directory_contents(starting_directory)
