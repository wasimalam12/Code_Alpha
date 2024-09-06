import os
import shutil

def organize_files_by_extension(directory):
    # Check if the given directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Extract file extension
        file_extension = os.path.splitext(filename)[1][1:]  # Get extension without the dot

        # If there is no extension, move file to 'No Extension' folder
        if not file_extension:
            file_extension = "No Extension"

        # Create a subdirectory for the file extension if it doesn't exist
        extension_dir = os.path.join(directory, file_extension)
        if not os.path.exists(extension_dir):
            os.makedirs(extension_dir)

        # Move the file to the appropriate subdirectory
        shutil.move(file_path, os.path.join(extension_dir, filename))
        print(f"Moved: {filename} to {extension_dir}")

if __name__ == "__main__":
    # Specify the directory to organize
    target_directory = input("Enter the directory to organize: ")
    organize_files_by_extension(target_directory)
