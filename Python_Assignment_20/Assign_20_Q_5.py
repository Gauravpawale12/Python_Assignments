# Design a python application that creates two threads Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50
# Thread2 should display numbers from 50 to 1 in reverse order
# Ensure that 
    # Thread2 starts execution only after Thread has completed
# use appropriate thread synchronization



import threading

def DisplayForward():
    print("Thread1 started")
    for i in range(1, 51):
        print(i, end=" ")
    print("\nThread1 completed\n")


def DisplayReverse():
    print("Thread2 started")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print("\nThread2 completed")


def main():
    t1 = threading.Thread(target=DisplayForward, name="Thread1")
    t2 = threading.Thread(target=DisplayReverse, name="Thread2")

    t1.start()
    t1.join()      # Thread2 waits until Thread1 completes

    t2.start()
    t2.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()
