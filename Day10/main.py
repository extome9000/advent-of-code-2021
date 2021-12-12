import re

def part1():
	data = [l.strip() for l in open("data.txt","r").readlines()]
	ERROR_POINTS = {")":3,"]":57,"}":1197,">":25137}

	def reduce(l):
		h = re.sub(r"\(\)|\[\]|\{\}|\<\>","",l)
		if h == l:
			return h
		else:
			return reduce(h)

	total = 0
	for line in data:
		for char in reduce(line):
			try:
				total += ERROR_POINTS[char]
				break
			except KeyError:
				pass

	print("Part1:",total)

def part2():
	data = [l.strip() for l in open("data.txt","r").readlines()]
	CHAR_FLIPPED = {"(":")","[":"]","{":"}","<":">"}
	CHAR_SCORES = {")":1,"]":2,"}":3,">":4}

	def reduce(l):
		h = re.sub(r"\(\)|\[\]|\{\}|\<\>","",l)
		if h == l:
			return h
		else:
			return reduce(h)

	data = [reduce(line) for line in data if not re.search("\)|\]|\}|\>",reduce(line))]

	totalScores = []
	for line in data:
		flippedLine = [CHAR_FLIPPED[x] for x in line][::-1]
		score = 0
		for char in flippedLine:
			score *= 5
			score += CHAR_SCORES[char]
		totalScores.append(score)
	totalScores.sort()

	print("Part2:",totalScores[len(totalScores)//2])

if __name__ == "__main__":
	part1()
	part2()