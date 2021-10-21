from os.path import abspath
from re import split
from functools import cached_property, lru_cache
from itertools import chain
from typing import Iterator, Dict, List, Tuple


class Bag(object):
    
    def __init__(self, bag_color: str, contains: List[Tuple[int, str]]) -> None:
        self.bag_color = bag_color
        self.contains = contains if contains != [("no", "other")] else []
    
    @lru_cache
    def __len__(self) -> int:
        length = sum(bag_types[i[1]]._rec__len__() * int(i[0]) for i in self.contains)
        return length
    
    @lru_cache
    def _rec__len__(self) -> int:
        length = sum(bag_types[i[1]]._rec__len__() * int(i[0]) for i in self.contains) + 1
        return length
    
    @cached_property
    def items(self) -> Iterator[str]:
        items = chain.from_iterable([bag_types[i[1]]._rec_items for i in self.contains])
        return items
    
    @cached_property
    def _rec_items(self) -> List[str]:
        items = [self.bag_color]
        items.extend([bag_types[i[1]]._rec_items for i in self.contains])
        return items


inpf = open(abspath(r".\2020\input\d7-handy-haversacks.txt"))
bag_types: Dict[str, Bag] = {}
for inp in inpf:
    parsed_inp = split(" bag(?:s)?(?:, |\.)?(?: contain )?", inp)
    parsed_items = [tuple(split(" ", i, 1)) for i in parsed_inp[1:-1]]
    bag_types.update({parsed_inp[0]: Bag(parsed_inp[0], parsed_items)})


s = 0
for bag in bag_types.values():
    if "shiny gold" in bag.items:
        s += 1
print(s)


print(len(bag_types["shiny gold"]))