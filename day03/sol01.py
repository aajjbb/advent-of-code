import sys
from string import ascii_lowercase, ascii_uppercase

def char_score(c):
    if c in ascii_lowercase:
        return ascii_lowercase.index(c) + 1
    elif c in ascii_uppercase:
        return ascii_uppercase.index(c) + 27
    else:
        raise Exception("Invalid character")

def get_common_char(sa, sb):
    counterDict = {}
    matchingChars = set()

    for ch in sa:
        counterDict[ch] = True

    for ch in sb:
        if ch in counterDict:
            matchingChars.add(ch)

    if len(matchingChars) > 1:
        print(sa, sb, matchingChars)
        raise Exception("More than 1 matching character")

    return matchingChars.pop()



if __name__ == "__main__":
    totalSum = 0

    for line in sys.stdin.readlines():
        line = line.strip()
        if len(line) % 2 != 0:
            raise Exception("Odd len input")
        segmentSize = len(line) // 2
        print(segmentSize)

        b = line[:segmentSize]
        e = line[segmentSize:]

        if len(b) != len(e):
            raise Exception("Incorrectly segment size.")

        commonChar = get_common_char(b, e)
        totalSum += char_score(commonChar)

       # print(b, e)
    print(totalSum)