# Design python application that creates two threads
# Thread1 should compute the sum of elements from list 
# Thread2 should compute the product of elements from the same list 
# Return the result to main thread and display them.


import threading

SumResult = 0
ProdResult = 1

def SumList(data):
    global SumResult
    SumResult = 0
    for no in data:
        SumResult = SumResult + no


def ProductList(data):
    global ProdResult
    ProdResult = 1
    for no in data:
        ProdResult = ProdResult * no


def main():
    arr = []

    print("Enter number of elements:")
    n = int(input())

    print("Enter the elements:")
    for i in range(n):
        arr.append(int(input()))

    t1 = threading.Thread(target=SumList, args=(arr,), name="SumThread")
    t2 = threading.Thread(target=ProductList, args=(arr,), name="ProductThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements is :", SumResult)
    print("Product of elements is :", ProdResult)
    print("Exit from main")


if __name__ == "__main__":
    main()
