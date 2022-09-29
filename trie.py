import copy

root = None

def add(word, cur):
    for i in word:
        if i in cur:
            cur = cur[i]
            continue
        else:
            cur[i] = {}
            cur = cur[i]
    cur['*'] = '*'

    return root

root = {}
root = add('바나나', root)
root = add('바구니', root)
root = add('아스키', root)
print(root)


def getallwords(cur, st, tmp):
    for i in cur:
        if cur[i] == '*':
            st += [''.join(tmp)]
        else:
            tmp += [i]
            getallwords(cur[i], st, tmp)
            tmp.pop()
st = []
getallwords(root, st, [])


def findnode(cur, word):
    for i in word:
        if i in cur:
            cur = cur[i]
        else:
            return None
    return cur


st = []
word = '바'
getallwords(findnode(root, word), st, [])
st = [word + i for i in st]
print(st)