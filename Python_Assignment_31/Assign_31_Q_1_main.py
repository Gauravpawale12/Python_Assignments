import sys
import Assign_31_Q_1_module  # Rule: Using user defined module

def main():
    # Rule: Accept input through command line
    if len(sys.argv) != 3:
        print("Usage: DirectoryFileSearch.py <Directory_Name> <Extension>")
        return

    directory = sys.argv[1]
    ext = sys.argv[2]

    # Trigger the functionality from the module
    Assign_31_Q_1_module.search_files_by_extension(directory, ext)
    print(f"Process complete. Please check 'automation.log' for results.")

if __name__ == "__main__":
    main()