'''

WAP to sort a Dictionary by key

'''

#PROGRAM - 1(Shortcut)

d = dict()
dct1 = eval(input('Enter a Dictionary to be Sorted : '))
for key in sorted(dct1.keys()):
    d[key] = dct1[key]
print('Sorted Dictionary :',d)




    
