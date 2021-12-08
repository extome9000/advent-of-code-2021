def part1():
	data = [l.strip().split(" | ") for l in open("data.txt","r").readlines()]
	lengths = set([2,3,4,7])
	totalDigits = 0

	for i in data:
		totalDigits += len([x for x in i[1].split(" ") if len(x) in lengths])

	print("Part1:",totalDigits)

def part2():
	data = [l.strip().split(" | ") for l in open("data.txt","r").readlines()]
	totalValue = 0
	LEN_FIVE = {(1,1):"2",(0,1):"3",(1,0):"5"}
	LEN_SIX = {(0,0):"9",(0,1):"0",(1,0):"6"}
	LEN_UND = {2:"1",3:"7",4:"4",7:"8"}

	def removeLetters(inp, ref):
		return set(ref) - set(inp.lower())

	for entry in data:
		reference = entry[0].split(" ")
		one = [x for x in reference if len(x) == 2][0]
		four = "".join(removeLetters(one,[x for x in reference if len(x) == 4][0]))
		seven = [x for x in reference if len(x) == 3][0]
		value = ""
		digits = entry[1].split(" ")

		for d in digits:
			mFour = len(removeLetters(d,four))
			mSeven = len(removeLetters(d,seven))
			length = len(d)
			if length == 5:
				value += LEN_FIVE[(mSeven,mFour)]
			elif length == 6:
				value += LEN_SIX[(mSeven,mFour)]
			else:
				value += LEN_UND[length]

		totalValue += int(value)

	print("Part2:",totalValue)

if __name__ == "__main__":
	part1()
	part2()