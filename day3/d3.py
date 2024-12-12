import re

with open("./day3/input", "r") as f:
    line = f.read()

# cut the between parts and the part after the last don't
line = re.sub(r"don't\(\).*?do\(\)", "", line, flags=re.DOTALL)
line = re.sub(r"don't\(\).*$", "", line, flags=re.DOTALL)

muls = re.findall(r"mul\((\d+),(\d+)\)", line)
sum = 0
for mul in muls:
    sum += int(mul[0]) * int(mul[1])
print(sum)