'''

WAP to sort a Dictionary by key

'''

#PROGRAM - 2

d = dict()
ls = []
dct = eval(input('Enter a Dictionary to be Sorted : '))
for i in dct:
    ls.append(i)
ls.sort()
d = d.fromkeys(ls)
for i in d:
    d[i] = dct[i]
print('Sorted Dictionary :',d)
    

    





    
