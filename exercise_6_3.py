def first(word):
    '''
    获得字符串的第一个元素
    word parameter：（type）string
    :param word:
    :return:
    '''
    return word[0]

def last(word):
    '''
    获得字符串的最后一个元素
    word parameter：（type）string
    :param word:
    :return:
    '''
    return word[-1]

def middle(word):
    '''
    获取字符串除了首尾元素剩下的部分
    word parameter：（type）string
    :param word:
    :return:
    '''
    return word[1: -1]

def is_palindrome(word):
    '''
    判断一个字符串是否为回文字符串,是的话返回True；否则返回False
    word parameter：（type）string
    :param word:
    :return:
    '''
    if len(word) == 0:
        print("输入的字符串为空！")
        return False
    first_word = first(word)
    last_word = last(word)
    middle_word = middle(word)
    if len(word) <= 1:
        return True
    elif first_word != last_word:
        return False
    return is_palindrome(middle_word)

print(is_palindrome(''))
print(is_palindrome('hhhahh'))
print(is_palindrome('hhhahhh'))
