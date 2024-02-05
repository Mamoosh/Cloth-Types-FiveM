import os

# Function to ensure the number is three digits
def format_number(number):
    return f"{int(number):03d}"

# Function to check for files and delete them
def delete_files(directory, output):
    found_files = []
    for filename in os.listdir(directory):
        if output in filename:
            file_to_delete = os.path.join(directory, filename)
            try:
                os.remove(file_to_delete)  # Deleting the file
                found_files.append(filename)
            except OSError as e:
                print(f"Error: {e.filename} - {e.strerror}.")
    return found_files

# Main function to read the file and delete corresponding files
def main(file_path, directory):
    with open(file_path, 'r') as file:
        for line in file:
            number_str = line.strip()
            if number_str.isdigit():  # Ensure the line is a number
                three_digit_number = format_number(number_str)
                cloth_type = "lowr"
                # Generate Output 1 and Output 2
                output1 = cloth_type + "_" + three_digit_number
                output2 = cloth_type + "_diff_" + three_digit_number

                # Find and delete matching files
                deleted_files1 = delete_files(directory, output1)
                deleted_files2 = delete_files(directory, output2)

                # Print out deleted files for both outputs
                if deleted_files1:
                    print(f"Deleted files matching '{output1}': {deleted_files1}")
                else:
                    print(f"No files found to delete for '{output1}'")

                if deleted_files2:
                    print(f"Deleted files matching '{output2}': {deleted_files2}")
                else:
                    print(f"No files found to delete for '{output2}'")

if __name__ == "__main__":
    file_path = 'C:\\Users\\YOURPCNAME\\Desktop\\format.txt'
    directory_path = ''
    main(file_path, directory_path)
