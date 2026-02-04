import sys
import Assign_31_Q_4_automation_kit as kit

# Usage: DirectoryCopy.py "Demo" "Temp"
if __name__ == "__main__":
    if len(sys.argv) == 3:
        kit.copy_all_files(sys.argv[1], sys.argv[2])
    else:
        print("Invalid arguments. Check automation.log.")