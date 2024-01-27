import functools
import sys

REQUIRED_FIELDS = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

passports = []
buffer = []
valid_cnt = 0

def is_valid(passport):
    for req_field in REQUIRED_FIELDS:
        valid = False

        for field in passport:
            if req_field in field:
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