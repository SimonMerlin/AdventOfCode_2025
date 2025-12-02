import os
import time
import re

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

REGEX = r'^(.+)\1$'

def parseInput():
    return [(int(a), int(b)) for a,b in (l.split('-') for l in lines[0].split(','))]

def sumInvalidIdInRange(mMin, mMax):
    return sum([v for v in range(mMin, mMax + 1) if re.search(REGEX, str(v)) is not None])

def main():
    return sum([sumInvalidIdInRange(r[0], r[1]) for r in parseInput()])

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
    f.close()