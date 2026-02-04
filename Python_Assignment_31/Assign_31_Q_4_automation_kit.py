import os
import shutil
import logging
import sys

# Rule: Display any message in log file instead of console
logging.basicConfig(
    filename='automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate_path(path):
    """Rule: Perform validations before taking any action"""
    if not os.path.exists(path):
        logging.error(f"Validation Error: Path '{path}' does not exist.")
        return False
    return True

def search_by_extension(dir_name, ext):
    """Task 1: Display all files with specific extension"""
    if not validate_path(dir_name): return
    try:
        logging.info(f"Searching for {ext} files in {dir_name}...")
        files = [f for f in os.listdir(dir_name) if f.endswith(ext)]
        for f in files:
            logging.info(f"Found: {f}")
    except Exception as e:
        logging.error(f"Error in search: {e}")

def copy_all_files(src, dest, ext=None):
    """Task 3 & 4: Copy files to a new directory"""
    if not validate_path(src): return
    try:
        # Rule: Second directory should be created at run time
        if not os.path.exists(dest):
            os.makedirs(dest)
            logging.info(f"Created directory: {dest}")
        
        for file_name in os.listdir(src):
            if ext is None or file_name.endswith(ext):
                shutil.copy2(os.path.join(src, file_name), os.path.join(dest, file_name))
                logging.info(f"Copied: {file_name}")
    except Exception as e:
        logging.error(f"Error in copy: {e}")