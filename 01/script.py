print("advent-of-code day 1")
"""
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
"""
example = (7, [199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
ex2 = (10, [9293, 9299, 9300, 9317, 9320, 9324, 9348, 9351, 9356, 9372, 9380])
ex3 = (8, [173, 179, 200, 210, 226, 229, 220, 221, 228, 233])

def howManyIncreases(data) :
    result = 0
    for ii in range (1, len(data)) :
        if (data[ii] > data[ii-1]) :
            result += 1
    return result


print(howManyIncreases(ex3[1]))

puzzleData = [] 
with open("01/puzzle.txt",'r') as input:
    puzzleData = [int(n) for n in input]


print(howManyIncreases(puzzleData))

