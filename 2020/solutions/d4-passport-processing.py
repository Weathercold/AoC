from re import search
from typing import Callable


CHECKLIST = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]


def read_passport(func: Callable) -> Callable:
    def deco_read_passport():
        passport = ""
        while (inp := func()) not in ["\n", ""]:
            passport += inp
        return passport
    
    return deco_read_passport


inpf = open(r".\2020\input\d4-passport-processing.txt")
inpf.readline = read_passport(inpf.readline)
valid_passports = 0
while (inp := inpf.readline()):
    if all([(i in inp) for i in CHECKLIST]):
        valid_passports += 1
print(valid_passports)


UPDATED_CHECKLIST = [r"byr:(?:19[2-9]\d|200[0-2])[ \n]",
                     r"iyr:20(?:1\d|20)[ \n]",
                     r"eyr:20(?:2\d|30)[ \n]",
                     r"hgt:(?:1(?:[5-8]\d|9[0-3])cm|(?:59|6\d|7[0-6])in)[ \n]",
                     r"hcl:#[0-9a-f]{6}[ \n]",
                     r"ecl:(?:amb|blu|brn|gry|grn|hzl|oth)[ \n]",
                     r"pid:\d{9}[ \n]"]


inpf.seek(0)
valid_passports = 0
while (inp := inpf.readline()):
    if all([search(i, inp) for i in UPDATED_CHECKLIST]):
        valid_passports += 1
print(valid_passports)


inpf.close()