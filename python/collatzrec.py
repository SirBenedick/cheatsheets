#maxSteps = 0
#maxNum = 0
#count = 0
import timeit

startChris = timeit.timeit()*1000


def collatzFunc(collatz):
    #global count
    if(collatz != 1):
        #collatz = startingNumber

        if collatz%2 == 1:
            collatz = 3*collatz+1
        else:
            collatz = collatz/2
        #count += 1
        #print(count , ". " , collatz)

        collatzFunc(collatz)

    #else:
        #global maxSteps
        #global maxNum
        #if maxSteps < count:
    #        maxSteps = count
    #        maxNum = startingNumber
    #    print("Zahl: ", startingNumber, "Schritte: ", count)


print("Collatz-Problem")
limit = int(input("Bitte gib eine Zahl ein: "))
#print(startingNumber)

#collatzFunc(startingNumber)
for x in range(1,limit+1):
#    count = 0
    collatzFunc(x)
#print("Meisten Schritte: ", maxSteps, " bei der Zahl: ", maxNum)

endChris = timeit.timeit()*1000
print (endChris - startChris)
