import sys
from string import ascii_lowercase, ascii_uppercase

def char_score(c):
    if c in ascii_lowercase:
        return ascii_lowercase.index(c) + 1
    elif c in ascii_uppercase:
        return ascii_uppercase.index(c) + 27
    else:
        raise Exception("Invalid character")

def get_common_char(listItems, innerListsLen):
    counterDict = {}

    for ls in listItems:
        for ch in set(ls):
            if ch in counterDict:
                counterDict[ch] += 1
            else:
                counterDict[ch] = 1

    return [k for k, v in counterDict.items() if v == innerListsLen][0]



if __name__ == "__main__":
    totalSum = 0
    position = 0

    groups = []

    for line in sys.stdin.readlines():
        line = line.strip()
        if position // 3 not in groups:
            groups.append([])

        groups[position // 3].append(line)

        position += 1

    for group in groups:
        if group == []:
            continue
        commonChar = get_common_char(group, 3)
        totalSum += char_score(commonChar)

       # print(b, e)
    print(totalSum)