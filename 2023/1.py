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


    with open('input_2.txt', mode='r', encoding='utf-8') as f:
        for x in f:
            x = x.replace('\n', '')
            inputs.append(x)

    for item in inputs:
        
        start = 0
        end = 0
        
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
        
        arr = list(item)
        matches = []
        
        while len(matches) < 1:
            sub = []
            for it in arr:
                print(item)
                print(sub)
                sub.append(it)
                
                if it.isnumeric():
                    matches.append(it)
                    break
                
                if len(sub) >= 3 and len(sub) < 6:
                    # print(str(sub))
                    # print(''.join(sub) in dict, "DORK")
                    if ''.join(sub) in dict:
                        # print("what")
                        matches.append(dict.get(''.join(sub)))
                        break
                    continue
                # print(len(sub))
                # print(len(sub) > 5)
                if len(sub) > 5:
                    # print("HIHIH")
                    sub.pop(-2)
                    sub.pop(-1)
                    sub.pop(0)
                    continue
                
        # print(item)
        # print(matches)
            
        # while len(matches) < 2:
            
            
                
            
            
        
        # ex = "[0-9]|oneight|one|two|three|four|five|six|seven|eight|nine"

        
    
    #     matches = re.findall(ex, item)
        
        
    #     if matches[0] in dict:
    #         matches[0] = dict.get(matches[0])
        
    #     if matches[-1] in dict:
    #         matches[-1] = dict.get(matches[-1])
            
    #     if matches:
    #         if len(matches) >= 2:
    #             res = int(str(matches[0]) + str(matches[-1]))
    #         else:
    #             res = int(str(matches[0]) + str(matches[0]))
    #     count += res

    # return count
    

if __name__ == '__main__':
    print(part_2())
    # print(part_1())
