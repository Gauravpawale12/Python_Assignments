import os
import logging

# Rule: Display messages in log file instead of console
logging.basicConfig(
    filename='automation.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s'
)

def search_files_by_extension(dir_name, extension):
    """
    Function to search and log files with a specific extension.
    Rule: For separate task define separate function.
    """
    # Rule: Perform validations before taking any action
    if not os.path.exists(dir_name):
        logging.error(f"Validation Failed: Directory '{dir_name}' does not exist.")
        return

    if not os.path.isdir(dir_name):
        logging.error(f"Validation Failed: '{dir_name}' is not a directory.")
        return

    # Rule: Handle every expected exception
    try:
        logging.info(f"Starting search in '{dir_name}' for extension '{extension}'")
        
        found_files = [f for f in os.listdir(dir_name) if f.endswith(extension)]
        
        if found_files:
            for file in found_files:
                logging.info(f"File Found: {file}")
        else:
            logging.info(f"No files with extension '{extension}' found.")
            
    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")