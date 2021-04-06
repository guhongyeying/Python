#https://blog.csdn.net/v_july_v/article/details/7041827

def get_next(pstr):

    plen = len(pstr)
    next = [-1]*plen
    k = -1
    j = 0
    while j < plen-1:
        if k ==-1 or pstr[k] == pstr[j]:
            k+=1
            j+=1

            if pstr[k] != pstr[j]:
                next[j] = k
            else:
                next[j] = next[k]

        else:

            k = next[k]
    return next


def search_kmp():
    sstr = "AGSDEDABAGABCDABDDDDE"
    pstr = "ABCDABD"
    sien = len(sstr)
    plen = len(pstr)
    i = 0
    j = 0
    next = get_next(pstr)
    print(next)
    while (i < sien and j < plen ):
        if j == -1 or sstr[i] == pstr[j]:
            i+=1
            j+=1
        else:

            j = next[j]

    if j == plen:
        print(i)
        return i-j
    else:
        return -1


rst = search_kmp()
print(rst)


# if __name__ == '__main__':
#     next = cal_next("ababab",6)
#     print(next)

