# NOT easy, NOT fun, made me write horrible code

"""
For each number in bingo board, replace it with the index of that number in the called-out number array you get at the start. A lower index iimplies that number is called early and a higher implies it's called late.

For each bingo board, get it's columns and rows. For each of those, find the maximum number in that column/row. This is the winning turn for that column/row. Then, find the minimum number of the winning turns. This is the winning turn for the bingo.

Then, simply find the bingo that has the lowest winning turn. Find the numbers that were called-out until that turn and do the needful.
"""

def _part1_checkBingo(b):
    for board in b: # Check horizontally
        for row in board:
            if row == [False]*5:
                return board
    for board in b: # Check vertically
        for i in range(5):
            if board[0][i] == False and board[1][i] == False and board[2][i] == False and board[3][i] == False and board[4][i] == False:
                return board

def part1():
    data = [l.strip() for l in open("data.txt","r") if l != "\n"]
    calledNumbers = [int(x) for x in data.pop(0).split(",")]
    boards = [[data[(i*5)+j] for j in range(5)] for i in range(len(data)//5)]
    boards = [[row.split(" ") for row in board] for board in boards]
    boards = [[[int(i) for i in row if i] for row in board] for board in boards]

    for number in calledNumbers:
        for i,board in enumerate(boards):
            for j,row in enumerate(board):
                for v,n in enumerate(row):
                    if n == number:
                        boards[i][j][v] = False
        correctBoard = _part1_checkBingo(boards)
        if correctBoard:
            lastNumber = number
            break

    boardTotal = 0
    for row in correctBoard:
        boardTotal += sum(row)

    print("Part1:",boardTotal*lastNumber)

if __name__ == "__main__":
    part1()
    part2()