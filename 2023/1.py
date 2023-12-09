import re

# part 1


def part_1():
    inputs = []
    count = 0
    with open('input_1.txt', mode='r', encoding='utf-8') as f:
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

    with open('input_1.txt', mode='r', encoding='utf-8') as f:
        for x in f:
            x = x.replace('\n', '')
            inputs.append(x)

    dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    for item in inputs:

        arr = list(item)
        matches = []
        sub = []

        i = 0
        j = i + 1
        
        while i < len(arr):
            if arr[i].isnumeric():
                matches.append(arr[i])
                break
            
            sub.append(arr[j])
            
            if arr[j].isnumeric():
                matches.append(arr[j])
                break
            
            if len(sub) >= 3 and len(sub) < 6:
                dict_entry = dict.get(''.join(sub))
                if dict_entry:
                    matches.append(dict_entry)
                    break
                
            if len(sub) > 5:
                sub.clear()
                i += 1
                j = i + 1
                sub.append(arr[i])
                continue
            j += 1
        
        i = len(arr) - 1
        j = i - 1
        sub = []
        
            
        while i > 0:
            if arr[i].isnumeric():
                matches.append(arr[i])
                break
            
            sub.append(arr[j])
            
            if arr[j].isnumeric():
                matches.append(arr[j])
                break

            if len(sub) >= 3 and len(sub) < 6:
                dict_entry = dict.get(''.join(sub))
                if dict_entry:
                    matches.append(dict_entry)
                    break

            if len(sub) > 5:
                sub.clear()
                i -= 1
                j = i - 1
                sub.append(arr[i])
                continue
       
        if matches:
            if len(matches) >= 2:
                res = int(str(matches[0]) + str(matches[-1]))
            else:
                res = int(str(matches[0]) + str(matches[0]))
        count += res
    return count

if __name__ == '__main__':
    print(part_2())
    # print(part_1())
