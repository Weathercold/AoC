from itertools import count
from os.path import abspath


def rtransform(subject_number: int) -> int:
    value = 1
    for loop_size in count(start=1):
        if (value := (value * 7) % 20201227) == subject_number:
            return loop_size

def transform(subject_number: int, loop_size: int) -> int:
    value = 1
    for i in range(loop_size):
        value = (value * subject_number) % 20201227
    return value


def main():
    inpf = open(abspath(".\inputs\d25-combo-breaker.txt"))
    card_public_key, door_public_key = map(int, inpf.readlines())
    card_loop_size, door_loop_size = rtransform(card_public_key), rtransform(door_public_key)
    card_encryption_key, door_encryption_key = transform(door_public_key, card_loop_size), transform(card_public_key, door_loop_size)
    print(card_encryption_key)
    

main()
