def readData(file):
    with open(file, 'r') as f:
        text = [list(line.strip()) for line in f.readlines()]
    return text

def countXMas(data, word):
    wordLength = len(word)
    rows = len(data)
    cols = len(data[0])

    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
        (-1, -1)  # Up-Left
    ]
    def checkDirections(r, c, dr, dc):
        for i in range(wordLength):
            nr, nc = r + dr * i,c + dc * i
            if not (0 <= nr < rows and 0 <= nc < cols) or data[nr][nc] != word[i]:
                return False
        return True
    
    counter = 0


    for r in range(rows):
        for c in range(cols):
            if data[r][c] == word[0]:
                for dr, dc in directions:
                    if checkDirections(r, c, dr, dc):
                        counter += 1

    return counter

def searchXMASPattern(data):
    rows = len(data)
    cols = len(data[0])
    counter = 0

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if data[r][c] == 'A':
                if data[r - 1][c - 1] == 'M' and data[r - 1][c + 1] == 'M': #Top left and right are M
                    if data[r + 1][c - 1] == 'S' and data[r + 1][c + 1] == 'S':
                        counter += 1
                if data[r - 1][c - 1] == 'M' and data[r + 1][c - 1] == 'M': #Top and bottom left are M
                    if data[r - 1][c + 1] == 'S' and data[r + 1][c + 1] == 'S':
                        counter += 1
                if data[r + 1][c + 1] == 'M' and data[r - 1][c + 1] == 'M': #Top and bottom right are M
                    if data[r - 1][c - 1] == 'S' and data[r + 1][c - 1] == 'S':
                        counter += 1
                if data[r + 1][c - 1] == 'M' and data[r + 1][c + 1] == 'M': #Bottom left and right are M
                    if data[r - 1][c - 1] == 'S' and data[r - 1][c + 1] == 'S':
                        counter += 1

    return counter

word = 'XMAS'
input = readData('input.txt')
print(countXMas(input, word))
print(searchXMASPattern(input))
                