import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import logging

# ---------------- GLOBAL SETTINGS ----------------
LOG_DIR = "Logs"
HISTORY_FILE = "BackupHistory.txt"
EXCLUDE_EXTENSIONS = [".tmp", ".log", ".exe"]
BACKUP_FOLDER = "MarvellousBackup"
# ------------------------------------------------


def CreateLogger():
    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = os.path.join(
        LOG_DIR, f"Backup_{time.strftime('%Y%m%d_%H%M%S')}.log")

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s : %(levelname)s : %(message)s"
    )
    return log_file


def calculate_hash(path):
    try:
        hobj = hashlib.md5()
        with open(path, "rb") as fobj:
            while True:
                data = fobj.read(1024)
                if not data:
                    break
                hobj.update(data)
        return hobj.hexdigest()
    except Exception as e:
        logging.error(f"Hash error : {e}")
        return None


def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zobj:
        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root, file)
                relative = os.path.relpath(full_path, folder)
                zobj.write(full_path, relative)

    logging.info(f"Zip created : {zip_name}")
    return zip_name


def BackupFiles(Source, Destination):
    copied_files = []
    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:

            if any(file.endswith(ext) for ext in EXCLUDE_EXTENSIONS):
                continue

            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            if (not os.path.exists(dest_path)) or \
               (calculate_hash(src_path) != calculate_hash(dest_path)):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)
                logging.info(f"Copied : {relative}")

    return copied_files


def StoreHistory(file_count, zip_name):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{time.ctime()} | Files : {file_count} | "
                f"Size : {os.path.getsize(zip_name)} bytes\n")


def RestoreBackup(zip_name, destination):
    if not os.path.exists(zip_name):
        return

    os.makedirs(destination, exist_ok=True)

    with zipfile.ZipFile(zip_name, 'r') as zobj:
        zobj.extractall(destination)


def MarvellousDataShieldStart(Source="Data"):
    CreateLogger()
    logging.info("Backup process started")

    files = BackupFiles(Source, BACKUP_FOLDER)
    zip_file = make_zip(BACKUP_FOLDER)

    StoreHistory(len(files), zip_file)

    logging.info("Backup completed successfully")
    logging.info(f"Files copied : {len(files)}")
    logging.info(f"Zip file name : {zip_file}")



def main():

    Border = "-"*50
    print(Border)
    print("--------- Marvellous Data Shield System ----------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This scipt is used to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        schedule.every(int(sys.argv[1])).minute.do(
            MarvellousDataShieldStart, sys.argv[2])

        print(Border)
        print("Data Sheild System started succesfully")
        print("Time interval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details") 

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)
# ====================================================================

if __name__ == "__main__":
    main()
