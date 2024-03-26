import os

def rename_and_save(folder_path):
    # Get the list of files in the specified folder
    files = os.listdir(folder_path)

    # Open a file to save the new filenames
    with open('zzzz.txt', 'w') as file:
        # Iterate through each file in the folder
        for filename in files:
            # Construct the new file name
            new_filename = f"video-{filename.lower().replace(' ', '-')}"

            # Rename the file
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

            # Write the new file name to the file
            file.write(new_filename + '\n')

if __name__ == "__main__":
    # Specify the path to the folder containing the files
    folder_path = 'D:\\posting-bot\\en\\results'

    # Call the function to rename files and save to a text file
    rename_and_save(folder_path)
