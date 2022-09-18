import copy

root = None

def add(word, root):
    cur = root
    cnt = 0
    for i in word:
        cnt += 1
        if i in cur:
            cur = cur[i]
            continue

        if cnt == len(word):
            cur[i] = '*'
        else:
            cur[i] = {}
        cur = cur[i]

    return root

root = {}
root = add('banana', root)
root = add('baguni', root)
root = add('ascii', root)
print(root)


def getallwords(cur, st, tmp):
    for i in cur:
        if cur[i] == '*':
            tmp += [i]
            st += [copy.deepcopy(''.join(tmp))]
            tmp.pop()
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
            return False
    return cur

st = []
word = 'asci'
getallwords(findnode(root, word), st, [])
st = [word + i for i in st]

print(st)