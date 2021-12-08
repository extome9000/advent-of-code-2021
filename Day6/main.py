# Part 1 done without help. Part 2 done with some reference.
def part1():
	with open("data.txt","r") as file:
		data = file.readline().split(",")
		data = [int(x) for x in data]

	days = 80

	def fish(l: list) -> list[int]:
		nl = []
		for lanternfish in l:
			if lanternfish == 0:
				nl.append(6)
				nl.append(8)
			else:
				nl.append(lanternfish-1)
		return nl

	for _ in range(days):
		data = fish(data)

	print(len(data))

def part2():
	with open("data.txt","r") as file:
		d = [int(x) for x in file.readline().split(",")]
	data = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
	for i in d:
		data[i] += 1

	days = 256

	for _ in range(days):
		zeroes = data[0]
		data[0] = 0
		for i in range(1,len(data)):
			data[i-1] += data[i]
			data[i] = 0
		data[6] += zeroes
		data[8] += zeroes

	total = 0
	for i,v in data.items():
		total += v

	print(total)
	# 142767123209

if __name__ == "__main__":
	part1()
	part2()