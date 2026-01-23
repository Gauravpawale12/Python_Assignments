# Design python application where multiple threads update a shared variable 
# Use Lock to avoid race conditions 
# Each thread should avoid increment the shared counter multiple times
# Display the final value of the counter after all threads complete execution


import threading

counter = 0
lock = threading.Lock()

def Increment():
    global counter

    for i in range(5):
        lock.acquire()
        counter = counter + 1
        lock.release()


def main():
    t1 = threading.Thread(target=Increment, name="Thread1")
    t2 = threading.Thread(target=Increment, name="Thread2")
    t3 = threading.Thread(target=Increment, name="Thread3")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Final value of counter :", counter)
    print("Exit from main")


if __name__ == "__main__":
    main()
