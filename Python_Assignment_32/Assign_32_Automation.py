import os
import sys
import time
import hashlib
import logging

# -------------------------------------------------
# Logger Setup
# -------------------------------------------------
def setup_logger():
    logging.basicConfig(
        filename="Log.txt",
        level=logging.INFO,
        format="%(asctime)s : %(message)s"
    )

# -------------------------------------------------
# Validation
# -------------------------------------------------
def validate_directory(dir_name):
    if not os.path.exists(dir_name):
        raise FileNotFoundError("Directory does not exist")
    if not os.path.isdir(dir_name):
        raise NotADirectoryError("Provided path is not a directory")

# -------------------------------------------------
# Utility Functions
# -------------------------------------------------
def get_all_files(dir_name):
    file_list = []
    for folder, subfolder, files in os.walk(dir_name):
        for file in files:
            file_list.append(os.path.join(folder, file))
    return file_list

def calculate_checksum(file_path):
    hash_obj = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024), b''):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# -------------------------------------------------
# Task 1: Display checksum of all files
# -------------------------------------------------
def directory_checksum(dir_name):
    files = get_all_files(dir_name)
    for file in files:
        checksum = calculate_checksum(file)
        logging.info(f"{file} : {checksum}")

# -------------------------------------------------
# Task 2: Find duplicate files
# -------------------------------------------------
def find_duplicates(dir_name):
    files = get_all_files(dir_name)
    checksum_map = {}

    for file in files:
        checksum = calculate_checksum(file)
        checksum_map.setdefault(checksum, []).append(file)

    for file_list in checksum_map.values():
        if len(file_list) > 1:
            for file in file_list:
                logging.info(f"Duplicate File : {file}")

# -------------------------------------------------
# Task 3 & 4: Remove duplicate files
# -------------------------------------------------
def remove_duplicates(dir_name):
    files = get_all_files(dir_name)
    checksum_map = {}

    for file in files:
        checksum = calculate_checksum(file)
        checksum_map.setdefault(checksum, []).append(file)

    for file_list in checksum_map.values():
        if len(file_list) > 1:
            for file in file_list[1:]:
                os.remove(file)
                logging.info(f"Deleted Duplicate File : {file}")

# -------------------------------------------------
# Main Function
# -------------------------------------------------
def main():
    setup_logger()
    start_time = time.time()

    try:
        if len(sys.argv) != 3:
            raise ValueError(
                "Usage: python DirectoryAutomation.py <DirectoryName> <Mode>"
            )

        dir_name = sys.argv[1]
        mode = sys.argv[2].lower()

        validate_directory(dir_name)

        if mode == "checksum":
            directory_checksum(dir_name)

        elif mode == "duplicate":
            find_duplicates(dir_name)

        elif mode == "remove":
            remove_duplicates(dir_name)

        elif mode == "remove_with_time":
            remove_duplicates(dir_name)
            end_time = time.time()
            logging.info(f"Execution Time : {end_time - start_time} seconds")

        else:
            raise ValueError("Invalid mode selected")

    except Exception as e:
        logging.error(e)

# -------------------------------------------------
if __name__ == "__main__":
    main()


'''
python DirectoryAutomation.py Demo checksum

python DirectoryAutomation.py Demo duplicate


python DirectoryAutomation.py Demo remove
python DirectoryAutomation.py Demo remove_with_time


'''