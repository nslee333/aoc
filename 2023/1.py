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

    for item in inputs:
        res = 0

        ex = "[0-9]|oneight|one|two|three|four|five|six|seven|eight|nine"

        dict = {
            'one':1, 
            'two': 2, 
            'three': 3, 
            'four': 4, 
            'five': 5, 
            'six': 6, 
            'seven': 7, 
            'eight': 8, 
            'nine': 9
        }



        matches = re.findall(ex, item)
        
        if matches[0] == 'oneight':
            matches[0] = 1
        elif matches[0] in dict:
            matches[0] = dict.get(matches[0])
        
        if matches[-1] == 'oneight':
                matches[-1] = 8
        elif matches[-1] in dict:
            matches[-1] = dict.get(matches[-1])
            
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
