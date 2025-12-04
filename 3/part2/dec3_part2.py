import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def getAllMaxFromList(list, xMin, xMax):
    results = []
    searchValue = max([int(v) for v in list[xMin:xMax+1]])
    for i in range(xMin, xMax+1):
        v = int(list[i])
        if v == searchValue:
            results.append((v, i))
    return results

def getMaxJoltageForBank(bank):
    bankList = list(bank)
    maxJoltage = ''
    xMin = 0
    while len(maxJoltage) < 12:
        candidates = getAllMaxFromList(bankList, xMin, len(bankList)-(12-(len(maxJoltage))))
        maxJoltage += str(candidates[0][0])
        xMin = candidates[0][1]+1
    return int(maxJoltage)

def main():
    return sum([getMaxJoltageForBank(bank) for bank in lines])

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
    f.close()