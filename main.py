import os
import time
from datetime import datetime

def set_file_modification_date(file_path, modification_date):
    os.utime(file_path, times=(modification_date, modification_date))
    print(f"Modification date of '{file_path}' set successfully.")

def create_files():
    while True:
        try:
            # Get the number of files to create from the user
            num_files = int(input("Enter the number of files to create: "))
            if num_files > 0:
                break
            else:
                print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Get file extension from the user
    file_extension = input("Enter the file extension (e.g., txt, csv, etc.): ")

    # Get custom modification date from the user (optional)
    set_modification_date = input("Do you want to set a custom modification date for all the files? (y/n): ").lower() == 'y'

    # Set the custom modification date if requested by the user
    custom_date = None
    if set_modification_date:
        custom_date_str = input("Enter the custom modification date (YYYY-MM-DD HH:MM:SS): ")
        try:
            custom_date = datetime.strptime(custom_date_str, "%Y-%m-%d %H:%M:%S").timestamp()
        except ValueError:
            print("Invalid date format. Please enter the date in the format 'YYYY-MM-DD HH:MM:SS'.")

    # Create the specified number of files
    for i in range(1, num_files + 1):
        # Generate the file name
        file_name = str(i)

        # Combine file name and extension to create the full file name
        full_file_name = f"{file_name}.{file_extension}"

        # Check if the file already exists
        if os.path.exists(full_file_name):
            print(f"The file '{full_file_name}' already exists.")
        else:
            # Create the file
            with open(full_file_name, 'w') as file:
                print(f"File '{full_file_name}' created successfully.")

            # Set the custom modification date for all files if provided by the user
            if custom_date is not None:
                set_file_modification_date(full_file_name, custom_date)

# Call the function to create files
create_files()
