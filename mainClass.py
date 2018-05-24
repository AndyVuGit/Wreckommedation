def main():
    # This is the first of the program
    # Simple outline featuring two list of random alphabet to simulate two people and their song selections
    firstuser = [1, 2, 3, 4]

    seconduser = [4, 6, 7, 8]

    firstcheck = seconduser[:]
    secondcheck = firstuser[:]

    # Checking if any value of the first list is in the compared list
    for i in range(0, len(firstuser)):
        item = firstuser[i]
        if item in firstcheck:
            firstcheck.remove(item)

    for i in range(0, len(seconduser)):
        item = seconduser[i]
        if item in secondcheck:
            secondcheck.remove(item)

    print ("first user recommended no. = ", firstcheck)
    print ("second user recommended no. = ", secondcheck)

main()