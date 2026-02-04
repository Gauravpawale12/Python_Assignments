import sys
import Assign_31_Q_3_Automation_logic as al

def main():
    # Accept input through command line
    if len(sys.argv) != 3:
        print("Usage: DirectoryFileSearch.py <Directory> <Extension>")
        return

    dir_name = sys.argv[1]
    ext = sys.argv[2]
    al.find_files_by_ext(dir_name, ext)

if __name__ == "__main__":
    main()