def most_frequent(a):
    d = dict()
    for key in a:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

a = input('String:- ')
print (most_frequent(a))

string:- mississippi
{'m': 1, 'i': 4, 's': 4, 'p': 2}
