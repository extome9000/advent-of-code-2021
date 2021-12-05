# Easier than day 3. Part 1 by myself, part 2 with some help.

def part1():
	data = [l.split() for l in open("data.txt","r")]
	data = [[tuple(v[0].split(",")),tuple(v[2].split(","))] for v in data]

	width, height = 1000,1000
	dataMap = [[0 for x in range(width)] for y in range(height)]

	for numSet in data:
		c1,c2 = numSet[0], numSet[1]
		x1,y1,x2,y2 = int(c1[0]),int(c1[1]),int(c2[0]),int(c2[1])
		if x1 == x2: # X == X
			diff = abs(y2-y1)
			start = min(y1,y2)
			for i in range(diff+1):
				dataMap[x1][start+i] += 1
		elif y1 == y2: # Y == Y
			diff = abs(x2-x1)
			start = min(x1,x2)
			for i in range(diff+1):
				dataMap[start+i][y1] += 1

	intersections = 0
	for x in dataMap:
		for y in x:
			if y >= 2:
				intersections += 1
	
	print("Part1",intersections)

def part2():
	data = [l.split() for l in open("data.txt","r")]
	data = [[tuple(v[0].split(",")),tuple(v[2].split(","))] for v in data]

	width, height = 1000,1000
	dataMap = [[0 for x in range(width)] for y in range(height)]

	for numSet in data:
		c1,c2 = numSet[0], numSet[1]
		x1,y1,x2,y2 = int(c1[0]),int(c1[1]),int(c2[0]),int(c2[1])
		if x1 == x2: # X == X
			diff = abs(y2-y1)
			start = min(y1,y2)
			for i in range(diff+1):
				dataMap[x1][start+i] += 1
		elif y1 == y2: # Y == Y
			diff = abs(x2-x1)
			start = min(x1,x2)
			for i in range(diff+1):
				dataMap[start+i][y1] += 1
		else:
			diff = abs(x2-x1)
			start_x = min(x1,x2)
			if start_x == x1:
				start_y = y1
			else:
				start_y = y2
			if start_y == max(y1,y2):
				up = -1
			else:
				up = 1
			for i in range(diff+1):
				dataMap[start_x+i][start_y+i*up] += 1

	intersections = 0
	for x in dataMap:
		for y in x:
			if y >= 2:
				intersections += 1
	
	print("Part2",intersections)

if __name__ == "__main__":
	part1()
	part2()