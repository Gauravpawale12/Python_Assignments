# Design a python application that creates three threads named Small, Capital and Digits
# All threads should accepts a string as input
# The Small thread should count and display the number of lowercase characters
# The Capital thread should count and display the number of uppercase characters
# The Digits thread should count and display the number of numeric digits
# Each thread must also display
    # ThreadID
    # Thread Name


import threading

def Small(text):
    count = sum(1 for ch in text if ch.islower())
    print("Thread Name :", threading.current_thread().name)
    print("Thread ID   :", threading.get_ident())
    print("Lowercase count :", count)
    print()


def Capital(text):
    count = sum(1 for ch in text if ch.isupper())
    print("Thread Name :", threading.current_thread().name)
    print("Thread ID   :", threading.get_ident())
    print("Uppercase count :", count)
    print()


def Digits(text):
    count = sum(1 for ch in text if ch.isdigit())
    print("Thread Name :", threading.current_thread().name)
    print("Thread ID   :", threading.get_ident())
    print("Digit count :", count)
    print()


def main():
    data = "Marvellous123Python"

    t1 = threading.Thread(target=Small, args=(data,), name="Small")
    t2 = threading.Thread(target=Capital, args=(data,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(data,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
