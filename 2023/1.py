import re

def part_1():
    inputs = []
    count = 0
    with open('inputs/1.txt', mode='r', encoding='utf-8') as f:
        for x in f:
            x = x.replace('\n', '')
            inputs.append(x)

    for item in inputs:
        res = 0

        matches = re.findall("[0-9]", item)
        if matches:
            if len(matches) >= 2:
                res = int(str(matches[0]) + str(matches[-1]))
            else:
                res = int(str(matches[0]) + str(matches[0]))

        count += res

    return count

def part_2():
    inputs = []
    count = 0

    with open('inputs/1.txt', mode='r', encoding='utf-8') as f:
        for x in f:
            x = x.replace('\n', '')
            inputs.append(x)

    # not my solution, here's what I followed -> https://www.youtube.com/watch?v=rnidYOt9m2o
    for item in inputs:
        digits = []
        for i,v in enumerate(item):
            if v.isdigit():
                digits.append(v)
            for d,c in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if item[i:].startswith(c):
                    digits.append(str(d+1))
        count += int(digits[0] + digits[-1])
    return count

if __name__ == '__main__':
    print(part_2())
    print(part_1())
