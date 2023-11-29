import os
import shutil
import json

def add_refiner_prompt_to_payload(root_directory):
    for subdir in os.listdir(root_directory):
        subdir_path = os.path.join(root_directory, subdir)

        # Check if the subdirectory name contains 'refiner_scheduler'
        if os.path.isdir(subdir_path) and 'refiner_scheduler' in subdir:
            payload_path = os.path.join(subdir_path, 'payload.json')

            # Check if payload.json exists in the folder
            if os.path.isfile(payload_path):
                with open(payload_path, 'r+') as file:
                    # Read the existing JSON data
                    data = json.load(file)

                    # Add the 'refiner_prompt' line
                    data["refiner_prompt"] = "high resolution, 8k, decent, beautiful, high quality"

                    # Move the file pointer to the beginning of the file and truncate the file
                    file.seek(0)
                    file.truncate()

                    # Write the updated JSON data back to the file
                    json.dump(data, file, indent=2)
                    print(f"Updated payload.json in {subdir}")


def copy_and_rename_folders(root_directory):
    # Loop through all subdirectories in the root directory
    for subdir in os.listdir(root_directory):
        subdir_path = os.path.join(root_directory, subdir)

        # Check if it's a directory and contains 'base_scheduler' in its name
        if os.path.isdir(subdir_path) and 'base_scheduler' in subdir:
            # Construct new folder name
            new_subdir = subdir.replace('base_scheduler', 'refiner_scheduler')
            new_subdir_path = os.path.join(root_directory, new_subdir)

            # Copy the contents of the old directory to the new directory
            shutil.copytree(subdir_path, new_subdir_path)
            print(f"Copied and renamed {subdir} to {new_subdir}")

if __name__ == "__main__":
    # Current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_directory = os.path.join(current_dir, "test", "regression")
    # copy_and_rename_folders(root_directory)
    add_refiner_prompt_to_payload(root_directory)
