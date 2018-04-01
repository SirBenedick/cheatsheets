maxSteps = 0
maxNum = 0
import timeit
import time

def collatzFuncBene(startingNumber):
    collatz = startingNumber
    count = 0
    while collatz != 1:
        if collatz%2 == 1:
            collatz = 3*collatz+1
        else:
            collatz = collatz/2
        count += 1
        print(count , ". " , collatz)
    global maxSteps
    global maxNum
    if maxSteps < count:
        maxSteps = count
        maxNum = startingNumber

    print("Zahl: ", startingNumber, "Schritte: ", count)

print("Collatz-Problem")
limit = int(input("Bitte gib eine Zahl ein: "))
tBene = time.process_time()
print(startingNumber)
##start = timeit.timeit()*1000
#collatzFunc(startingNumber)
for x in range(1,limit+1):
    collatzFuncBene(x)
print("Meisten Schritte: ", maxSteps, " bei der Zahl: ", maxNum)
##end = timeit.timeit()*1000
##print (end - start)
elapsed_timeBene = time.process_time() - tBene
print(elapsed_timeBene,"s")
#------------------------
print("Chris.:")
##startChris = timeit.timeit()*1000


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


#print("Collatz-Problem")
#limit = int(input("Bitte gib eine Zahl ein: "))
#print(startingNumber)
##startChris = timeit.timeit()*1000
#collatzFunc(startingNumber)
tChris = time.process_time()
for x in range(1,limit+1):
#    count = 0
    collatzFunc(x)
#print("Meisten Schritte: ", maxSteps, " bei der Zahl: ", maxNum)
elapsed_timeChris = time.process_time() - tChris
print(elapsed_timeChris,"s")
##endChris = timeit.timeit()*1000
##print (endChris - startChris)
diff = elapsed_timeChris/elapsed_timeBene
print(diff)
