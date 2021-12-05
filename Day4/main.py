def part1():
    data = [l.strip() for l in open("data.txt","r") if l != "\n"]
    calledNumbers = [int(x) for x in data.pop(0).split(",")]

    print(data)
    print(calledNumbers)

if __name__ == "__main__":
    part1()