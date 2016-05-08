class CharItem:
    c = None        # char
    value = None    # number
    leading = None  # 0 can't be first char

    def __init__(self, c, value, leading):
        self.c = c
        self.value = value
        self.leading = leading


class CharValue:
    value = None
    used = None

    def __init__(self, value, used):
        self.value = value
        self.used = used


# CharItem[] c_i
# string str
def MakeIntegerValue(c_i, word):
    integer = 0
    str_len = len(word)
    for pointer, c in enumerate(word):
        value = [char_item.value for char_item in c_i if char_item.c == c and char_item.value is not None].pop()
        integer += value * 10**(str_len - pointer - 1)
    return integer


# CharItem[] c_i
def OnCharListReady(c_i):
    minuend = "WWWDOT"
    subtrahead = "GOOGLE"
    diff = "DOTCOM"

    m = MakeIntegerValue(c_i, minuend)
    s = MakeIntegerValue(c_i, subtrahead)
    d = MakeIntegerValue(c_i, diff)
    # print m, s, d
    if m - s == d:
        print "%d - %d = %d" % (m, s, d)


# CharItem char_item
# CharValue char_value
def IsValueValid(char_item, char_value):
    if char_value.used or (char_item.leading and char_value.value == 0):
        return False
    return True


# CharItem[] c_i
# CharValue[] c_v
# int index
def SearchingResult(c_i, c_v, index):
    if index == len(c_i):
        OnCharListReady(c_i)
        return

    for i in range(len(c_v)):
        if IsValueValid(c_i[index], c_v[i]):
            c_v[i].used = True  # set used sign
            c_i[index].value = c_v[i].value
            SearchingResult(c_i, c_v, index + 1)
            c_v[i].used = False  # clear used sign


def main():
    # WWWDOT - GOOGLE = DOTCOM
    char_item = [CharItem('W', None, True), CharItem('D', None, True), CharItem('O', None, False),
                 CharItem('T', None, False), CharItem('G', None, True), CharItem('L', None, False),
                 CharItem('E', None, False), CharItem('C', None, False), CharItem('M', None, False)]
    char_value = [CharValue(0, False), CharValue(1, False), CharValue(2, False), CharValue(3, False),
                  CharValue(4, False), CharValue(5, False), CharValue(6, False), CharValue(7, False),
                  CharValue(8, False), CharValue(9, False)]
    SearchingResult(char_item, char_value, 0)


if __name__ == '__main__':
    main()
