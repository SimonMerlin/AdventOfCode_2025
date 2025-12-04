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

def countAceessibleRolls():
    xMax, yMax = len(lines[0]), len(lines)
    accessedRollsPositions = []
    for y in range(yMax):
        for x in range(xMax):
            if lines[y][x] == '@':
                coordsAround = generateCoordinatesAround(x, y, xMax, yMax)
                if countRollsInCoordinates(lines, coordsAround) < 4:
                    accessedRollsPositions.append((x, y))

    for (x, y) in accessedRollsPositions:
        lines[y] = lines[y][:x] + '.' + lines[y][x+1:]
    
    return len(accessedRollsPositions)

def main():
    totalAccessibleRolls = 0
    accessibleRolls = countAceessibleRolls()
    while accessibleRolls != 0:
        totalAccessibleRolls += accessibleRolls
        accessibleRolls = countAceessibleRolls()
    return totalAccessibleRolls

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
    f.close()