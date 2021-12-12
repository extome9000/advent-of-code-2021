def part1():
	data = [l.strip() for l in open("data.txt","r").readlines()]
	dataDict = {}

	for y in range(100):
		for x in range(100):
			dataDict[tuple([y,x])] = int(data[x][y])

	def getPoint(x,y):
		try:
			return dataDict[(x,y)]
		except KeyError:
			return None

	lowPoints = []
	for y in range(100):
		for x in range(100):
			points = filter(lambda x: x != None,[getPoint(x-1,y),getPoint(x+1,y),getPoint(x,y-1),getPoint(x,y+1)])
			point = dataDict[(x,y)]
			if point < min(points):
				lowPoints.append(point+1)

	print(sum(lowPoints))

if __name__ == "__main__":
	part1()