import re
import regex

r = re.compile(r"mul\((\d+),(\d+)\)")
dont = re.compile(r"don\'t\(\)")
do = re.compile(r"do\(\)")
with open("./day3/input") as f:
    d = f.read()

print(sum([int(i)*int(j) for i,j in r.findall(d)]))

donts = [d.start() for d in dont.finditer(d)]
dos = [d.start() for d in do.finditer(d)]
pos = 0
last_do = 0
last_dont = 0 
sum_of_muls = 0

while pos < len(d):
    if pos == 0:
        sum_of_muls += sum([int(i)*int(j) for i,j in r.findall(d,endpos=donts[0])])
        pos = donts[0]+len("don't()")
        last_dont = donts[0]
        continue
    try:
        next_do = [i for i in dos if i>last_dont][0]
        next_dont = [i for i in donts if i>next_do][0]
        sum_of_muls += sum([int(i)*int(j) for i,j in r.findall(d,pos=next_do,endpos=next_dont)])
        last_dont = next_dont
        last_do = next_do
    except:
        break
    
print(sum_of_muls)