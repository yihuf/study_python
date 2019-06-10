#coding=utf-8

test = [1, 2, 4, 7, 80, 22, 7, 7, 7, 43, 3, 55, 7, 4, 21, 77]

'''
排序思路：确定一个基准值pos，先从最左边left开始比较，如果left大于等于pos（表明pos左侧均小于pos）则中止比较，
再从最右边right开始比较，如果right小于等于pos（表明pos右侧均大于pos）则中止比较，直到left和right均等于pos
，本轮比较结束，再比较pos左右两边的子序列，直到最后无法分割
'''
def quick_sort(low, high):
    if low >= high:
        return

    pos = low
    left = low
    right = high
    while(True):
        if left >= pos and right <= pos:
            break
        if left < pos:
            if test[left] > test[pos]:
                tmp = test[left]
                test[left] = test[pos]
                test[pos] = tmp
                pos = left
            left+=1

        if right > pos:
            if test[right] < test[pos]:
                tmp = test[right]
                test[right] = test[pos]
                test[pos] = tmp
                pos = right
            right-=1

        print(left, right, pos, test)

    quick_sort(low, pos)
    quick_sort(pos+1, high)


quick_sort(0, len(test)-1)
print(test)
