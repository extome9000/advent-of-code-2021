# Easy.

def main():
	data = [tuple(l.strip().split()) for l in open("data.txt","r")]
	position, depth, aim = 0, 0, 0

	for t in data:
		instruction = t[0]
		units = int(t[1])
		if instruction == "forward":
			position += units
			depth += (aim * units)
		elif instruction == "down":
			aim += units
		elif instruction == "up":
			aim -= units
	print(position * depth)

if __name__ == "__main__":
	main()