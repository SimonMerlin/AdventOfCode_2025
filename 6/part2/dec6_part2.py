import os
import time
from functools import reduce
import operator

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseInput():
    #detect columns indexes
    columnsIndexes = set()
    for row in lines:
        if len(columnsIndexes) == 0:
            columnsIndexes = set(i for i in range(len(row)) if row[i] == ' ')
        else:
            columnsIndexes = columnsIndexes.intersection(set(i for i in range(len(row)) if row[i] == ' '))
        
    cuts = sorted(columnsIndexes)
    newLines = []
    
    # cut rows on column indexes
    for row in lines :
        start = 0
        newRow = []
        for i in cuts:
            newRow.append(row[start:i])
            start = i+1
        newRow.append(row[start:])
        newLines.append(newRow)

    return newLines

def solveProblem(problem):
    numbers = []
    maxLength = max([len(p) for p in problem[:-1]])
    for column in range(maxLength-1, -1, -1):
        n = ''
        for value in problem[:-1]:
            if column < len(value):
                n += value[column]
            else:
                n += '0'
        numbers.append(int(n))


    if problem[-1].strip() == '+':
        return sum([int(c) for c in numbers])
    else:
        return reduce(operator.mul, [int(c) for c in numbers], 1)
    
def main():
    problems = parseInput()
    nbProblems = len(problems[0])
    s = 0
    for i in range(nbProblems):
        problem = [p[i] for p in problems]
        s += solveProblem(problem)
    return s



if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
    f.close()