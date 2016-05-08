def EditDistance(src, dest):
    src_len = len(src)
    dest_len = len(dest)
    d = [[None]*src_len for _ in xrange(dest_len)]

    for i in range(src_len):
        d[i][0] = i
    for j in range(dest_len):
        d[0][j] = j

    for i in range(1, src_len):
        for j in range(1, dest_len):
            if src[i - 1] == dest[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                edIns = d[i][j - 1] + 1  # source insert char
                edDel = d[i - 1][j] + 1  # source delete char
                edRep = d[i - 1][j - 1] + 1  # source replace char
                d[i][j] = min(min(edIns, edDel), edRep)

    return d[src_len-1][dest_len-1]


def main():
    str1 = "SNOWY"
    str2 = "SUNNY"
    print EditDistance(str1, str2)


if __name__ == '__main__':
    main()
