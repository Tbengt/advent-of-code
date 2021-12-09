import sys
import re
import numpy as np

def verify_passport(passport_str: str) -> bool:
    passport_fields = passport_str.split(" ")
    if len(passport_fields) == 8:
        return True
    elif len(passport_fields) == 7 and -1 == passport_str.find("cid"):
        return True
    return False

def validate_byr(byr : int) -> bool:
    return 1920 <= byr <= 2002

def validate_iyr(iyr : int) -> bool:
    return 2010 <= iyr <= 2020

def validate_eyr(eyr: int) -> bool:
    return 2020 <= eyr <= 2030

def get_unit(measurement: str) -> str:
    if measurement.endswith("cm"):
        return "cm"
    if measurement.endswith("in"):
        return "in"

    return "invalid"

def validate_hgt(hgt: str) -> bool:
    unit = get_unit(hgt)
    height = int(hgt.strip(unit))
    if unit == "cm":
        return 150 <= height <= 193
    if unit == "in":
        return 59 <= height <= 76
    return False

def validate_hcl(hcl : str) -> bool:
    return re.fullmatch("#[a-f0-9]{6}", hcl) is not None

def validate_ecl(ecl: str) -> bool:
    valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in valid_colours

def validate_pid(pid: str) -> bool:
    return re.fullmatch("[0-9]{9}", pid) is not None

def validate_passport(passport_str: str) -> bool:
    passport_fields = passport_str.split(" ")
    passport_dict = {}
    for field in passport_fields:
        name, value = field.split(":")
        passport_dict[name] = value

    if not validate_byr(int(passport_dict["byr"])):
        print("failed byr " + passport_dict["byr"])
        return False

    if not validate_iyr(int(passport_dict["iyr"])):
        print("failed iyr " + passport_dict["iyr"])
        return False

    if not validate_eyr(int(passport_dict["eyr"])):
        print("failed eyr " + passport_dict["eyr"])
        return False

    if not validate_hgt(passport_dict["hgt"]):
        print("failed hgt " + passport_dict["hgt"])
        return False

    if not validate_hcl(passport_dict["hcl"]):
        print("failed hcl " + passport_dict["hcl"])
        return False

    if not validate_pid(passport_dict["pid"]):
        print("failed pid " + passport_dict["pid"])
        return False

    if not validate_ecl(passport_dict["ecl"]):
        print("failed ecl " + passport_dict["ecl"])
        return False

    return True


if __name__ == "__main__":
    sonar_measurements = []
    for line in sys.stdin:
        sonar_measurements.append(int(line.strip()))

    # A
    print(np.sum(np.array(sonar_measurements[1:]) - np.array(sonar_measurements[:-1]) > 0))

    # B
    print(np.sum(np.array(sonar_measurements[3:]) - np.array(sonar_measurements[:-3]) > 0))



