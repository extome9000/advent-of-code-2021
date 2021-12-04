# Easy.

def main():
	data = [int(l.strip()) for l in open("data.txt","r")]

	total = 0
	for i,n in zip(data,data[1:]):
		if i < n:
			total += 1
	print(total)

	threesum_data = []
	for i,n,p in zip(data,data[1:],data[2:]):
		threesum_data.append(i+n+p)
	total = 0
	for i,n in zip(threesum_data,threesum_data[1:]):
		if i < n:
			total += 1
	print(total)


if __name__ == "__main__":
	main()