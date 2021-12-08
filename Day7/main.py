# Part2 works but it's slow. Done without help.

def part1():
	data = [int(l) for l in open("data.txt","r").readline().split(",")]
	maximum = max(data)

	fuelCosts = []
	for i in range(maximum):
		totalCost = 0
		for n in data:
			totalCost += abs(n-i)
		fuelCosts.append(totalCost)
	
	print("Part1:",min(fuelCosts))

def part2():
	data = [int(l) for l in open("data.txt","r").readline().split(",")]
	maximum = max(data)

	def sumFactorial(n):
		x = 0
		for i in range(n):
			x += (i+1)
		return x

	fuelCosts = []
	for i in range(maximum):
		totalCost = 0
		for n in data:
			totalCost += sumFactorial(abs(n-i))
		fuelCosts.append(totalCost)
	
	print("Part2:",min(fuelCosts))

if __name__ == "__main__":
	part1()
	part2()