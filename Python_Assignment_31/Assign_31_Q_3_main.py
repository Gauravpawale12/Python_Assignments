import sys
import Assign_31_Q_3_Automation_logic as al

def main():
    # Accept input through command line
    if len(sys.argv) != 3:
        print("Usage: DirectoryCopy.py <Source_Dir> <Dest_Dir>")
        return

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    al.copy_directory_contents(src_dir, dest_dir)

if __name__ == "__main__":
    main()