# Design a python application thaat creates two threads named EvenList and OddList
# Both threads should accept a list of integers as input
# The EvenList thread should:
    # Extract all even elements from the list 
    # Calculate and display their sum
# The OddList thread should:
    # Extract all odd elements from the list
    # Calculte and display their sum
# Thread should run concurrently



import threading

def EvenList(numbers):
    even_nums = [num for num in numbers if num % 2 == 0]
    print("Even elements :", even_nums)
    print("Sum of even elements :", sum(even_nums))


def OddList(numbers):
    odd_nums = [num for num in numbers if num % 2 != 0]
    print("Odd elements :", odd_nums)
    print("Sum of odd elements :", sum(odd_nums))


def main():
    data = [10, 15, 20, 23, 30, 45, 50, 55]

    t1 = threading.Thread(target=EvenList, args=(data,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(data,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
