import os
import shutil
import logging

# Configure logging to file instead of console
logging.basicConfig(
    filename='automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate_dir(path):
    """Checks if a directory exists and is a directory."""
    if not os.path.exists(path):
        logging.error(f"Validation failed: {path} does not exist.")
        return False
    if not os.path.isdir(path):
        logging.error(f"Validation failed: {path} is not a directory.")
        return False
    return True

def find_files_by_ext(directory, extension):
    """Logic for Task 1: Search files by extension."""
    if not validate_dir(directory):
        return
    
    try:
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        if files:
            logging.info(f"Files found in {directory} with {extension}: {', '.join(files)}")
        else:
            logging.info(f"No files found with extension {extension} in {directory}.")
    except Exception as e:
        logging.error(f"Error during file search: {e}")

def copy_directory_contents(src, dest):
    """Logic for Task 3: Copy all files to a new directory."""
    if not validate_dir(src):
        return

    try:
        # Create destination directory at run time if it doesn't exist
        if not os.path.exists(dest):
            os.makedirs(dest)
            logging.info(f"Created new directory: {dest}")
        
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dest, item)
            if os.path.isfile(s):
                shutil.copy2(s, d)
        
        logging.info(f"Successfully copied all files from {src} to {dest}")
    except Exception as e:
        logging.error(f"Error during directory copy: {e}")