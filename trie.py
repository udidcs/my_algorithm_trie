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
            st += [copy.deepcopy(''.join(tmp))]
        else:
            tmp += [i]
            cur2 = cur[i]
            getallwords(cur2, st, tmp)
            tmp.pop()
st = []
getallwords(root, st, [])
print(st)


def findnode(cur, word):
    for i in word:
        if i in cur:
            cur = cur[i]
        else:
            return None
    return cur


st = []
word = '바ㄴ'
getallwords(findnode(root, word), st, [])
st = [word + i for i in st]
print(st)