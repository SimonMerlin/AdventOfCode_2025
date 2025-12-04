import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def getMaxJoltageForBank(bank):
    i, j = int(bank[0]), int(bank[1])
    for index in range(2, len(bank)):
        v = int(bank[index])
        if v > j and (v <= i or index == len(bank)-1):
            j = v
        elif v > i and index < len(bank)-1:
            if j > v:
                i, j = j, v
            else:
                i = v
                index += 1
                j = int(bank[index])
    return int(str(i)+str(j))

def main():
    return sum([getMaxJoltageForBank(bank) for bank in lines])

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
    f.close()