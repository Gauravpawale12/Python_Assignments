# Design a python application that creates two seperate threads named Even and Odd
# The even thread should display the first 10 even numbers
# The odd thread should display the first 10 odd numbers
# Both threads should execute independently using the threading module
# Ensure proper thread creation and execution


import threading

# Thread function to display even numbers
def DisplayEven():
    print("Even thread started")
    for i in range(1, 11):
        print("Even:", i * 2)
    print("Even thread finished")


# Thread function to display odd numbers
def DisplayOdd():
    print("Odd thread started")
    for i in range(10):
        print("Odd:", (2 * i) + 1)
    print("Odd thread finished")


def main():
    t1 = threading.Thread(target=DisplayEven, name="Even")
    t2 = threading.Thread(target=DisplayOdd, name="Odd")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Main thread finished")


if __name__ == "__main__":
    main()
