buyerDict = {
    '123': 12,
    '234': 2,
    '1234': 132,
    'njcs': 111
}
dic = {}
for i, j in buyerDict.items():
    dic.update({i:j})
for i, j in dic.items():
    print(i,j)