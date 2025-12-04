import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def generateCoordinatesAround(x, y, xMax, yMax):
    coords = [(x-1, y-1), (x, y-1), (x+1, y-1),
              (x-1, y),             (x+1, y),
              (x-1, y+1), (x, y+1), (x+1, y+1)]
    return [(x, y) for (x, y) in coords if 0 <= x < xMax and 0 <= y < yMax]

def countRollsInCoordinates(grid, coords):
    return len([1 for (x, y) in coords if grid[y][x] == '@'])

def main():
    xMax, yMax = len(lines[0]), len(lines)
    accessibleRolls = 0
    for y in range(yMax):
        for x in range(xMax):
            if lines[y][x] == '@':
                coordsAround = generateCoordinatesAround(x, y, xMax, yMax)
                if countRollsInCoordinates(lines, coordsAround) < 4:
                    accessibleRolls += 1
    return accessibleRolls

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
    f.close()