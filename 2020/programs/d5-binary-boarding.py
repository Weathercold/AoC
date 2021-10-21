from os.path import abspath
from functools import reduce


ROWS = (0, 127)
COLUMNS = (0, 7)


inpf = open(abspath(".\input\d5-binary-boarding.txt"))
highest_id = 0
binary_locate = lambda loc, side: (loc[0], (loc[0] + loc[1]) // 2) if side in ["F", "L"] else ((loc[0] + loc[1] + 1) // 2, loc[1])
while (inp := inpf.readline().strip()):
    highest_id = max(highest_id, reduce(binary_locate, inp[:7], ROWS)[0] * 8 + reduce(binary_locate, inp[7:], COLUMNS)[0])
print(highest_id)


inpf.seek(0)
seats = set(range((COLUMNS[1] + 1) * (ROWS[1] + 1)))
while (inp := inpf.readline().strip()):
    seats.remove(reduce(binary_locate, inp[:7], ROWS)[0] * 8 + reduce(binary_locate, inp[7:], COLUMNS)[0])
front_id = -1
for i in sorted(seats):
    if i - front_id == 1: front_id = i
    else: 
        front_id = i
        break
print(front_id)


inpf.close()