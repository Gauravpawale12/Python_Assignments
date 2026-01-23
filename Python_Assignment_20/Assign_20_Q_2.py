# Design a python application that creates two seperate threads named EvenFactor and OddFactor
# Both threads should accept one integer number as parameter
# The EvenFactor thread should: 
    # Identify all even factors of the given number
    # Calculate and display the sum of even factors
# The OddFactor thread should:
    # Identify all the odd factors of the given number
    # Calculate and display the sum of odd factors
# After both threads complete execution, the main thread should display the message:
# "Exit from main"


import threading

# Thread function to calculate even factors
def EvenFactor(iNo):
    iSum = 0
    print("Even factors are:")
    for i in range(1, iNo + 1):
        if iNo % i == 0 and i % 2 == 0:
            print(i, end=" ")
            iSum = iSum + i
    print("\nSum of even factors:", iSum)


# Thread function to calculate odd factors
def OddFactor(iNo):
    iSum = 0
    print("Odd factors are:")
    for i in range(1, iNo + 1):
        if iNo % i == 0 and i % 2 != 0:
            print(i, end=" ")
            iSum = iSum + i
    print("\nSum of odd factors:", iSum)


def main():
    print("Enter the number:")
    iValue = int(input())

    t1 = threading.Thread(target=EvenFactor, args=(iValue,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(iValue,), name="OddFactor")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
