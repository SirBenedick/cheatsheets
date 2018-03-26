import hashlib, random, string, sys, time

def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def getHash(rawString):
    return hashlib.sha256(str(rawString).encode('utf-8')).hexdigest()

startValue = "asdfgh" #randomword(10)
print(startValue.center(40,"-"))
startHash = getHash(startValue)
print(startHash)
print("-"*40)

start_time = time.time()
b = 1
i = 0
while True:
    ranWord = randomword(6)
    ranHash = getHash(ranWord)
    seconds = "%s" % (time.time() - start_time)
    #hashRate
    if ranHash[0:b] == startHash[0:b]:
        sys.stdout.write("\033[F")
        print("\n",i,". \t",ranWord,": \t",ranHash, "\t s=",seconds)
        b += 1
    else:
        sys.stdout.write("\r{0}>".format(i))
        sys.stdout.flush()
    i += 1
