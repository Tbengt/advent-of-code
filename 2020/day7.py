import sys
import re
from typing import Dict


def find_gold_bag(bag: str, bag_regulations: Dict[str, Dict[str, int]]) -> bool:
    if "shiny gold bag" in bag_regulations[bag]:
        return True
    elif len(bag_regulations[bag]) == 0:
        return False
    else:
        found = False
        for b in bag_regulations[bag]:
            found = found or find_gold_bag(b, bag_regulations)
        return found


def remove_plural_s(bag: str) -> str:
    if bag.endswith("s"):
        return bag[0:-1]
    else:
        return bag


if __name__ == "__main__":
    bag_regulations_raw = []
    for line in sys.stdin:
        bag_regulations_raw.append(line.strip())
    print(bag_regulations_raw)

    bag_regulations_parsed = {}
    for line in bag_regulations_raw:
        bag, subbags = line.split("contain")
        subbag_dict = {}
        for subbag in subbags.split(","):
            number_match = re.search("[0-9]+", subbag)
            bag_match = re.findall('[a-z ]+', subbag.strip())
            if number_match is not None:
                subbag_dict[remove_plural_s(bag_match[0].strip())] = number_match.group(0)
        bag_regulations_parsed[remove_plural_s(bag.strip())] = subbag_dict

    print(bag_regulations_parsed)

    # for each bag, see if we can get to the gold bag
    count = 0
    for bag in bag_regulations_parsed:
        if find_gold_bag(bag, bag_regulations_parsed):
            count += 1
    print(count)
