import os

# Specify the directory path
directory_path = "/home/kane/repos"  # Replace with the actual directory path

# Use os.listdir() to get a list of files and directories
contents = os.listdir(directory_path)

# Print the contents
# print("Contents of", directory_path + ":")
for item in contents:
    print(item)

