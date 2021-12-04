# Easy, although required some thinking.
# Hacky solution with strings, would be nicer if it used bitwise operations.

def part1():
	data = [l.strip() for l in open("data.txt","r")]
	gamma, epsilon = "",""

	for i in range(12):
		t0, t1 = 0, 0
		for byte in data:
			if byte[i] == "0":
				t0 += 1
			elif byte[i] == "1":
				t1 += 1
		if t0 > t1:
			gamma += "0"
			epsilon += "1"
		else:
			gamma += "1"
			epsilon += "0"
	print("Part1:",int(gamma,2)*int(epsilon,2))

def part2():
	data = [l.strip() for l in open("data.txt","r")]
	oxygenList, co2List = data, data

	for i in range(12):
		t0, t1 = 0, 0
		for byte in oxygenList:
			if byte[i] == "0":
				t0 += 1
			elif byte[i] == "1":
				t1 += 1
		if t0 > t1:
			oxygenList = [x for x in oxygenList if x[i] == "0"]
		else:
			oxygenList = [x for x in oxygenList if x[i] == "1"]
		if len(oxygenList) == 1:
			break

	for i in range(12):
		t0, t1 = 0, 0
		for byte in co2List:
			if byte[i] == "0":
				t0 += 1
			elif byte[i] == "1":
				t1 += 1
		if t0 > t1:
			co2List = [x for x in co2List if x[i] == "1"]
		else:
			co2List = [x for x in co2List if x[i] == "0"]
		if len(co2List) == 1:
			break

	print(int(oxygenList[0],2)*int(co2List[0],2))

if __name__ == "__main__":
	part1()
	part2()