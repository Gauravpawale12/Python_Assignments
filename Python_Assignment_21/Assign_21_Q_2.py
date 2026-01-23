# Design a python application that creates two threads
# Thread1 should calculate and display the minimum element from a list 
# Thread2 should calculate and display the minimum element from same list 
# The list should be accepted from the user


import threading

def DisplayMin(data):
    min_no = data[0]
    for no in data:
        if no < min_no:
            min_no = no
    print(f"Minimum element is : {min_no}")
    print(f"Thread Name : {threading.current_thread().name}")
    print(f"Thread ID   : {threading.get_ident()}\n")


def main():
    arr = []
    print("Enter number of elements:")
    n = int(input())

    print("Enter the elements:")
    for i in range(n):
        arr.append(int(input()))

    t1 = threading.Thread(target=DisplayMin, args=(arr,), name="Thread1")
    t2 = threading.Thread(target=DisplayMin, args=(arr,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
