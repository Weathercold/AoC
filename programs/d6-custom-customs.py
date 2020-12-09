from os.path import abspath


inpf = open(abspath(".\inputs\d6-custom-customs.txt"))
identifieds = 0
inp = " "
while inp:
    gr_identifieds = 0
    while (inp := inpf.readline()) not in ["\n", ""]:
        gr_identifieds += len(set(inp.strip()))
    identifieds += gr_identifieds
print(identifieds)


inpf.seek(0)
identifieds = 0
inp = " "
while inp:
    gr_identifieds = set(inpf.readline().strip())
    while (inp := inpf.readline()) not in ["\n", ""]:
        gr_identifieds &= set(inp.strip())
    identifieds += len(gr_identifieds)
print(identifieds)


inpf.close()