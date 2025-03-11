
inputs = []
def get_input():
    with open('inputs/2.txt', 'r', encoding='utf-8') as f:
        for x in f:
            x = x.replace('\n', '')
            inputs.append(x)


# possible for 12 red, 13 green, 14 blue
# [12, red], [13, green], [14, blue]
# {red: 12, green: 13, blue: 14}
def part_1():
    get_input()
    # idea = []
    # print(list(inputs[0]))
    li = list(inputs[0])
    for i, item in enumerate(li):
        if item == ' ':
            li.remove(item)
    li_new = ''.join(li)
    l = li_new.split(';')
    # print(l)
    j = []
    for k,v in enumerate(l):
        o = v.split(":")
        # print(o)
        for item in o: j.append(item)
        # i = o[0].split(",")
        # j.append(o)
        # j.append(i)
    print(j)
            
            
    # new = inputs[0].split(':')
    # new[0] = new[0].replace('Game ', '')
    # idea.append(int(new[0]))
    
    # inputs = inputs.replace('Game ')
    
    # print(idea)
    # idea.append
    # print(new)
    # # inputs[0].split(';')
    # new = new[0].split('')
    # print(new)
    


# Looking for games that are possible, then adding their ids up.


# ; = end of subset

# 3 blue, 2 green, FALSE
# 

if __name__ == '__main__':
    part_1()
