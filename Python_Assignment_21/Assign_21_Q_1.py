# Design a python application that creates two Threads named Prime and NonPrime
# Both threads should accept a list of integers 
# The Prime thread should display all prime numbers from the list 
# The NonPrime thread should display all non-prime numbres from list.



import threading

def ChkPrime(iNo):
    if iNo < 2:
        return False

    for i in range(2, int(iNo / 2) + 1):
        if iNo % i == 0:
            return False

    return True


def Prime(numbers):
    print("Prime Thread Started")
    print("Prime numbers are : ", end=" ")
    for no in numbers:
        if ChkPrime(no):
            print(no, end=" ")
    print("\nPrime Thread Ended\n")


def NonPrime(numbers):
    print("NonPrime Thread Started")
    print("Non-Prime numbers are : ", end=" ")
    for no in numbers:
        if not ChkPrime(no):
            print(no, end=" ")
    print("\nNonPrime Thread Ended")


def main():
    data = [2, 3, 4, 5, 6, 7, 8, 9, 11, 15, 17, 20]

    t1 = threading.Thread(target=Prime, args=(data,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()
