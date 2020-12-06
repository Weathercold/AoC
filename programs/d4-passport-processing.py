from os.path import abspath
from re import search


CHECKLIST = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]


def readpassport(func):
    def deco_readpassport():
        passport = ""
        while (inp := func()) not in ["\n", ""]:
            passport += inp
        return passport
    
    return deco_readpassport


inpf = open(abspath(".\inputs\d4-passport-processing.txt"))
inpf.readline = readpassport(inpf.readline)
valid_passports = 0
while (inp := inpf.readline()):
    if all([(i in inp) for i in CHECKLIST]):
        valid_passports += 1
print(valid_passports)


UPDATED_CHECKLIST = ["byr:(?:19[2-9]\d|200[0-2])[ \n]",
                     "iyr:20(?:1\d|20)[ \n]",
                     "eyr:20(?:2\d|30)[ \n]",
                     "hgt:(?:1(?:[5-8]\d|9[0-3])cm|(?:59|6\d|7[0-6])in)[ \n]",
                     "hcl:#[0-9a-f]{6}[ \n]",
                     "ecl:(?:amb|blu|brn|gry|grn|hzl|oth)[ \n]",
                     "pid:\d{9}[ \n]"]


inpf.seek(0)
valid_passports = 0
while (inp := inpf.readline()):
    if all([search(i, inp) for i in UPDATED_CHECKLIST]):
        valid_passports += 1
print(valid_passports)