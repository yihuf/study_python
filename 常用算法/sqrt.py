pricision = 0.00001    #设置精度值

'''通过二分法实现开根号'''
def sqrt1(number):
    max = number
    min = 0
    mid = (max + min) / 2
    count = 0
    while True:
        count += 1
        if (number - mid * mid).__abs__() < pricision:
            break
        mid = (min + max) / 2
        if (mid * mid) > number:
            max = mid
        elif mid * mid < number:
            min = mid
        else:
            break

    print("value:{},count:{}".format(mid, count))


'''通过牛顿法实现开根号'''
def sqrt2(number):
    x = 1  #设置一个随机值
    count = 0
    while True:
        count += 1
        if (number - x * x).__abs__() < pricision:
            break
        x = (x + number / x) / 2

    print("value:{},count:{}".format(x, count))

sqrt1(2.25)
sqrt1(9)
sqrt1(25)
sqrt1(100)
sqrt1(1000000)
sqrt2(2.25)
sqrt2(9)
sqrt2(25)
sqrt2(100)
sqrt2(1000000)

'''使用牛顿法可以显著提高求根效率'''
