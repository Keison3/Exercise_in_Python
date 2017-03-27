import math


def mysqrt(a):
    '''
    estimate the square root of a
    :param a:
    :return: the square root of a
    '''
    x = 3
    epsilon = 0.0000001
    while True:
        # print(x)
        y = (x + a / x) / 2
        if abs(x - y) < epsilon:
            return y
            break
        x = y


def mysqrt_recrusive(a, x=3):
    '''
    using recrusive to estimate the square root of a
    :param a:
    :return:
    '''
    y = (x + a / x) / 2
    eplison = 0.0000001
    # print(x)
    if abs(x - y) < eplison:
        return y
    x = y
    return mysqrt_recrusive(a, x)


def test_square_root():
    '''
    make the difference between the function mysqrt and math.sqrt
    :param a:
    print a, the respetive result of the function mysqrt and math.sqrt, the diffence between the two function
    '''
    print("a      ", "mysqrt(a)        ", "math.sqrt(a)       ", "diff ")
    print("-      ", "---------------  ", "----------------   ", "-----")
    i = 0.0
    while i < 9:
        i += 1
        sqrt_from_mysqrt = mysqrt(i)
        sqrt_from_math_sqrt = math.sqrt(i)
        diff = abs(sqrt_from_math_sqrt - sqrt_from_math_sqrt)
        print(i, '  ', sqrt_from_mysqrt, '', sqrt_from_math_sqrt, ' ', diff)


# print(mysqrt(1600))
# print(mysqrt_recrusive(1600))
test_square_root()
