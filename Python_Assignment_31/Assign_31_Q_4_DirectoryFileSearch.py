import sys
import Assign_31_Q_4_automation_kit as kit

# Usage: DirectoryFileSearch.py "Demo" ".txt"
if __name__ == "__main__":
    if len(sys.argv) == 3:
        kit.search_by_extension(sys.argv[1], sys.argv[2])
    else:
        print("Invalid arguments. Check automation.log.")