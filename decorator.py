inp = ['смартфон:120000',
'яблоко:2',
'сумка:560',
'брюки:2500',
'линейка:10',
'бумага:500'
]
    
def sortit(func):
    def wrapper(*args):
        tempd = func(*args)
        tempd = sorted(tempd)
        tempd = func(tempd)
        tempd = dict(tempd)
        return tempd
    return wrapper



@sortit
def revert(dic):
    res = list()
    for i in dic:
        n,m = i
        try:
            n,m = int(m),n
        except:
            n,m = m,n
        finally:
            res.append((n,m))
    return res


def first3(inp):
    tempd = []
    for el in inp:
        temp = el.split(':')
        tempd.append(tuple(temp))
    tempd = revert(tempd)
    result = []
    for i in tempd.keys():
        result.append(i)
    result = result[:3]
    return result


        
print(*first3(inp))
