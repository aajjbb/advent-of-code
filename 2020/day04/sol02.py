import functools
import re
import sys

REQUIRED_FIELDS = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

passports = []
buffer = []
valid_cnt = 0

def valid_field(field_name, raw_content):
    content = raw_content.replace(field_name, '')

    if field_name == 'byr:':
        return 1920 <= int(content) <= 2002
    elif field_name == 'iyr:':
        return 2010 <= int(content) <= 2020
    elif field_name == 'eyr:':
        return 2020 <= int(content) <= 2030
    elif field_name == 'hgt:':
        unit = content[-2:]
        content = content[:-2]

        if unit == 'cm':
            return 150 <= int(content) <= 193
        elif unit == 'in':
            return 59 <= int(content) <= 76
        else:
            return False
    elif field_name == 'hcl:':
        return re.search("#[0-9a-f]{6}", content)
    elif field_name == 'ecl:':
        return content in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif field_name == 'pid:':
        return re.search("[0-9]{9}", content)

    return False

def is_valid(passport):
    for req_field in REQUIRED_FIELDS:
        valid = False

        for field in passport:
            if req_field in field and valid_field(req_field, field):
                valid = True

        if not valid:
            return False
    return True

for line in sys.stdin:
    line_content = str(line).replace('\r\n', '')

    if line_content == '':
        passports.append(buffer)
        buffer = []
        continue

    tokens = line_content.split(" ")
    buffer = buffer + tokens

if buffer != []:
    passports.append(buffer)

for passport in passports:
    if is_valid(passport):
        valid_cnt += 1

print(valid_cnt)