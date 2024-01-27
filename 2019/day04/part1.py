def valid(value):
    value_str = str(value)

    if len(value_str) != 6:
        return False
    if list(value_str) != sorted(value_str):
        return False
    if len(set(value_str)) == len(value_str):
        return False

    digit_cnt = {}

    for digit in value_str:
        if digit not in digit_cnt:
            digit_cnt[digit] = 1
        else:
            digit_cnt[digit] += 1

    for key in digit_cnt:
        if digit_cnt[key] == 2:
            return True

    return False

if __name__ == "__main__":
    F = 248345
    S = 746315

    print(sum([valid(_) for _ in range(F, S + 1)]))
