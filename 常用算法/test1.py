
def check_max_right_height(heights):
    cur_height = len(heights[0])
    length = 1
    for height in heights:
        if cur_height > height:
            length += 1
            continue
        else:
            break

    if length == len(heights) + 1:


    return length


case_num = raw_input()
cases = []

for i in range(int(case_num)):
    raw_input()
    case = raw_input()
    cases.append(case)

for case in cases:
    heights = case.split(' ')
    #print(heights)



